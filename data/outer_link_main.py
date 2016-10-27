import json

import numpy


def load_data():
    f1 = open('resource/poseidon_all.json.0')
    f2 = open('resource/poseidon_all.json.1')
    f3 = open('resource/poseidon_all.json.2')
    return json.loads(f1.read())['content'] + json.loads(f2.read())['content'] + json.loads(f3.read())['content']


def main():
    data = load_data()
    data = filter(lambda x: x['note'] == 'yahoo', data)
    data_ignore = filter(lambda x: x['ignoreOuterLink'], data)
    data_full = filter(lambda x: not x['ignoreOuterLink'], data)
    print(len(data_ignore), len(data_full))
    print([x['http1Time'] for x in data_ignore])
    print([x['http2Time'] for x in data_ignore])
    print(numpy.mean([x['http1Time'] for x in data_full]))
    print(numpy.mean([x['http2Time'] for x in data_full]))
    # print("".format(numpy.mean([filter(lambda a: a['url'] == 'https://www.yahoo.com', x['http1Traces'])[0]['time_elapsed'] for x in data_ignore])))
    # print(numpy.mean(
    #     [filter(lambda a: a['url'] == 'https://www.yahoo.com', x['http2Traces'])[0]['time_elapsed'] for x in
    #      data_ignore]))
    h1_fp_time = []
    h2_fp_time = []
    for d in data_full:
        for a in filter(lambda a: 'polyfill.min.js' in a['url'], d['http1Traces']):
            h1_fp_time.append(a['time_elapsed'])
        for a in filter(lambda a: 'polyfill.min.js' in a['url'], d['http2Traces']):
            h2_fp_time.append(a['time_elapsed'])
    print('h1_fp_time = {};'.format(numpy.mean(h1_fp_time)))
    print('h2_fp_time = {};'.format(numpy.mean(h2_fp_time)))

    # print([d['http2TcpdumpResponseTcpSizeAll'] / float(d['http2ResponseTcpSize']) for d in data_full])

    # print("h1_fp_time = {};".format([filter(lambda a: a['url'] == 'https://www.yahoo.com/favicon.ico', x['http1Traces'])[0]['time_elapsed'] for x in data_full]))
    # print("h2_fp_time = {};".format([filter(lambda a: a['url'] == 'https://www.yahoo.com/favicon.ico', x['http2Traces'])[0]['time_elapsed'] for x in data_full]))
    # print("h1_fp_5 = {};".format(numpy.percentile(
    #     [filter(lambda a: a['url'] == 'https://www.yahoo.com', x['http1Traces'])[0]['time_elapsed'] for x in data_full],
    #     5)))
    # print("h2_fp_5 = {};".format(numpy.percentile(
    #     [filter(lambda a: a['url'] == 'https://www.yahoo.com', x['http2Traces'])[0]['time_elapsed'] for x in data_full],
    #     5)))
    # print("h1_fp_50 = {};".format(numpy.percentile(
    #     [filter(lambda a: a['url'] == 'https://www.yahoo.com', x['http1Traces'])[0]['time_elapsed'] for x in data_full],
    #     50)))
    # print("h2_fp_50 = {};".format(numpy.percentile(
    #     [filter(lambda a: a['url'] == 'https://www.yahoo.com', x['http2Traces'])[0]['time_elapsed'] for x in data_full],
    #     50)))
    # print("h1_fp_95 = {};".format(numpy.percentile(
    #     [filter(lambda a: a['url'] == 'https://www.yahoo.com', x['http1Traces'])[0]['time_elapsed'] for x in data_full],
    #     95)))
    # print("h2_fp_95 = {};".format(numpy.percentile(
    #     [filter(lambda a: a['url'] == 'https://www.yahoo.com', x['http2Traces'])[0]['time_elapsed'] for x in data_full],
    #     95)))
    print(numpy.mean([x['http1ResponseTcpSize'] for x in data_ignore]))
    print(numpy.mean([x['http2ResponseTcpSize'] for x in data_ignore]))
    print(numpy.mean([x['http1ResponseTcpSize'] for x in data_full]))
    print(numpy.mean([x['http2ResponseTcpSize'] for x in data_full]))


if __name__ == '__main__':
    main()
