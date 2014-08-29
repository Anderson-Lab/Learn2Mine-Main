#!/usr/bin/env python

"""
Access a Galaxy instance and get data for histories.
"""
import os
import sys
import pprint

import setup
import common

# the REST URL for the user resource
RESOURCE_URL = '/api/histories'

# ----------------------------------------------------------------------------- functions
def get_histories():
    """
    Return a list of dictionaries that describe the current user's histories.
    """
    # notice how similar this is to users.get_users - in fact only the name and doc has changed
    apikey = setup.get_apikey()
    full_url = setup.get_base_url() + RESOURCE_URL
    return common.get( apikey, full_url )


# ----------------------------------------------------------------------------- main
if __name__ == '__main__':
    # get the resource data using the function we defined above
    returned = get_histories()
    # pretty print the list of dictionaries that Galaxy sent us in response
    pprint.pprint( returned, indent=2 )
