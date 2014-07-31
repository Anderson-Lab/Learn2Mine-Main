# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1402424368.042912
_template_filename='templates/user/register.mako'
_template_uri='/user/register.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='ascii'
_exports = ['javascripts', 'render_registration_form']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.TemplateNamespace('__anon_0x1074dc090', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None, calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x1074dc090')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1074dc090')._populate(_import_ns, [u'render_msg'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        redirect_url = _import_ns.get('redirect_url', context.get('redirect_url', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        def render_registration_form(form_action=None):
            return render_render_registration_form(context.locals_(__M_locals),form_action)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        # SOURCE LINE 4
        if redirect_url:
            # SOURCE LINE 5
            __M_writer(u'    <script type="text/javascript">  \n        top.location.href = \'')
            # SOURCE LINE 6
            __M_writer(filters.html_escape(unicode(redirect_url )))
            __M_writer(u"';\n    </script>\n")
            pass
        # SOURCE LINE 9
        __M_writer(u'\n')
        # SOURCE LINE 12
        __M_writer(u'\n\n')
        # SOURCE LINE 14
        if not redirect_url and message:
            # SOURCE LINE 15
            __M_writer(u'    ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 17
        __M_writer(u'\n')
        # SOURCE LINE 20
        if trans.user_is_admin() or not trans.user:
            # SOURCE LINE 21
            __M_writer(u'    ')
            __M_writer(unicode(render_registration_form()))
            __M_writer(u'\n\n')
            # SOURCE LINE 23
            if trans.app.config.get( 'terms_url', None ) is not None:
                # SOURCE LINE 24
                __M_writer(u'        <br/>\n        <p>\n            <a href="')
                # SOURCE LINE 26
                __M_writer(unicode(trans.app.config.get('terms_url', None)))
                __M_writer(u'">Terms and Conditions for use of this service</a>\n        </p>\n')
                pass
            pass
        # SOURCE LINE 30
        __M_writer(u'\n')
        # SOURCE LINE 178
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1074dc090')._populate(_import_ns, [u'render_msg'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 10
        __M_writer(u'\n    ')
        # SOURCE LINE 11
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_registration_form(context,form_action=None):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x1074dc090')._populate(_import_ns, [u'render_msg'])
        username = _import_ns.get('username', context.get('username', UNDEFINED))
        redirect = _import_ns.get('redirect', context.get('redirect', UNDEFINED))
        user_type_form_definition = _import_ns.get('user_type_form_definition', context.get('user_type_form_definition', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        registration_warning_message = _import_ns.get('registration_warning_message', context.get('registration_warning_message', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        user_type_fd_id_select_field = _import_ns.get('user_type_fd_id_select_field', context.get('user_type_fd_id_select_field', UNDEFINED))
        widgets = _import_ns.get('widgets', context.get('widgets', UNDEFINED))
        subscribe_checked = _import_ns.get('subscribe_checked', context.get('subscribe_checked', UNDEFINED))
        t = _import_ns.get('t', context.get('t', UNDEFINED))
        cntrller = _import_ns.get('cntrller', context.get('cntrller', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        email = _import_ns.get('email', context.get('email', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 31
        __M_writer(u'\n\n    ')
        # SOURCE LINE 33

        if form_action is None:
            form_action = h.url_for( controller='user', action='create', cntrller=cntrller )
        from galaxy.web.form_builder import CheckboxField
        subscribe_check_box = CheckboxField( 'subscribe' )
            
        
        # SOURCE LINE 38
        __M_writer(u'\n\n<script type="text/javascript">\n\t$(document).ready(function() {\n\n\t\tfunction validateString(test_string, type) { \n\t\t\tvar mail_re = /^(([^<>()[\\]\\\\.,;:\\s@\\"]+(\\.[^<>()[\\]\\\\.,;:\\s@\\"]+)*)|(\\".+\\"))@((\\[[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\])|(([a-zA-Z\\-0-9]+\\.)+[a-zA-Z]{2,}))$/;\n\t\t\t//var mail_re_RFC822 = /^([^\\x00-\\x20\\x22\\x28\\x29\\x2c\\x2e\\x3a-\\x3c\\x3e\\x40\\x5b-\\x5d\\x7f-\\xff]+|\\x22([^\\x0d\\x22\\x5c\\x80-\\xff]|\\x5c[\\x00-\\x7f])*\\x22)(\\x2e([^\\x00-\\x20\\x22\\x28\\x29\\x2c\\x2e\\x3a-\\x3c\\x3e\\x40\\x5b-\\x5d\\x7f-\\xff]+|\\x22([^\\x0d\\x22\\x5c\\x80-\\xff]|\\x5c[\\x00-\\x7f])*\\x22))*\\x40([^\\x00-\\x20\\x22\\x28\\x29\\x2c\\x2e\\x3a-\\x3c\\x3e\\x40\\x5b-\\x5d\\x7f-\\xff]+|\\x5b([^\\x0d\\x5b-\\x5d\\x80-\\xff]|\\x5c[\\x00-\\x7f])*\\x5d)(\\x2e([^\\x00-\\x20\\x22\\x28\\x29\\x2c\\x2e\\x3a-\\x3c\\x3e\\x40\\x5b-\\x5d\\x7f-\\xff]+|\\x5b([^\\x0d\\x5b-\\x5d\\x80-\\xff]|\\x5c[\\x00-\\x7f])*\\x5d))*$/;\n\t\t\tvar username_re = /^[a-z0-9\\-]{3,255}$/;\n\t\t\tif (type === \'email\') {\n\t\t\t\treturn mail_re.test(test_string);\n\t\t\t} else if (type === \'username\'){\n\t\t\t\treturn username_re.test(test_string);\n\t\t\t}\n\t\t} \n\n\t\tfunction renderError(message) {\n\t\tif ($(".errormessage").length === 1) {\n\t\t\t$(".errormessage").html(message)\n\t\t} else {\n\t\t\tvar div = document.createElement("div");\n\t\t\tdiv.className = "errormessage"\n\t\t\tdiv.innerHTML = message;\n\t\t\tdocument.body.insertBefore(div, document.body.firstChild);\n\t\t\t}\n\t\t}\n\n\t\t$(\'#registration\').bind(\'submit\', function(e) {\n\t\t\t$(\'#send\').attr(\'disabled\', \'disabled\');\n            \n            // we need this value to detect submitting at backend\n\t\t\tvar hidden_input = \'<input type="hidden" id="create_user_button" name="create_user_button" value="Submit"/>\';\n\t\t\t$("#email_input").before(hidden_input);\n\n\t\t\tvar error_text_email= \'Please enter your valid email address\';\n\t\t\tvar error_text_email_long= \'Email cannot be more than 255 characters in length\';\n\t\t\tvar error_text_username_characters = \'Public name must contain only lowercase letters, numbers and "-". It also has to be shorter than 255 characters but longer than 3.\';\n\t\t\tvar error_text_password_short = \'Please use a password of at least 6 characters\';\n\t\t\tvar error_text_password_match = "Passwords don\'t match";\n\n\t\t    var validForm = true;\n\t\t    \n\t\t    var email = $(\'#email_input\').val();\n\t\t    var name = $(\'#name_input\').val()\n\t\t    if (email.length > 255){ renderError(error_text_email_long); validForm = false;}\n\t\t    else if (!validateString(email,"email")){ renderError(error_text_email); validForm = false;}\n\t\t    else if (!($(\'#password_input\').val() === $(\'#password_check_input\').val())){ renderError(error_text_password_match); validForm = false;}\n\t\t    else if ($(\'#password_input\').val().length < 6 ){ renderError(error_text_password_short); validForm = false;}\n\t\t    else if (name && !(validateString(name,"username"))){ renderError(error_text_username_characters); validForm = false;}\n\n\t   \t\tif (!validForm) { \n\t\t        e.preventDefault();\n\t\t        // reactivate the button if the form wasn\'t submitted\n\t\t        $(\'#send\').removeAttr(\'disabled\');\n\t\t        }\n\t\t\t});\n\t});\n\n</script>\n    <div class="toolForm">\n        <form name="registration" id="registration" action="')
        # SOURCE LINE 98
        __M_writer(unicode(form_action))
        __M_writer(u'" method="post" >\n            <div class="toolFormTitle">Create account</div>\n            <div class="form-row">\n                <label>Email address:</label>\n                <input id="email_input" type="text" name="email" value="')
        # SOURCE LINE 102
        __M_writer(filters.html_escape(unicode(email )))
        __M_writer(u'" size="40"/>\n                <input type="hidden" name="redirect" value="')
        # SOURCE LINE 103
        __M_writer(filters.html_escape(unicode(redirect )))
        __M_writer(u'" size="40"/>\n            </div>\n            <div class="form-row">\n                <label>Password:</label>\n                <input id="password_input" type="password" name="password" value="" size="40"/>\n            </div>\n            <div class="form-row">\n                <label>Confirm password:</label>\n                <input id="password_check_input" type="password" name="confirm" value="" size="40"/>\n            </div>\n            <div class="form-row">\n                <label>Public name:</label>\n                <input id="name_input" type="text" name="username" size="40" value="')
        # SOURCE LINE 115
        __M_writer(filters.html_escape(unicode(username )))
        __M_writer(u'"/>\n')
        # SOURCE LINE 116
        if t.webapp.name == 'galaxy':
            # SOURCE LINE 117
            __M_writer(u'                    <div class="toolParamHelp" style="clear: both;">\n                        Your public name is an identifier that will be used to generate addresses for information\n                        you share publicly. Public names must be at least four characters in length and contain only lower-case\n                        letters, numbers, and the \'-\' character.\n                    </div>\n')
            # SOURCE LINE 122
        else:
            # SOURCE LINE 123
            __M_writer(u'                    <div class="toolParamHelp" style="clear: both;">\n                        Your public name provides a means of identifying you publicly within this tool shed. Public\n                        names must be at least four characters in length and contain only lower-case letters, numbers,\n                        and the \'-\' character.  You cannot change your public name after you have created a repository\n                        in this tool shed.\n                    </div>\n')
            pass
        # SOURCE LINE 130
        __M_writer(u'            </div>\n')
        # SOURCE LINE 131
        if trans.app.config.smtp_server:
            # SOURCE LINE 132
            __M_writer(u'                <div class="form-row">\n                    <label>Subscribe to mailing list:</label>\n')
            # SOURCE LINE 134
            if subscribe_checked:
                # SOURCE LINE 135
                __M_writer(u'                        ')
                subscribe_check_box.checked = True 
                
                __M_writer(u'\n')
                pass
            # SOURCE LINE 137
            __M_writer(u'                    ')
            __M_writer(unicode(subscribe_check_box.get_html()))
            __M_writer(u'\n                    <p>See <a href="http://galaxyproject.org/wiki/Mailing%20Lists" target="_blank">\n                    all Galaxy project mailing lists</a>.</p>\n                </div>\n')
            pass
        # SOURCE LINE 142
        if user_type_fd_id_select_field and len( user_type_fd_id_select_field.options ) > 1:
            # SOURCE LINE 143
            __M_writer(u'                <div class="form-row">\n                    <label>User type</label>\n                    ')
            # SOURCE LINE 145
            __M_writer(unicode(user_type_fd_id_select_field.get_html()))
            __M_writer(u'\n                </div>\n')
            pass
        # SOURCE LINE 148
        if user_type_form_definition:
            # SOURCE LINE 149
            for field in widgets:
                # SOURCE LINE 150
                __M_writer(u'                    <div class="form-row">\n                        <label>')
                # SOURCE LINE 151
                __M_writer(unicode(field['label']))
                __M_writer(u'</label>\n                        ')
                # SOURCE LINE 152
                __M_writer(unicode(field['widget'].get_html()))
                __M_writer(u'\n                        <div class="toolParamHelp" style="clear: both;">\n                            ')
                # SOURCE LINE 154
                __M_writer(unicode(field['helptext']))
                __M_writer(u'\n                        </div>\n                        <div style="clear: both"></div>\n                    </div>\n')
                pass
            # SOURCE LINE 159
            if not user_type_fd_id_select_field:
                # SOURCE LINE 160
                __M_writer(u'                    <input type="hidden" name="user_type_fd_id" value="')
                __M_writer(unicode(trans.security.encode_id( user_type_form_definition.id )))
                __M_writer(u'"/>\n')
                pass
            pass
        # SOURCE LINE 163
        __M_writer(u'            <div id="for_bears">\n            If you see this, please leave following field blank. \n            <input type="text" name="bear_field" size="1" value=""/>\n            </div>\n            <div class="form-row">\n                <input type="submit" id="send" name="create_user_button" value="Submit"/>\n            </div>\n        </form>\n')
        # SOURCE LINE 171
        if registration_warning_message:
            # SOURCE LINE 172
            __M_writer(u'        <div class="alert alert-danger" style="margin: 30px 12px 12px 12px;">\n            ')
            # SOURCE LINE 173
            __M_writer(unicode(registration_warning_message))
            __M_writer(u'           \n        </div>\n')
            pass
        # SOURCE LINE 176
        __M_writer(u'    </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


