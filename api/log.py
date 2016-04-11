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
def ping_log(host_name, target_url, http2_transfer_time, https_transfer_time, trace_route):
    api_request_data = ApiRequestData(hostName=host_name, targetUrl=target_url, traceRoute=trace_route,
                                      http2TransferTime=http2_transfer_time, httpsTransferTime=https_transfer_time)
    api_request_data.put()
    return api_request_data
