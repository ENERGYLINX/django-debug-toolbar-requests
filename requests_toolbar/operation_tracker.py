import json
import requests
import functools
import time
import inspect

__all__ = ['results', 'install_trackers', 'uninstall_trackers', 'reset']

_original_methods = {
    'request': requests.request,
    'get': requests.get,
    'post': requests.post,
    'patch': requests.patch,
    'put': requests.put,
}

results = []


def _get_stacktrace():
    try:
        return inspect.stack()[2:]
    except IndexError:
        return [(
            "",
            0,
            "Error retrieving stack",
            "Could not retrieve stack. IndexError exception occured in inspect.stack(). "
            "This error might occur when templates are on the stack.",
        )]


def parse_content(response):
    try:

        content = json.dumps(response.json(), indent=4, sort_keys=True)
        is_json = True
    except Exception:
        is_json = False
        content = response.content

    return is_json, content


@functools.wraps(_original_methods['request'])
def _request(method, url, **kwargs):
    start_time = time.time()
    response = _original_methods['request'](method, url, **kwargs)
    total_time = (time.time() - start_time) * 1000

    is_json, content = parse_content(response)
    results.append({
        'method': method.upper(),
        'url': url,
        'time': total_time,
        'stacktrace': _get_stacktrace(),
        'kwargs': kwargs,
        'status_code': response.status_code,
        'content': content,
        'is_json': is_json,
    })

    return response


@functools.wraps(_original_methods['get'])
def _get(url, **kwargs):
    start_time = time.time()
    response = _original_methods['get'](url, **kwargs)
    total_time = (time.time() - start_time) * 1000

    is_json, content = parse_content(response)
    results.append({
        'method': 'GET',
        'url': url,
        'time': total_time,
        'stacktrace': _get_stacktrace(),
        'kwargs': kwargs,
        'status_code': response.status_code,
        'content': content,
        'is_json': is_json,
    })

    return response


@functools.wraps(_original_methods['post'])
def _post(url, **kwargs):
    start_time = time.time()
    response = _original_methods['post'](url, **kwargs)
    total_time = (time.time() - start_time) * 1000

    is_json, content = parse_content(response)
    results.append({
        'method': 'POST',
        'url': url,
        'time': total_time,
        'stacktrace': _get_stacktrace(),
        'kwargs': kwargs,
        'status_code': response.status_code,
        'content': content,
        'is_json': is_json,
    })

    return response


@functools.wraps(_original_methods['patch'])
def _patch(url, **kwargs):
    start_time = time.time()
    response = _original_methods['patch'](url, **kwargs)
    total_time = (time.time() - start_time) * 1000

    is_json, content = parse_content(response)
    results.append({
        'method': 'PATCH',
        'url': url,
        'time': total_time,
        'stacktrace': _get_stacktrace(),
        'kwargs': kwargs,
        'status_code': response.status_code,
        'content': content,
        'is_json': is_json,
    })

    return response


@functools.wraps(_original_methods['put'])
def _put(url, **kwargs):
    start_time = time.time()
    response = _original_methods['put'](url, **kwargs)
    total_time = (time.time() - start_time) * 1000

    is_json, content = parse_content(response)
    results.append({
        'method': 'PUT',
        'url': url,
        'time': total_time,
        'stacktrace': _get_stacktrace(),
        'kwargs': kwargs,
        'status_code': response.status_code,
        'content': content,
        'is_json': is_json,
    })

    return response


def install_trackers():
    if requests.request != _request:
        requests.request = _request
    if requests.get != _get:
        requests.get = _get
    if requests.post != _post:
        requests.post = _post


def uninstall_trackers():
    if requests.request == _request:
        requests.request = _original_methods['request']
    if requests.get == _get:
        requests.get = _original_methods['get']
    if requests.post == _post:
        requests.post = _original_methods['post']
    if requests.patch == _patch:
        requests.patch = _original_methods['patch']
    if requests.put == _put:
        requests.put = _original_methods['put']


def reset():
    global results
    results = []
