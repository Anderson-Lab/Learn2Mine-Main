"""Cache object

The Cache object is used to manage a set of cache files and their
associated backend. The backends can be rotated on the fly by
specifying an alternate type when used.

Advanced users can add new backends in beaker.backends

"""
import pkg_resources
import warnings

import beaker.container as container
import beaker.util as util
from beaker.exceptions import BeakerException, InvalidCacheBackendError

# Initialize the basic available backends
clsmap = {
          'memory':container.MemoryNamespaceManager,
          'dbm':container.DBMNamespaceManager,
          'file':container.FileNamespaceManager,
          }


# Load up the additional entry point defined backends
for entry_point in pkg_resources.iter_entry_points('beaker.backends'):
    try:
        NamespaceManager = entry_point.load()
        name = entry_point.name
        if name in clsmap:
            raise BeakerException("NamespaceManager name conflict,'%s' "
                                  "already loaded" % name)
        clsmap[name] = NamespaceManager
    except (InvalidCacheBackendError, SyntaxError):
        # Ignore invalid backends
        pass
    except:
        import sys
        from pkg_resources import DistributionNotFound
        # Warn when there's a problem loading a NamespaceManager
        if not isinstance(sys.exc_info()[1], DistributionNotFound):
            import traceback
            from StringIO import StringIO
            tb = StringIO()
            traceback.print_exc(file=tb)
            warnings.warn("Unable to load NamespaceManager entry point: '%s': "
                          "%s" % (entry_point, tb.getvalue()), RuntimeWarning,
                          2)


# Load legacy-style backends
try:
    import beaker.ext.memcached as memcached
    clsmap['ext:memcached'] = memcached.MemcachedNamespaceManager
except InvalidCacheBackendError, e:
    clsmap['ext:memcached'] = e

try:
    import beaker.ext.database as database
    clsmap['ext:database'] = database.DatabaseNamespaceManager
except InvalidCacheBackendError, e:
    clsmap['ext:database'] = e

try:
    import beaker.ext.sqla as sqla
    clsmap['ext:sqla'] = sqla.SqlaNamespaceManager
except InvalidCacheBackendError, e:
    clsmap['ext:sqla'] = e

try:
    import beaker.ext.google as google
    clsmap['ext:google'] = google.GoogleNamespaceManager
except (InvalidCacheBackendError, SyntaxError), e:
    clsmap['ext:google'] = e


class Cache(object):
    """Front-end to the containment API implementing a data cache.

    ``namespace``
        the namespace of this Cache

    ``type``
        type of cache to use

    ``expire``
        seconds to keep cached data

    ``expiretime``
        seconds to keep cached data (legacy support)

    ``starttime``
        time when cache was cache was
    """
    def __init__(self, namespace, type='memory', expiretime=None,
                 starttime=None, expire=None, **nsargs):
        try:
            cls = clsmap[type]
            if isinstance(cls, InvalidCacheBackendError):
                raise cls
        except KeyError:
            raise TypeError("Unknown cache implementation %r" % type)
            
        self.namespace = cls(namespace, **nsargs)
        self.expiretime = expiretime or expire
        self.starttime = starttime
        self.nsargs = nsargs
        
    def put(self, key, value, **kw):
        self._get_value(key, **kw).set_value(value)
    set_value = put
    
    def get(self, key, **kw):
        """Retrieve a cached value from the container"""
        return self._get_value(key, **kw).get_value()
    get_value = get
    
    def remove_value(self, key, **kw):
        mycontainer = self._get_value(key, **kw)
        if mycontainer.has_current_value():
            mycontainer.clear_value()
    remove = remove_value

    def _get_value(self, key, **kw):
        if isinstance(key, unicode):
            key = key.encode('ascii', 'backslashreplace')

        if 'type' in kw:
            return self._legacy_get_value(key, **kw)

        kw.setdefault('expiretime', self.expiretime)
        kw.setdefault('starttime', self.starttime)
        
        return container.Value(key, self.namespace, **kw)
    
    def _legacy_get_value(self, key, type, **kw):
        expiretime = kw.pop('expiretime', self.expiretime)
        starttime = kw.pop('starttime', None)
        createfunc = kw.pop('createfunc', None)
        kwargs = self.nsargs.copy()
        kwargs.update(kw)
        c = Cache(self.namespace.namespace, type=type, **kwargs)
        return c._get_value(key, expiretime=expiretime, createfunc=createfunc, 
                            starttime=starttime)
    _legacy_get_value = util.deprecated(_legacy_get_value, "Specifying a "
        "'type' and other namespace configuration with cache.get()/put()/etc. "
        "is deprecated. Specify 'type' and other namespace configuration to "
        "cache_manager.get_cache() and/or the Cache constructor instead.")
    
    def clear(self):
        """Clear all the values from the namespace"""
        self.namespace.remove()
    
    # dict interface
    def __getitem__(self, key):
        return self.get(key)
    
    def __contains__(self, key):
        return self._get_value(key).has_current_value()
    
    def has_key(self, key):
        return key in self
    
    def __delitem__(self, key):
        self.remove_value(key)
    
    def __setitem__(self, key, value):
        self.put(key, value)


class CacheManager(object):
    def __init__(self, **kwargs):
        """Initialize a CacheManager object with a set of options
        
        Options should be parsed with the
        :func:`~beaker.util.parse_cache_config_options` function to
        ensure only valid options are used.
        
        """
        self.kwargs = kwargs
        self.caches = {}
        self.regions = kwargs.pop('cache_regions', {})
    
    def get_cache(self, name, **kwargs):
        kw = self.kwargs.copy()
        kw.update(kwargs)
        return self.caches.setdefault(name + str(kw), Cache(name, **kw))
    
    def get_cache_region(self, name, region):
        if region not in self.regions:
            raise BeakerException('Cache region not configured: %s' % region)
        kw = self.regions[region]
        return self.caches.setdefault(name + str(kw), Cache(name, **kw))
    
    def region(self, region, *args):
        """Decorate a function to cache itself using a cache region
        
        The region decorator requires arguments if there are more than
        2 of the same named function, in the same module. This is
        because the namespace used for the functions cache is based on
        the functions name and the module.
        
        
        Example::
            
            # Assuming a cache object is available like:
            cache = CacheManager(dict_of_config_options)
            
            
            def populate_things():
                
                @cache.region('short_term', 'some_data')
                def load(search_term, limit, offset):
                    return load_the_data(search_term, limit, offset)
                
                return load('rabbits', 20, 0)
        
        .. note::
            
            The function being decorated must only be called with
            positional arguments.
        
        """
        cache = [None]
        key = " ".join(str(x) for x in args)
        
        def decorate(func):
            def cached(*args):
                reg = self.regions[region]
                if not reg.get('enabled', True):
                    return func(*args)
                
                if not cache[0]:
                    namespace = util.func_namespace(func)
                    cache[0] = self.get_cache_region(namespace, region)
                
                cache_key = key + " " + " ".join(str(x) for x in args)
                def go():
                    return func(*args)
                
                return cache[0].get_value(cache_key, createfunc=go)
            return cached
        return decorate

    def cache(self, *args, **kwargs):
        """Decorate a function to cache itself with supplied parameters

        ``args`` 
            used to make the key unique for this function, as in region()
            above.

        ``kwargs``
            parameters to be passed to get_cache(), will override defaults

        Example::

            # Assuming a cache object is available like:
            cache = CacheManager(dict_of_config_options)
            
            
            def populate_things():
                
                @cache.cache('mycache', expire=15)
                def load(search_term, limit, offset):
                    return load_the_data(search_term, limit, offset)
                
                return load('rabbits', 20, 0)
        
        .. note::
            
            The function being decorated must only be called with
            positional arguments. 

        """
        cache = [None]
        key = " ".join(str(x) for x in args)
        
        def decorate(func):
            def cached(*args):
                if not cache[0]:
                    namespace = util.func_namespace(func)
                    cache[0] = self.get_cache(namespace, **kwargs)
                cache_key = key + " " + " ".join(str(x) for x in args)
                def go():
                    return func(*args)

                return cache[0].get_value(cache_key, createfunc=go)
            return cached
        return decorate
