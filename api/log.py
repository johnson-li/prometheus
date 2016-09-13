import time

from base import restful_request
from entity.data import JsonData, ApiRequestData, TrafficSizeData, Http2SupportData, FullWebData, MultiConnData, \
    PoseidonData
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
def traffic_size(host_name, target_url, https_request_size, https_response_size, http2_request_size,
                 http2_response_size, https_request_size_tcp=0, https_response_size_tcp=0, http2_request_size_tcp=0,
                 http2_response_size_tcp=0, time_stamp=int(time.time() * 1000), request_times=0):
    traffic_size_data = TrafficSizeData(hostName=host_name, targetUrl=target_url, timeStamp=time_stamp,
                                        requestTimes=request_times, httpsRequestSize=https_request_size,
                                        httpsResponseSize=https_response_size, http2RequestSize=http2_request_size,
                                        http2ResponseSize=http2_response_size,
                                        httpsRequestSizeTcp=https_request_size_tcp,
                                        httpsResponseSizeTcp=https_response_size_tcp,
                                        http2RequestSizeTcp=http2_request_size_tcp,
                                        http2ResponseSizeTcp=http2_response_size_tcp)
    traffic_size_data.put()
    return traffic_size_data


@log_api.route('/log/full_web', methods=['POST'])
@restful_request
def full_web(host_name, target_url, https_request_size, https_response_size, http2_request_size,
             http2_response_size, https_request_size_tcp, https_response_size_tcp, http2_request_size_tcp,
             http2_response_size_tcp, https_transfer_time, http2_transfer_time, https_traces, http2_traces,
             time_stamp=int(time.time() * 1000)):
    full_web_data = FullWebData(hostName=host_name, targetUrl=target_url, timeStamp=time_stamp,
                                httpsRequestSize=https_request_size, httpsTraces=https_traces, http2Traces=http2_traces,
                                httpsResponseSize=https_response_size, http2RequestSize=http2_request_size,
                                http2ResponseSize=http2_response_size,
                                httpsRequestSizeTcp=https_request_size_tcp,
                                httpsResponseSizeTcp=https_response_size_tcp,
                                http2RequestSizeTcp=http2_request_size_tcp,
                                http2ResponseSizeTcp=http2_response_size_tcp, httpsTransferTime=https_transfer_time,
                                http2TransferTime=http2_transfer_time)
    full_web_data.put()
    return full_web_data


@log_api.route('/log/multi_conn', methods=['POST'])
@restful_request
def multi_conn(host_name, target_url, https_request_size, https_response_size, http2_request_size,
               http2_response_size, https_request_size_tcp, https_response_size_tcp, http2_request_size_tcp,
               http2_response_size_tcp, https_transfer_time, http2_transfer_time, https_traces, http2_traces,
               https_channel_request_size, https_channel_response_size, https_request_size_tcp_tcpdump,
               https_response_size_tcp_tcpdump, http2_request_size_tcp_tcpdump, http2_response_size_tcp_tcpdump,
               https_tcpdump_packets_drop, http2_tcpdump_packets_drop,
               time_stamp=int(time.time() * 1000)):
    multi_conn_data = MultiConnData(hostName=host_name, targetUrl=target_url, timeStamp=time_stamp,
                                    httpsRequestSize=https_request_size, httpsTraces=https_traces,
                                    http2Traces=http2_traces, httpsResponseSize=https_response_size,
                                    http2RequestSize=http2_request_size, http2ResponseSize=http2_response_size,
                                    httpsRequestSizeTcp=https_request_size_tcp,
                                    httpsResponseSizeTcp=https_response_size_tcp,
                                    http2RequestSizeTcp=http2_request_size_tcp,
                                    http2ResponseSizeTcp=http2_response_size_tcp, httpsTransferTime=https_transfer_time,
                                    http2TransferTime=http2_transfer_time,
                                    httpsChannelRequestSize=https_channel_request_size,
                                    httpsChannelResponseSize=https_channel_response_size,
                                    httpsRequestSizeTcpTcpdump=https_request_size_tcp_tcpdump,
                                    httpsResponseSizeTcpTcpdump=https_response_size_tcp_tcpdump,
                                    http2RequestSizeTcpTcpdump=http2_request_size_tcp_tcpdump,
                                    http2ResponseSizeTcpTcpdump=http2_response_size_tcp_tcpdump,
                                    httpsTcpdumpPacketsDrop=https_tcpdump_packets_drop,
                                    http2TcpdumpPacketsDrop=http2_tcpdump_packets_drop)
    multi_conn_data.put()
    return multi_conn_data


@log_api.route('/log/poseidon', methods=['POST'])
@restful_request
def poseidon(poseidon_data):
    config = poseidon_data['config']
    http1_data = poseidon_data['http1Data']
    http1_measured_data = http1_data['tcpdumpInfo']['measuredTrafficSize']
    http2_data = poseidon_data['http2Data']
    http2_measured_data = http2_data['tcpdumpInfo']['measuredTrafficSize']
    poseidon_db_data = PoseidonData(hostName=config['hostName'], targetUrl=config['targetUrl'],
                                    timeStamp=int(time.time() * 1000), ignoreOuterLink=config['ignoreOuterLink'],
                                    channelPoolSize=config['channelPoolSize'],
                                    http1Traces=http1_data['traceInfoList'],
                                    http1RequestTcpSizes=http1_data['tcpTrafficSize']['requestTcpTrafficSizeMap'],
                                    http1ResponseTcpSizes=http1_data['tcpTrafficSize']['responseTcpTrafficSizeMap'],
                                    http1RequestTcpSize=http1_data['tcpTrafficSize']['requestTcpTrafficSizeAll'],
                                    http1ResponseTcpSize=http1_data['tcpTrafficSize']['responseTcpTrafficSizeAll'],
                                    http1Time=http1_data['timeAll'],
                                    http1TcpdumpPacketsDrop=http1_data['tcpdumpInfo']['tcpdumpPacketsDrop'],
                                    http1TcpdumpRequestTcpSizeAll=http1_measured_data['requestTcpSizeAll'],
                                    http1TcpdumpResponseTcpSizeAll=http1_measured_data['responseTcpSizeAll'],
                                    http1TcpdumpRequestIpSizeAll=http1_measured_data['requestIpSizeAll'],
                                    http1TcpdumpResponseIpSizeAll=http1_measured_data['responseIpSizeAll'],
                                    http1TcpdumpRequestTcpSizes=http1_measured_data['requestTcpSizeMap'],
                                    http1TcpdumpResponseTcpSizes=http1_measured_data['responseTcpSizeMap'],
                                    http1TcpdumpRequestIpSizes=http1_measured_data['requestIpSizeMap'],
                                    http1TcpdumpResponseIpSizes=http1_measured_data['responseIpSizeMap'],
                                    http2Traces=http2_data['traceInfoList'],
                                    http2RequestTcpSizes=http2_data['tcpTrafficSize']['requestTcpTrafficSizeMap'],
                                    http2ResponseTcpSizes=http2_data['tcpTrafficSize']['responseTcpTrafficSizeMap'],
                                    http2RequestTcpSize=http2_data['tcpTrafficSize']['requestTcpTrafficSizeAll'],
                                    http2ResponseTcpSize=http2_data['tcpTrafficSize']['responseTcpTrafficSizeAll'],
                                    http2Time=http2_data['timeAll'],
                                    http2TcpdumpPacketsDrop=http2_data['tcpdumpInfo']['tcpdumpPacketsDrop'],
                                    http2TcpdumpRequestTcpSizeAll=http2_measured_data['requestTcpSizeAll'],
                                    http2TcpdumpResponseTcpSizeAll=http2_measured_data['responseTcpSizeAll'],
                                    http2TcpdumpRequestIpSizeAll=http2_measured_data['requestIpSizeAll'],
                                    http2TcpdumpResponseIpSizeAll=http2_measured_data['responseIpSizeAll'],
                                    http2TcpdumpRequestTcpSizes=http2_measured_data['requestTcpSizeMap'],
                                    http2TcpdumpResponseTcpSizes=http2_measured_data['responseTcpSizeMap'],
                                    http2TcpdumpRequestIpSizes=http2_measured_data['requestIpSizeMap'],
                                    http2TcpdumpResponseIpSizes=http2_measured_data['responseIpSizeMap'])
    poseidon_db_data.put()
    return poseidon_db_data


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


@log_api.route('/log/all', methods=['GET'])
@restful_request
def get_all():
    return ApiRequestData.query().fetch()


@log_api.route('/log/traffic_size_all', methods=['GET'])
@restful_request
def get_all_traffic_size():
    return TrafficSizeData.query().fetch()


@log_api.route('/log/http2_check_all', methods=['GET'])
@restful_request
def get_all_http2_check():
    return Http2SupportData.query().fetch()


@log_api.route('/log/full_web_all', methods=['GET'])
@restful_request
def get_all_full_web(page_size=20, index=0):
    page_size = int(page_size)
    index = int(index)
    return FullWebData.query().fetch(page_size, offset=page_size * index)


@log_api.route('/log/multi_conn_all', methods=['GET'])
@restful_request
def get_all_multi_conn(page_size=20, index=0):
    page_size = int(page_size)
    index = int(index)
    return MultiConnData.query().fetch(page_size, offset=page_size * index)
