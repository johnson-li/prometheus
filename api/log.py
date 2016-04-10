from flask import Blueprint
from entity.data import JsonData, ApiRequestData
from base import restful_request

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
def ping_log(host_name, target_url, transfer_times, trace_route):
    api_request_data = ApiRequestData(hostName=host_name, targetUrl=target_url, traceRoute=trace_route,
                                      transferTimes=transfer_times)
    api_request_data.put()
    return api_request_data
