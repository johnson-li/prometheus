import functools
import json
import logging
import sys
import traceback

from bson import ObjectId
from pymongo.cursor import Cursor

import response_code
from flask import request, jsonify, stream_with_context
from flask.wrappers import Response
from util import codec

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


def serialise(data):
    if data is None:
        return data
    elif isinstance(data, Response):
        return data
    elif isinstance(data, (str, unicode)):
        return data
    elif isinstance(data, (int, long, float, bool)):
        return str(data)
    # elif isinstance(data, ndb.Model):
    #     return data.to_dict()
    elif isinstance(data, dict):
        return {codec.decode_mongo_key(serialise(key)): serialise(val) for key, val in data.iteritems()}
    elif isinstance(data, list):
        return [serialise(i) for i in data]
    elif isinstance(data, Cursor):
        return serialise([d for d in data.limit(0)])
    elif isinstance(data, ObjectId):
        return str(data)
    else:
        raise Exception('Unknown return type: ' + str(type(data)))


def restful_request(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        resp = {'rc': response_code.SUCCESS, 'content': ''}
        try:
            data = handle_restful_request(func, *args, **kwargs)
            resp['content'] = serialise(data)
        except Exception as e:
            resp['rc'] = response_code.FAIL
            resp['content'] = type(e).__name__ + ' ' + e.message
            traceback.print_exc(file=sys.stdout)
            logging.error(e.message)
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
