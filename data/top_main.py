import json

import numpy


def load_data():
    res = []
    for i in range(0, 5):
        res += json.loads(open('resource/poseidon_all.json.{}'.format(i)).read())['content']
    return res


def check_support():
    data = load_data()
    data = filter(lambda x: x['note'] == 'top-20', data)
    data = filter(lambda x: x['http1RequestTcpSize'] > 0, data)
    data = filter(lambda x: x['http2RequestTcpSize'] > 0, data)
    res = []
    with open('/Users/johnson/Workspace/web/top-200') as f:
        for line in f:
            line = line.strip()
            if 'https://{}'.format(line) in [x['targetUrl'] for x in data]:
                res.append(line)
                print '[x]' + line
            else:
                print '[ ]' + line
    print res


def action():
    data = load_data()
    data = filter(lambda x: x['note'] == 'top-20-sni', data)
    data = filter(lambda x: len(x['http2Traces']) > 0, data)
    data = filter(lambda x: x['http1RequestTcpSize'] > 0, data)
    data = filter(lambda x: x['http2RequestTcpSize'] > 0, data)
    data = filter(lambda x: len(x['http1Traces']) == len(x['http2Traces']), data)
    print(len(data))
    print(len(set([x['hostName'] for x in data])))
    targets = set([x['targetUrl'] for x in data])
    print(len(targets))
    http2_percentages = {}
    http2_improvements = {}
    for target in targets:
        print(target)
        target_data = filter(lambda x: x['targetUrl'] == target, data)
        print(numpy.mean([len(d['http1Traces']) for d in target_data]))
        print(numpy.mean([len(d['http2Traces']) for d in target_data]))
        http2_percentages[target] = numpy.mean(
            [len(filter(lambda x: x['protocol'] == 'h2', d['http2Traces'])) * 100 / len(d['http2Traces']) for d in
             target_data])
        http2_improvements[target] = [
            numpy.percentile([(d['http1Time'] - d['http2Time']) / float(d['http1Time']) for d in target_data], p) for p
            in [10, 50, 90]]
        print(numpy.percentile([(d['http1Time'] - d['http2Time']) / float(d['http1Time']) for d in target_data], 10))
        print(numpy.percentile([(d['http1Time'] - d['http2Time']) / float(d['http1Time']) for d in target_data], 50))
        print(numpy.percentile([(d['http1Time'] - d['http2Time']) / float(d['http1Time']) for d in target_data], 90))

    print("http2_tag = {}".format(http2_percentages.keys()))
    print("http2_percentages_val = {}".format(http2_percentages.values()))
    print("http2_improvements = {}".format([x[1] for x in http2_improvements.values()]))


def main():
    action()
    # d = filter(lambda x: x['timeStamp'] == 1476185645328, data)[0]
    # data = filter(lambda x: len(x['http1Traces']) - len(x['http2Traces']) == 0, data)
    # print(len(data))
    # print([len(x['http1Traces']) - len(x['http2Traces']) for x in data])
    # for x in data:
    #     if len(x['http1Traces']) - len(x['http2Traces']) != 0:
    #         print(len(x['http1Traces']) - len(x['http2Traces']))
    #         print(json.dumps(x))
    # print(len(set([x['targetUrl'] for x in data])))
    # single = filter(lambda x: x['targetUrl'] == 'https://dailymotion.com', data)[0]
    # print(json.dumps(d))
    # time_diff = [(x['http1Time'] - x['http2Time']) / float(x['http1Time']) for x in data]
    # print(numpy.mean(filter(lambda x: x > 0, time_diff)))
    # print(numpy.mean(filter(lambda x: x < 0, time_diff)))
    # print(numpy.percentile(filter(lambda x: x > 0, time_diff), 100))
    # print(numpy.percentile(filter(lambda x: x < 0, time_diff), 00))
    # for x in data:
    #     if (x['http1Time'] - x['http2Time']) / float(x['http1Time']) < -2:
    #         print(json.dumps(x))

    # print(filter(lambda x: x['time_elapsed'] == 0, d['http2Traces']))
    # print(sorted([x['time_elapsed'] for x in d['http2Traces']]))
    # print(sorted([x['time_elapsed'] for x in d['http1Traces']]))


if __name__ == '__main__':
    main()
