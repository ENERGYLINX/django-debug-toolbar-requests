django-debug-toolbar-requests
=============================
Adds requests debuging information


Install
-------
::

    pip install -e git+git@github.com:ENERGYLINX/django-debug-toolbar-requests.git#egg=django-debug-toolbar-requests


Setup
-----
Add the following lines to your ``settings.py``::

   INSTALLED_APPS = (
       ...
       'requests_toolbar',
       ...
   )

   DEBUG_TOOLBAR_PANELS = (
       ...
       'requests_toolbar.panels.RequestsDebugPanel',
       ...
   )

