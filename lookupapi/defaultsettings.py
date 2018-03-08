"""
Default settings values for the :py:mod:`lookupapi` application.

"""
# Variables whose names are in upper case and do not start with an underscore from this module are
# used as default settings for the lookupapi application. See LookupAPIConfig in .apps for
# how this is achieved. This is a bit mucky but, at the moment, Django does not have a standard way
# to specify default values for settings.  See: https://stackoverflow.com/questions/8428556/

LOOKUP_API_ENDPOINT_HOST = 'www.lookup.cam.ac.uk'
"""
Hostname of proxied Lookup API endpoint. This is usually one of "lookup-test.csx.cam.ac.uk" or
"www.lookup.cam.ac.uk" depending on whether you want to interact with the test or production Lookup
instances.

"""

LOOKUP_API_ENDPOINT_PORT = 443
"""
Port to connect to proxied Lookup API on. Defaults to the HTTPS service port 443.

"""

LOOKUP_API_ENDPOINT_BASE = ''
"""
Base path for proxied Lookup API. If using the deployed test or production instances this should be
the empty string.

"""

LOOKUP_API_ENDPOINT_VERIFY = True
"""
Specify whether the certificate presented by the proxied Lookup API should be checked. Unless you
are extremely sure in what you are doing, set this to True.

"""

LOOKUP_API_OAUTH2_CLIENT_ID = None
"""
OAuth2 client id which the API server uses to identify itself to the OAuth2 token introspection
endpoint.

"""

LOOKUP_API_OAUTH2_CLIENT_SECRET = None
"""
OAuth2 client secret which the API server uses to identify itself to the OAuth2 token introspection
endpoint.

"""

LOOKUP_API_OAUTH2_TOKEN_URL = None
"""
URL of the OAuth2 token endpoint the API server uses to request an authorisation token to perform
OAuth2 token introspection.

"""

LOOKUP_API_OAUTH2_INTROSPECT_URL = None
"""
URL of the OAuth2 token introspection endpoint. The API server will first identify itself to the
OAuth2 token endpoint and request an access token for this endpoint.

"""

LOOKUP_API_OAUTH2_INTROSPECT_SCOPES = None
"""
List of OAuth2 scopes the API server will request for the token it will use with the token
introspection endpoint.

"""
