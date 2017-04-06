django-debug-toolbar-requests
=============================
Adds requests debuging information

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

