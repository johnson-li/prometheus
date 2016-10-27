import json

import numpy


def load_data():
    f1 = open('resource/poseidon_all.json.0')
    f2 = open('resource/poseidon_all.json.1')
    f3 = open('resource/poseidon_all.json.2')
    # f4 = open('resource/poseidon_all.json.3')
    return json.loads(f1.read())['content'] + json.loads(f2.read())['content'] + json.loads(f3.read())['content']


def main():
    data = load_data()
    data = filter(lambda x: x['note'] == 'google_no_multiplexing', data)
    print('http1Time = {};'.format([x['http1Time'] for x in data]))
    print('http2Time = {};'.format([x['http2Time'] for x in data]))
    print(numpy.mean([x['http1Time'] for x in data]) / float(numpy.mean([x['http2Time'] for x in data])))


if __name__ == '__main__':
    main()
