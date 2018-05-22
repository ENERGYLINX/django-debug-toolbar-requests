# django-debug-toolbar-requests

A Django Debug Toolbar panel for most popular http library [requests](http://docs.python-requests.org/en/master/).

# About

This is a panel for [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/stable/index.html) that displays [requests](http://docs.python-requests.org/en/master/) http queries, data headers and stack trace.

### Installation

Install django-debug-toolbar-requests

```sh
$ pip install django-debug-toolbar-requests
```

Add library into your django `settings.py`

```python
INSTALLED_APPS = (
   ...
   'requests_toolbar',
   ...
)
```

Add panel into `DEBUG_TOOLBAR_PANELS`

```python
DEBUG_TOOLBAR_PANELS = (
   ...
   'requests_toolbar.panels.RequestsDebugPanel',
   ...
)
```


## Example

Now always if you're will use [requests](http://docs.python-requests.org/en/master/) then you will see debug information in your [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/stable/index.html).


```python
requests.get('https://httpbin.org/get', headers={'X-headers': 'value of x header'})
```

## Screenshot
![Screenshot](https://raw.githubusercontent.com/ENERGYLINX/django-debug-toolbar-requests/master/screenshot.png)
