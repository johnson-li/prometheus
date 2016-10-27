import json
import numpy


def load_data():
    f1 = open('resource/poseidon_all.json.0')
    f2 = open('resource/poseidon_all.json.1')
    f3 = open('resource/poseidon_all.json.2')
    return json.loads(f1.read())['content'] + json.loads(f2.read())['content'] + json.loads(f3.read())['content']


def main():
    data = load_data()
    data = filter(lambda x: x.get('note', '') == 'non_parallel', data)
    print('http1Time = {};'.format([d['http1Time'] for d in data]))
    print('http2Time = {};'.format([d['http2Time'] for d in data]))
    print('http1Time_1 = {};'.format([filter(lambda a: a['url'] == 'https://www.google.com', d['http1Traces'])[0]['time_elapsed'] for d in data]))
    print('http2Time_1 = {};'.format([filter(lambda a: a['url'] == 'https://www.google.com', d['http2Traces'])[0]['time_elapsed'] for d in data]))
    print('http1Time_2 = {};'.format([filter(lambda a: a['url'] == 'https://www.google.com/images/branding/googlelogo/1x/googlelogo_white_background_color_272x92dp.png', d['http1Traces'])[0]['time_elapsed'] for d in data]))
    print('http2Time_2 = {};'.format([filter(lambda a: a['url'] == 'https://www.google.com/images/branding/googlelogo/1x/googlelogo_white_background_color_272x92dp.png', d['http2Traces'])[0]['time_elapsed'] for d in data]))
    print('http1Time_3 = {};'.format([filter(lambda a: a['url'] == 'https://www.google.com/images/branding/product/ico/googleg_lodp.ico', d['http1Traces'])[0]['time_elapsed'] for d in data]))
    print('http2Time_3 = {};'.format([filter(lambda a: a['url'] == 'https://www.google.com/images/branding/product/ico/googleg_lodp.ico', d['http2Traces'])[0]['time_elapsed'] for d in data]))

    print('http1_size = {};'.format([x['http1TcpdumpResponseIpSizeAll'] for x in data]))
    print('http2_size = {};'.format([x['http2TcpdumpResponseIpSizeAll'] for x in data]))

    print([[a['url'] for a in d['http1Traces']] for d in data][0])
    print([len(d['http2Traces']) for d in data])


if __name__ == '__main__':
    main()
