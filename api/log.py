import time

from base import restful_request
from entity.data import JsonData, ApiRequestData
from flask import Blueprint

__author__ = 'johnson'

log_api = Blueprint('log', __name__)


@log_api.route('/log/universal', methods=['POST'])
@restful_request
def universal_log(json):
    json_data = JsonData(json=json)
    json_data.put()
    return json_data


@log_api.route('/log/api_request', methods=['POST'])
@restful_request
def request_log(host_name, target_url, http2_transfer_time,
                https_transfer_time, trace_route="", time_stamp=int(time.time())):
    if not isinstance(http2_transfer_time, (list, tuple)):
        http2_transfer_time = [http2_transfer_time]
    if not isinstance(https_transfer_time, (list, tuple)):
        https_transfer_time = [https_transfer_time]
    api_request_data = ApiRequestData(hostName=host_name, targetUrl=target_url, traceRoute=trace_route,
                                      http2TransferTime=http2_transfer_time, httpsTransferTime=https_transfer_time,
                                      timeStamp=time_stamp)
    api_request_data.put()
    return api_request_data


@log_api.route('/log/all', methods=['GET'])
@restful_request
def get_all():
    return ApiRequestData.query().fetch()


@log_api.route('/log/all_by_page', methods=['GET'])
@restful_request
def get_all_by_page(page_size=20, index=0):
    page_size = int(page_size)
    index = int(index)
    return ApiRequestData.query().fetch(page_size, offset=page_size * index)
