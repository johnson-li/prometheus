import os

import cloudstorage
from base import restful_request, file_request
from flask import Blueprint

__author__ = 'johnson'

static_api = Blueprint('static', __name__)
read_retry_parameter = cloudstorage.RetryParams(initial_delay=0.2,
                                                max_delay=5.0,
                                                backoff_factor=2,
                                                max_retry_period=15)
bucket_name = os.environ.get('BUCKET_NAME', 'prometheus-1151.appspot.com')


@static_api.route('/static/upload', methods=['POST'])
@restful_request
def upload(static_files):
    """ Upload file to store in Google Cloud Storage
    :param static_files: file to be stored
    :return: stored file name
    """
    files = []
    for static_file in static_files:
        file_name = '/' + bucket_name + '/' + static_file.filename
        content_type = static_file.headers.get('Content-Type', None)
        gcs_file = cloudstorage.open(file_name, 'w', content_type=content_type)
        gcs_file.write(static_file.read())
        gcs_file.close()
        files.append(static_file.filename)
    return {'static_files': files}


@static_api.route('/static/download', methods=['GET'])
@file_request
def download(token):
    """ Download file from Google Cloud Storage by file name
    :param token: file name
    :return:
    """
    file_name = '/' + bucket_name + '/' + token
    return {
        'data': generator(file_name),
        'name': token
    }


def generator(file_name):
    gcs_file = cloudstorage.open(file_name)
    data = gcs_file.read(1 << 20)
    while data:
        yield data
        data = gcs_file.read(1 << 20)
    gcs_file.close()
