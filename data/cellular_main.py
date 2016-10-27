import json

import numpy


def load_data():
    f1 = open('resource/cellular/poseidon_all.json')
    return json.loads(f1.read())['content']


# 2g, 3g, 4g
# http1, http2
# time
# ip traffic, retransmission ratio,

def main():
    data = load_data()
    data_2g = filter(lambda x: x['note'] == 'cellular_2g', data)
    data_3g = filter(lambda x: x['note'] == 'cellular_3g', data)
    data_4g = filter(lambda x: x['note'] == 'cellular', data)
    print(numpy.mean([x['http1Time'] for x in data_4g]))
    print(numpy.mean([x['http2Time'] for x in data_4g]))
    print(numpy.mean([x['http1Time'] for x in data_3g]))
    print(numpy.mean([x['http2Time'] for x in data_3g]))
    print(numpy.mean([x['http1Time'] for x in data_2g]))
    print(numpy.mean([x['http2Time'] for x in data_2g]))

    print([x['http1TcpdumpResponseIpSizeAll'] for x in data_3g])
    print([x['http2TcpdumpResponseIpSizeAll'] for x in data_3g])
    print([x['http1TcpdumpResponseTcpSizeAll'] / float(x['http1ResponseTcpSize']) for x in data_4g])
    print([x['http2TcpdumpResponseTcpSizeAll'] / float(x['http2ResponseTcpSize']) for x in data_4g])
    print([x['http1TcpdumpResponseTcpSizeAll'] / float(x['http1ResponseTcpSize']) for x in data_3g])
    print([x['http2TcpdumpResponseTcpSizeAll'] / float(x['http2ResponseTcpSize']) for x in data_3g])
    print([x['http1TcpdumpResponseTcpSizeAll'] / float(x['http1ResponseTcpSize']) for x in data_2g])
    print([x['http2TcpdumpResponseTcpSizeAll'] / float(x['http2ResponseTcpSize']) for x in data_2g])

    print('names = [{}];'.format(';'.join(["'{}'".format(a) for a in ['(http1, 4g)'] * len(data_4g) + ['(http2, 4g)'] * len(data_4g) + ['(http1, 3g)'] * len(data_3g) + ['(http2, 3g)'] * len(data_3g) + ['(http1, 2g)'] * len(data_2g) + ['(http2, 2g)'] * len(data_2g)])))
    print('data_time = {};'.format([x['http1Time'] for x in data_4g] + [x['http2Time'] for x in data_4g] + [x['http1Time'] for x in data_3g] + [x['http2Time'] for x in data_3g] + [x['http1Time'] for x in data_2g] + [x['http2Time'] for x in data_2g]))
    print('data_size = {};'.format([x['http1TcpdumpResponseIpSizeAll'] for x in data_4g] + [x['http2TcpdumpResponseIpSizeAll'] for x in data_4g] + [x['http1TcpdumpResponseIpSizeAll'] for x in data_3g] + [x['http2TcpdumpResponseIpSizeAll'] for x in data_3g] + [x['http1TcpdumpResponseIpSizeAll'] for x in data_2g] + [x['http2TcpdumpResponseIpSizeAll'] for x in data_2g]))
    print('data_ratio = {};'.format([x['http1TcpdumpResponseTcpSizeAll'] / float(x['http1ResponseTcpSize']) for x in data_4g] + [x['http2TcpdumpResponseTcpSizeAll'] / float(x['http2ResponseTcpSize']) for x in data_4g] + [x['http1TcpdumpResponseTcpSizeAll'] / float(x['http1ResponseTcpSize']) for x in data_3g] + [x['http2TcpdumpResponseTcpSizeAll'] / float(x['http2ResponseTcpSize']) for x in data_3g] + [x['http1TcpdumpResponseTcpSizeAll'] / float(x['http1ResponseTcpSize']) for x in data_2g] + [x['http2TcpdumpResponseTcpSizeAll'] / float(x['http2ResponseTcpSize']) for x in data_2g]))


if __name__ == '__main__':
    main()
