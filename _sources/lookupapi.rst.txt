The lookupapi Application
=========================

The :py:mod:`lookupapi` application provides a REST-y API which proxies the
University of Cambridge `Lookup API
<https://help.uis.cam.ac.uk/email-telephony-and-collaboration/map-collaborative-services/lookup/ws>`_.
Currently only the anonymous API is proxied but access to the API is protected
by requiring an OAuth2 token with the appropriate scopes
(:py:attr:`lookupapi.views.REQUIRED_SCOPES`). The OAuth2 token is verified by
means of a third-party OAuth2 `token introspection
<https://tools.ietf.org/html/rfc7662>`_ endpoint.

Installation
````````````

Add the lookupapi application to your ``INSTALLED_APPS`` configuration as usual.
Make sure to configure the various ``LOOKUP_API_OAUTH2_...`` settings.

Default settings
````````````````

.. automodule:: lookupapi.defaultsettings
    :members:

Views and serializers
`````````````````````

.. automodule:: lookupapi.views
    :members:

.. automodule:: lookupapi.serializers
    :members:

Authentication and permissions
``````````````````````````````

.. automodule:: lookupapi.authentication
    :members:

.. automodule:: lookupapi.permissions
    :members:

Extensions to drf-yasg
``````````````````````

.. automodule:: lookupapi.inspectors
    :members:

Accessing the Lookup API
````````````````````````

.. automodule:: lookupapi.ibis
    :members:

Default URL routing
```````````````````

.. automodule:: lookupapi.urls
    :members:

Application configuration
`````````````````````````

.. automodule:: lookupapi.apps
    :members:

.. automodule:: lookupapi.systemchecks
    :members:
