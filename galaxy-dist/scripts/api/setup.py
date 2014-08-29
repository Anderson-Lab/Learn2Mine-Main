#!/usr/bin/env python

"""
Sets an environment variable that stores a user's Galaxy API key until they
log out of the current bash window.
"""
import os
import sys

# ----------------------------------------------------------------------------- functions
def get_base_url():
    """
    Retrieve the base URL Galaxy is being served at.
    """
    url = os.environ.get( 'GALAXY_BASE_URL', None )
    if not url:
        raise Exception( 'No base URL found' )
    return url

def get_apikey():
    """
    Retrieve the API key.
    """
    key = os.environ.get( 'GALAXY_API_KEY', None )
    if not key:
        raise Exception( 'No API key found' )
    return key


# ----------------------------------------------------------------------------- main
if __name__ == '__main__':
    print 'base url:', get_base_url()
    print 'api key:', get_apikey()
