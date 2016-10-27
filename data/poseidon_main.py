import json
import logging

import numpy


def divide(a, b):
    if float(b) != 0:
        return float(a) / float(b)
    elif float(a) == 0:
        return 0
    else:
        raise ZeroDivisionError()


def main():
    data = load_data()
    data = filter(lambda x: x['ignoreOuterLink'], data)
    # data = filter(lambda x: x['targetUrl'] not in (
    #     'https://www.youtube.com/', 'https://www.wordpress.org/', 'https://www.facebook.com/share.php',
    #     'https://www.facebook.com/sharer.php', 'https://www.facebook.com', 'https://www.facebook.com/Onecom'), data)
    data = filter(lambda x: 'facebook' not in x['targetUrl'], data)
    data = filter(lambda x: x['http2TcpdumpPacketsDrop'] == 0 and x['http1TcpdumpPacketsDrop'] == 0, data)
    logging.error([i['hostName'] for i in
                   filter(lambda x: float(x['http1TcpdumpResponseTcpSizeAll']) < float(x['http1ResponseTcpSize']),
                          data)])
    logging.error([i['hostName'] for i in
                   filter(lambda x: float(x['http2TcpdumpResponseTcpSizeAll']) < float(x['http2ResponseTcpSize']),
                          data)])
    data = filter(lambda x: float(x['http1TcpdumpResponseTcpSizeAll']) >= float(x['http1ResponseTcpSize']), data)
    data = filter(lambda x: float(x['http1TcpdumpRequestTcpSizeAll']) >= float(x['http1RequestTcpSize']), data)
    data = filter(lambda x: float(x['http2TcpdumpResponseTcpSizeAll']) >= float(x['http2ResponseTcpSize']), data)
    data = filter(lambda x: float(x['http2TcpdumpRequestTcpSizeAll']) >= float(x['http2RequestTcpSize']), data)

    target_urls = set([d['targetUrl'] for d in data])
    target_urls = sorted(list(target_urls))
    print(target_urls)

    http1_request_ratios_5 = []
    http1_response_ratios_5 = []
    http2_request_ratios_5 = []
    http2_response_ratios_5 = []
    http1_request_ratios_50 = []
    http1_response_ratios_50 = []
    http2_request_ratios_50 = []
    http2_response_ratios_50 = []
    http1_request_ratios_95 = []
    http1_response_ratios_95 = []
    http2_request_ratios_95 = []
    http2_response_ratios_95 = []
    for url in target_urls:
        sub_data = filter(lambda x: x['targetUrl'] == url, data)
        print(set([len(x['http1Traces']) for x in sub_data]))
        print('{}: {}'.format(url, len(sub_data)))

        print([x['http1ResponseTcpSize'] for x in sub_data])
        print([x['http1TcpdumpResponseTcpSizeAll'] for x in sub_data])

        http1_request_ratios = [divide(x['http1TcpdumpRequestTcpSizeAll'], x['http1RequestTcpSize']) for x in sub_data]
        http1_response_ratios = [divide(x['http1TcpdumpResponseTcpSizeAll'], x['http1ResponseTcpSize']) for x in
                                 sub_data]
        http2_request_ratios = [divide(x['http2TcpdumpRequestTcpSizeAll'], x['http2RequestTcpSize']) for x in sub_data]
        http2_response_ratios = [divide(x['http2TcpdumpResponseTcpSizeAll'], x['http2ResponseTcpSize']) for x in
                                 sub_data]
        http1_request_data_ratios = [divide(x['http1TcpdumpRequestIpSizeAll'], x['http1TcpdumpRequestTcpSizeAll']) for x
                                     in
                                     sub_data]
        http1_response_data_ratios = [divide(x['http1TcpdumpResponseIpSizeAll'], x['http1TcpdumpResponseTcpSizeAll'])
                                      for x in
                                      sub_data]
        http2_request_data_ratios = [divide(x['http2TcpdumpRequestIpSizeAll'], x['http2TcpdumpRequestTcpSizeAll']) for x
                                     in
                                     sub_data]
        http2_response_data_ratios = [divide(x['http2TcpdumpResponseIpSizeAll'], x['http2TcpdumpResponseTcpSizeAll'])
                                      for x in
                                      sub_data]
        http1_request_ip = [x['http1TcpdumpRequestIpSizeAll'] for x in sub_data]
        http2_request_ip = [x['http2TcpdumpRequestIpSizeAll'] for x in sub_data]
        http1_response_ip = [x['http1TcpdumpResponseIpSizeAll'] for x in sub_data]
        http2_response_ip = [x['http2TcpdumpResponseIpSizeAll'] for x in sub_data]
        http1_request_tcp = [x['http1TcpdumpRequestTcpSizeAll'] for x in sub_data]
        http2_request_tcp = [x['http2TcpdumpRequestTcpSizeAll'] for x in sub_data]
        http1_response_tcp = [x['http1TcpdumpResponseTcpSizeAll'] for x in sub_data]
        http2_response_tcp = [x['http2TcpdumpResponseTcpSizeAll'] for x in sub_data]
        http1_request_tcp_size = [x['http1RequestTcpSize'] for x in sub_data]
        http2_request_tcp_size = [x['http2RequestTcpSize'] for x in sub_data]
        http1_response_tcp_size = [x['http1ResponseTcpSize'] for x in sub_data]
        http2_response_tcp_size = [x['http2ResponseTcpSize'] for x in sub_data]

        print(http1_request_ratios)
        print(numpy.percentile(http1_request_ratios, 5), numpy.percentile(http1_request_ratios, 50))
        http1_request_ratios_5.append(numpy.percentile(http1_request_ratios, 5))
        http1_request_ratios_50.append(numpy.percentile(http1_request_ratios, 50))
        http1_request_ratios_95.append(numpy.percentile(http1_request_ratios, 95))
        http2_request_ratios_5.append(numpy.percentile(http2_request_ratios, 5))
        http2_request_ratios_50.append(numpy.percentile(http2_request_ratios, 50))
        http2_request_ratios_95.append(numpy.percentile(http2_request_ratios, 95))
        http1_response_ratios_5.append(numpy.percentile(http1_response_ratios, 5))
        http1_response_ratios_50.append(numpy.percentile(http1_response_ratios, 50))
        http1_response_ratios_95.append(numpy.percentile(http1_response_ratios, 95))
        http2_response_ratios_5.append(numpy.percentile(http2_response_ratios, 5))
        http2_response_ratios_50.append(numpy.percentile(http2_response_ratios, 50))
        http2_response_ratios_95.append(numpy.percentile(http2_response_ratios, 95))

        print('http1_request_ratios = {};'.format(http1_request_ratios))
        print('http1_response_ratios = {};'.format(http1_response_ratios))
        print('http2_request_ratios = {};'.format(http2_request_ratios))
        print('http2_response_ratios = {};'.format(http2_response_ratios))
        print('http1_request_data_ratios = {};'.format(http1_request_data_ratios))
        print('http1_response_data_ratios = {};'.format(http1_response_data_ratios))
        print('http2_request_data_ratios = {};'.format(http2_request_data_ratios))
        print('http2_response_data_ratios = {};'.format(http2_response_data_ratios))
        print('http1_request_ip = {};'.format(http1_request_ip))
        print('http2_request_ip = {};'.format(http2_request_ip))
        print('http1_response_ip = {};'.format(http1_response_ip))
        print('http2_response_ip = {};'.format(http2_response_ip))
        print('http1_request_tcp = {};'.format(http1_request_tcp))
        print('http2_request_tcp = {};'.format(http2_request_tcp))
        print('http1_response_tcp = {};'.format(http1_response_tcp))
        print('http2_response_tcp = {};'.format(http2_response_tcp))
        print('http1_request_tcp_size = {};'.format(http1_request_tcp_size))
        print('http2_request_tcp_size = {};'.format(http2_request_tcp_size))
        print('http1_response_tcp_size = {};'.format(http1_response_tcp_size))
        print('http2_response_tcp_size = {};'.format(http2_response_tcp_size))
    print('urls = [{}];'.format(', '.join(["'{}'".format(url) for url in target_urls])))
    print('http1_request_ratios_5 = {};'.format(http1_request_ratios_5))
    print('http2_request_ratios_5 = {};'.format(http2_request_ratios_5))
    print('http1_response_ratios_5 = {};'.format(http1_response_ratios_5))
    print('http2_response_ratios_5 = {};'.format(http2_response_ratios_5))
    print('http1_request_ratios_50 = {};'.format(http1_request_ratios_50))
    print('http2_request_ratios_50 = {};'.format(http2_request_ratios_50))
    print('http1_response_ratios_50 = {};'.format(http1_response_ratios_50))
    print('http2_response_ratios_50 = {};'.format(http2_response_ratios_50))
    print('http1_request_ratios_95 = {};'.format(http1_request_ratios_95))
    print('http2_request_ratios_95 = {};'.format(http2_request_ratios_95))
    print('http1_response_ratios_95 = {};'.format(http1_response_ratios_95))
    print('http2_response_ratios_95 = {};'.format(http2_response_ratios_95))


def load_data():
    f1 = open('resource/poseidon_all.json.1')
    f2 = open('resource/poseidon_all.json.2')
    f3 = open('resource/poseidon_all.json.3')
    return json.loads(f1.read())['content'] + json.loads(f2.read())['content'] + json.loads(f3.read())['content']


if __name__ == '__main__':
    main()
