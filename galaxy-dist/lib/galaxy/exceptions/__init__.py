"""
Custom exceptions for Galaxy
"""

from galaxy import eggs
eggs.require( "Paste" )

from paste import httpexceptions
from ..exceptions import error_codes


class MessageException( Exception ):
    """
    Exception to make throwing errors from deep in controllers easier.
    """
    # status code to be set when used with API.
    status_code = 400
    # Error code information embedded into API json responses.
    err_code = error_codes.UNKNOWN

    def __init__( self, err_msg=None, type="info", **extra_error_info ):
        self.err_msg = err_msg or self.err_code.default_error_message
        self.type = type
        self.extra_error_info = extra_error_info

    def __str__( self ):
        return self.err_msg


class ItemDeletionException( MessageException ):
    pass


class ItemAccessibilityException( MessageException ):
    status_code = 403
    err_code = error_codes.USER_CANNOT_ACCESS_ITEM


class ItemOwnershipException( MessageException ):
    status_code = 403
    err_code = error_codes.USER_DOES_NOT_OWN_ITEM


class DuplicatedSlugException( MessageException ):
    status_code = 400
    err_code = error_codes.USER_SLUG_DUPLICATE


class ObjectAttributeInvalidException( MessageException ):
    status_code = 400
    err_code = error_codes.USER_OBJECT_ATTRIBUTE_INVALID


class ObjectAttributeMissingException( MessageException ):
    status_code = 400
    err_code = error_codes.USER_OBJECT_ATTRIBUTE_MISSING


class ActionInputError( MessageException ):
    def __init__( self, err_msg, type="error" ):
        super( ActionInputError, self ).__init__( err_msg, type )


class ObjectNotFound( MessageException ):
    """ Accessed object was not found """
    status_code = 404
    err_code = error_codes.USER_OBJECT_NOT_FOUND


class ObjectInvalid( Exception ):
    """ Accessed object store ID is invalid """
    pass
