"""
Support for integration with the Biostar Q&A application
"""

from galaxy.web.base.controller import BaseUIController, url_for, error, web

import base64
from galaxy.util import json
import hmac

# Slugifying from Armin Ronacher (http://flask.pocoo.org/snippets/5/)

import re
from unicodedata import normalize

_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')


def slugify(text, delim=u'-'):
    """Generates an slightly worse ASCII-only slug."""
    result = []
    for word in _punct_re.split(text.lower()):
        word = normalize('NFKD', word).encode('ascii', 'ignore')
        if word:
            result.append(word)
    return unicode(delim.join(result))


# Biostar requires all keys to be present, so we start with a template
DEFAULT_PAYLOAD = {
    'email': "",
    'title': "",
    'tags': 'galaxy',
    'tool_name': '',
    'tool_version': '',
    'tool_id': ''
}


def encode_data( key, data ):
    """
    Encode data to send a question to Biostar
    """
    text = json.to_json_string(data)
    text = base64.urlsafe_b64encode(text)
    digest = hmac.new(key, text).hexdigest()
    return text, digest


def tag_for_tool( tool ):
    """
    Generate a reasonavle biostar tag for a tool.
    """
    return slugify( unicode( tool.name ) )


class BiostarController( BaseUIController ):
    """
    Provides integration with Biostar through external authentication, see: http://liondb.com/help/x/
    """

    @web.expose
    def biostar_redirect( self, trans, payload=None, biostar_action=None ):
        """
        Generate a redirect to a Biostar site using external authentication to
        pass Galaxy user information and information about a specific tool.
        """
        payload = payload or {}
        # Ensure biostar integration is enabled
        if not trans.app.config.biostar_url:
            return error( "Biostar integration is not enabled" )
        # Start building up the payload
        payload = dict( DEFAULT_PAYLOAD, **payload )
        # Do the best we can of providing user information for the payload
        if trans.user:
            payload['username'] = "user-" + trans.security.encode_id( trans.user.id )
            payload['email'] = trans.user.email
            if trans.user.username:
                payload['display_name'] = trans.user.username
            else:
                payload['display_name'] = trans.user.email.split( "@" )[0]
        else:
            encoded = trans.security.encode_id( trans.galaxy_session.id )
            payload['username'] = "anon-" + encoded
            payload['display_name'] = "Anonymous Galaxy User"
        data, digest = encode_data( trans.app.config.biostar_key, payload )
        return trans.response.send_redirect( url_for( trans.app.config.biostar_url, data=data, digest=digest, name=trans.app.config.biostar_key_name, action=biostar_action ) )

    @web.expose
    def biostar_question_redirect( self, trans, payload=None ):
        """
        Generate a redirect to a Biostar site using external authentication to
        pass Galaxy user information and information about a specific tool.
        """
        payload = payload or {}
        return self.biostar_redirect( trans, payload=payload, biostar_action='new' )

    @web.expose
    def biostar_tool_question_redirect( self, trans, tool_id=None ):
        """
        Generate a redirect to a Biostar site using external authentication to
        pass Galaxy user information and information about a specific tool.
        """
        # tool_id is required
        if tool_id is None:
            return error( "No tool_id provided" )
        # Load the tool
        tool_version_select_field, tools, tool = \
            self.app.toolbox.get_tool_components( tool_id, tool_version=None, get_loaded_tools_by_lineage=False, set_selected=True )
        # No matching tool, unlikely
        if not tool:
            return error( "No tool found matching '%s'" % tool_id )
        # Tool specific information for payload
        payload = { 'tool_name': tool.name,
                    'tool_version': tool.version,
                    'tool_id': tool.id,
                    'tags': 'galaxy ' + tag_for_tool( tool ) }
        # Pass on to regular question method
        return self.biostar_question_redirect( trans, payload )
