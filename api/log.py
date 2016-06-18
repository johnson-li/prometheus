import time

from base import restful_request
from entity.data import JsonData, ApiRequestData, TrafficSizeData, Http2SupportData
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
def request_log(host_name, target_url, http2_transfer_time, https_transfer_time, https_request_size, http2_request_size,
                https_response_size, http2_response_size, trace_route="", time_stamp=int(time.time() * 1000),
                request_times=0):
    if not isinstance(http2_transfer_time, (list, tuple)):
        http2_transfer_time = [http2_transfer_time]
    if not isinstance(https_transfer_time, (list, tuple)):
        https_transfer_time = [https_transfer_time]
    api_request_data = ApiRequestData(hostName=host_name, targetUrl=target_url, traceRoute=trace_route,
                                      http2TransferTime=http2_transfer_time, httpsTransferTime=https_transfer_time,
                                      timeStamp=time_stamp, requestTimes=request_times,
                                      httpsRequestSize=https_request_size, httpsResponseSize=https_response_size,
                                      http2RequestSize=http2_request_size, http2ResponseSize=http2_response_size)
    api_request_data.put()
    return api_request_data


@log_api.route('/log/traffic_size', methods=['POST'])
@restful_request
def traffic_size(host_name, target_url, https_request_size, http2_request_size,
                 http2_response_size, time_stamp=int(time.time() * 1000), request_times=0):
    traffic_size_data = TrafficSizeData(host_name, target_url, time_stamp, request_times, https_request_size,
                                        https_response_size, http2_request_size, http2_response_size)
    traffic_size_data.put()
    return traffic_size_data


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


@log_api.route('/log/http2_check', methods=['POST'])
@restful_request
def http2_check(host, source, support, errors=[], time_stamp=int(time.time() * 1000)):
    data = Http2SupportData(host=host, source=source, timeStamp=time_stamp, support=support, errors=errors)
    data.put()
    return data
