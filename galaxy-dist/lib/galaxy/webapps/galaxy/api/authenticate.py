"""
API key retrieval through BaseAuth
"""

from galaxy import util, web
from pprint import pprint
from galaxy.web.base.controller import BaseAPIController
from base64 import b64decode, b64encode
from urllib import quote, unquote
from galaxy.exceptions import ObjectNotFound
from paste.httpexceptions import HTTPBadRequest

import logging
log = logging.getLogger( __name__ )

class AuthenticationController( BaseAPIController ):

    @web.expose_api_anonymous
    def get_api_key( self, trans, **kwd ):
        """
        def get_api_key( self, trans, **kwd )
        * GET /api/authenticate/baseauth
          returns an API key for authenticated user based on BaseAuth headers

        :returns: api_key in json format
        :rtype:   dict

        :raises: ObjectNotFound, HTTPBadRequest
        """
        email, password = self._decode_baseauth( trans.environ.get( 'HTTP_AUTHORIZATION' ) )

        user = trans.sa_session.query( trans.app.model.User ).filter( trans.app.model.User.table.c.email == email ).all()

        if ( len( user ) is not 1 ):
            # DB is inconsistent and we have more users with same email
            raise ObjectNotFound
        else:
            user = user[0]
            is_valid_user = user.check_password( password )

        if ( is_valid_user ):
            user_id = user.id
            api_key_row = trans.sa_session.query( trans.app.model.APIKeys ).filter( trans.app.model.APIKeys.table.c.user_id == user_id ).first()
        else:
            trans.response.status = 500
            return "invalid password" 

        return dict( api_key= api_key_row.key )

    def _decode_baseauth( self, encoded_str ):
        """
        Decode an encrypted HTTP basic authentication string. Returns a tuple of
        the form (email, password), and raises a HTTPBadRequest exception if
        nothing could be decoded.

        :param  encoded_str: BaseAuth string encoded base64
        :type   encoded_str: string

        :returns: email of the user
        :rtype:   string
        :returns: password of the user
        :rtype:   string

        :raises: HTTPBadRequest
        """
        split = encoded_str.strip().split( ' ' )

        # If split is only one element, try to decode the email and password
        # directly.
        if len( split ) == 1:
            try:
                email, password = b64decode( split[ 0 ] ).split( ':' )
            except:
                raise HTTPBadRequest

        # If there are only two elements, check the first and ensure it says
        # 'basic' so that we know we're about to decode the right thing. If not,
        # bail out.
        elif len( split ) == 2:
            if split[ 0 ].strip().lower() == 'basic':
                try:
                    email, password = b64decode( split[ 1 ] ).split( ':' )
                except:
                    raise HTTPBadRequest
            else:
                raise HTTPBadRequest

        # If there are more than 2 elements, something crazy must be happening.
        # Bail.
        else:
            raise HTTPBadRequest

        return unquote( email ), unquote( password )
