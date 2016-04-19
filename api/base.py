import functools
import json

from google.appengine.ext import ndb

import response_code
from flask import request, jsonify, stream_with_context
from flask.wrappers import Response

__author__ = 'Johnson'


def handle_restful_request(func, *args, **kwargs):
    kwargs = kwargs.copy()
    if request.args:
        kwargs.update(request.args.to_dict())
    if request.data:
        data = json.loads(request.data)
        # escape character is only supported in the top level value field
        data = {k: (lambda x: x.replace('\\n', '\n') if isinstance(x, (str, unicode)) else x)(v) for k, v in
                data.items()}
        kwargs.update(data)
    if request.form:
        kwargs.update(request.form.to_dict())
    if request.files:
        kwargs.update({k: request.files.getlist(k) for k in request.files})
    return func(*args, **kwargs)


def _build_deco_chain(decoding_func, decoded_func, decoding_obj):
    if not hasattr(decoded_func, '_real_func'):
        decoded_func._real_func = decoded_func
    _real_func = decoded_func._real_func
    decoding_func._real_func = _real_func
    setattr(_real_func, '_decorators', getattr(_real_func, '_decorators', []) + [decoding_obj])


def restful_request(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        resp = {'rc': response_code.SUCCESS, 'content': ''}
        try:
            data = handle_restful_request(func, *args, **kwargs)
            if isinstance(data, Response):
                return data
            elif isinstance(data, dict) or isinstance(data, (str, unicode)):
                resp['content'] = data
            elif isinstance(data, (int, long, float, bool)):
                resp['content'] = str(data)
            elif isinstance(data, ndb.Model):
                resp['content'] = data.to_dict()
            else:
                raise Exception('Unknown return type: ' + str(type(data)))
        except Exception as e:
            resp['rc'] = response_code.FAIL
            resp['content'] = type(e).__name__ + ' ' + e.message
        return jsonify(resp)

    _build_deco_chain(wrapped, func, restful_request)
    return wrapped


def file_request(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        data = handle_restful_request(func, *args, **kwargs)
        response = Response(stream_with_context(data['data']))
        response.headers['Content-Type'] = 'application/octet-stream'
        response.headers['content-disposition'] = 'attachment; filename="' + data['name'] + '"'
        return response

    return wrapped

