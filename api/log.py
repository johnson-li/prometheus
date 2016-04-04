from flask import Blueprint
from entity.data import JsonData
from base import restful_request

__author__ = 'johnson'

log_api = Blueprint('log', __name__)


@log_api.route('/log/universal', methods=['POST'])
@restful_request
def universal_log(json):
    json_data = JsonData(json=json)
    json_data.put()
    return json_data
