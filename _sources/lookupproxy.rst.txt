The lookupproxy project
=======================

The ``lookupproxy`` project contains top-level configuration and URL routes for
the entire web application.

Extensions to drf-yasg
----------------------

This project overrides the ``drf-yasg/swagger-ui.html`` template provided by
`drf-yasg <https://drf-yasg.readthedocs.io/>`_. The default template does not
provided the degree of customisation needed for this project. Most notably, the
OAuth2 redirect URL could not be customised. We ship a lightly modified version
of the template for our needs along with some custom initialisation JavaScript
as a static file. We also include the ``oauth2-redirect.html`` file which ships
with the Swagger UI so that the OAuth2 flow works.

Settings
--------

The ``lookupproxy`` project ships a number of settings files.

.. _settings:

Generic settings
````````````````

.. automodule:: lookupproxy.settings
    :members:

.. _settings_testsuite:

Test-suite specific settings
````````````````````````````

.. automodule:: lookupproxy.settings.tox
    :members:

.. _settings_developer:

Developer specific settings
```````````````````````````

.. automodule:: lookupproxy.settings.developer
    :members:

Custom test suite runner
------------------------

The :any:`test suite settings <settings_testsuite>` overrides the
``TEST_RUNNER`` setting to point to
:py:class:`~lookupproxy.test.runner.BufferedTextTestRunner`. This runner captures
output to stdout and stderr and only reports the output if a test fails. This
helps make our tests a little less noisy.

.. autoclass:: lookupproxy.test.runner.BufferedDiscoverRunner

.. autoclass:: lookupproxy.test.runner.BufferedTextTestRunner
