import json
import re

import numpy


def load_data():
    # f1 = open('resource/poseidon_all.json.0')
    # f2 = open('resource/poseidon_all.json.1')
    # f3 = open('resource/poseidon_all.json.2')
    # return json.loads(f1.read())['content'] + json.loads(f2.read())['content'] + json.loads(f3.read())['content']
    return json.loads(open('resource/poseidon_all.json.new.10').read())['content']


def main():
    data = load_data()
    # data = filter(lambda x: x['note'] == 'sohu_4', data)
    print(len(data))
    data_full = filter(lambda x: not x['ignoreOuterLink'], data)
    print('http1Time_full = {};'.format([d['http1Time'] for d in data_full]))
    print('http2Time_full = {};'.format([d['http2Time'] for d in data_full]))
    print([len(x['http1Traces']) for x in data_full])
    print([len(x['http2Traces']) for x in data_full])

    http1_res = {}
    pattern = re.compile(".*host='(.+?)'.*")
    address_pattern = re.compile(".*addr='(.+?)'.*")
    for x in data_full:
        res = []
        for key, val in x['http1TcpdumpResponseIpSizes'].iteritems():
            k = pattern.findall(key)[0]
            if 'ajax.googleapis.com' in k:
                res.append(key)
            http1_res.setdefault(k, [])
            http1_res[k].append(val)
        print(set([address_pattern.findall(x)[0] for x in res]))
    traces = data_full[0]['http1Traces']
    for k, v in http1_res.iteritems():
        print('{}: {}, {}'.format(k, numpy.mean(v), len(filter(lambda x: k in x['url'], traces))))
    print(data_full[0]['targetUrl'])


if __name__ == '__main__':
    main()
