import json

import numpy

import ip_util

ip_map = {}
continents = [u'Europe', u'Australia', u'America', u'Asia', u'Pacific']
URL_LIST = [u'https://planetlab1.ie.cuhk.edu.hk:5555/', u'https://planet-lab1.itba.edu.ar:5555/',
            u'https://planetlab2.cs.ucla.edu:5555/', u'https://pl2.eng.monash.edu.au:5555/',
            u'https://planetlab1.ecs.vuw.ac.nz:5555/', u'https://planetvs2.informatik.uni-stuttgart.de:5555/',
            u'https://planetlab4.goto.info.waseda.ac.jp:5555/']
APP_ENGINE = 'https://isports-1093.appspot.com:443/ping'


def avg(iterable):
    return sum(iterable) / len(iterable)


def get_continent(data):
    if isinstance(data, (str, unicode)):
        host_name = data
    else:
        host_name = data['hostName']
    status = ip_map[host_name]['status']
    if not status == 'success':
        return ''
    time_zone = ip_map[host_name]['timezone']
    continent = time_zone[0:time_zone.find('/')]
    return continent


def valid_host_name(host_name):
    return ip_map[host_name]['status'] == 'success'


def get_host_names(data_list, url_list):
    if not url_list:
        return []
    data_map = {}
    for data in data_list:
        host_name = data['hostName']
        data_map.setdefault(host_name, set()).add(data['targetUrl'])
    return filter(lambda key: data_map[key].issuperset(url_list), data_map.keys())


def generate_heat_map_for_matlab(data_list, url, host_names):
    data_map = {data['hostName']: data for data in data_list
                if data['targetUrl'] == url}
    result = {}
    for host_name in host_names:
        result[host_name] = {}
        https = data_map[host_name]['httpsTransferTime']
        http2 = data_map[host_name]['http2TransferTime']
        result[host_name]['https'] = sum(https) / len(https)
        result[host_name]['http2'] = sum(http2) / len(http2)
    http2_result = {key: val['http2'] for key, val in result.items()}
    https_result = {key: val['https'] for key, val in result.items()}
    http2 = [(https_result[host_name] - http2_result[host_name]) for host_name in host_names]
    print '**'
    print sorted(http2)
    print '**'
    return http2
    # print sorted(http2)
    # print('http2 = ' + str(http2) + ';')


def generate_data_for_matlab(data_list):
    https = []
    http2 = []
    for data in data_list:
        https.extend(data['httpsTransferTime'])
        http2.extend(data['http2TransferTime'])
    https_str = 'https = ' + str(https) + ';'
    http2_str = 'http2 = ' + str(http2) + ';'
    print(https_str)
    print(http2_str)


def parse_requests():
    f = open('resource/api_request_data.json', 'r')
    data_str = f.read()
    data_json = json.loads(data_str)
    data_json = data_json['content']
    host_names = get_host_names(data_json, URL_LIST)
    host_names = sorted(host_names, key=lambda data: get_continent(data))
    print('hosts = {' + ', '.join("'" + host + "'" for host in host_names))
    print('continents = {' + ', '.join("'" + get_continent(host)[:2] + "'" for host in host_names) + '};')
    # generate_data_for_matlab(data_json)
    print('target_urls = {' + ', '.join("'" + url + "'" for url in URL_LIST) + '};')
    data_str = ''
    for url in URL_LIST:
        data_str += ';' + str(generate_heat_map_for_matlab(data_json, url, host_names))
    print('data = [' + data_str + '];')


def parse_single_request():
    f = open('resource/api_request_data.json', 'r')
    data_str = f.read()
    data_json = json.loads(data_str)
    data_json = data_json['content']
    count_map = {}
    for host_name in URL_LIST:
        data_list = filter(lambda data: data['targetUrl'] == host_name, data_json)
        res_list = []
        for data in data_list:
            https = sum(data['httpsTransferTime']) / len(data['httpsTransferTime'])
            http2 = sum(data['http2TransferTime']) / len(data['http2TransferTime'])
            res_list.append(100 * (https - http2) / float(https))
            if sum(data['http2TransferTime']) > sum(data['httpsTransferTime']):
                count_map[data['hostName']] = count_map.get(data['hostName'], 0) + 1
                # print json.dumps(count_map, indent=2)
                # print('data = ' + str(res_list) + ';')
                # https = 'https = ['
                # http2 = 'http2 = ['
                # for data in data_list:
                #     for time in data['http2TransferTime']:
                #         http2 += str(time) + ','
                #     for time in data['httpsTransferTime']:
                #         https += str(time) + ','
                # https += '];'
                # http2 += '];'
                # print https
                # print http2
    print(len(URL_LIST))
    print(json.dumps(count_map, indent=2))


def parse_hosts():
    f = open('resource/host_location.json', 'r')
    data_str = f.read()
    data_json = json.loads(data_str)
    global ip_map
    ip_map = data_json
    # res = ''
    # for key in data_json:
    #     val = data_json[key]
    #     if val['status'] == 'success':
    #         if not res:
    #             res = 'GeoPosition[{{{}, {}}}]'.format(val['lat'], val['lon'])
    #         else:
    #             res += ',GeoPosition[{{{}, {}}}]'.format(val['lat'], val['lon'])
    # print res


def query_ip(ip_list):
    print(json.dumps({ip: ip_util.query_ip_info(ip) for ip in ip_list}))


def load_request_data():
    f = open('resource/api_request_data.json')
    json_data = f.read()
    return json.loads(json_data)['content']


def load_traffic_data():
    f = open('resource/traffic_size_all.json')
    json_data = f.read()
    return json.loads(json_data)['content']


def http2_tcp_size():
    data = load_request_data()
    data = filter(lambda x: x.get('httpsResponseSize', 0) > 0, data)
    data = filter(lambda x: x['targetUrl'] == 'https://www.google.com:443', data)
    http2_time = {}
    http2_req_size = {}
    http2_res_size = {}
    for d in data:
        host = d['hostName']
        http2_time.setdefault(host, []).extend(d['http2TransferTime'])
        http2_req_size.setdefault(host, []).append(d['http2RequestSize'])
        http2_res_size.setdefault(host, []).append(d['http2ResponseSize'])
    hosts = {d['hostName'] for d in data}
    req_var = {}
    req_avg = {}
    res_var = {}
    res_avg = {}
    for host in hosts:
        req_size = http2_req_size.get(host)
        res_size = http2_res_size.get(host)
        req_avg[host] = numpy.average(req_size)
        res_avg[host] = numpy.average(res_size)
        req_var[host] = numpy.std(req_size)
        res_var[host] = numpy.std(res_size)
    req_avg_avg = avg(req_avg.values())
    req_avg_var = numpy.std(req_avg.values())
    res_avg_avg = avg(res_avg.values())
    res_avg_var = numpy.std(res_avg.values())
    print(req_avg_avg)
    print(req_avg_var)
    print(res_avg.values())
    print(res_avg_avg)
    print(res_avg_var)


def https_tcp_size():
    data = load_request_data()
    data = filter(lambda x: x.get('httpsResponseSize', 0) > 0, data)
    data = filter(lambda x: x['targetUrl'] == 'https://www.google.com:443', data)
    https_time = {}
    https_req_size = {}
    https_res_size = {}
    for d in data:
        host = d['hostName']
        https_time.setdefault(host, []).extend(d['httpsTransferTime'])
        https_req_size.setdefault(host, []).append(d['httpsRequestSize'])
        https_res_size.setdefault(host, []).append(d['httpsResponseSize'])
    hosts = {d['hostName'] for d in data}
    req_var = {}
    req_avg = {}
    res_var = {}
    res_avg = {}
    for host in hosts:
        req_size = https_req_size.get(host)
        res_size = https_res_size.get(host)
        req_avg[host] = numpy.average(req_size)
        res_avg[host] = numpy.average(res_size)
        req_var[host] = numpy.std(req_size)
        res_var[host] = numpy.std(res_size)
    req_avg_avg = avg(req_avg.values())
    req_avg_var = numpy.std(req_avg.values())
    res_avg_avg = avg(res_avg.values())
    res_avg_var = numpy.std(res_avg.values())
    print('host num: ' + str(len(hosts)))
    print(req_avg_avg)
    print(req_avg_var)
    print(res_avg_avg)
    print(res_avg_var)


def cmp_tcp_size():
    data = load_request_data()
    data = filter(lambda x: x.get('httpsResponseSize', 0) > 0, data)
    data = filter(lambda x: x['targetUrl'] == 'https://www.google.com:443', data)
    https_req_size = {}
    https_res_size = {}
    http2_req_size = {}
    http2_res_size = {}
    for d in data:
        host = d['hostName']
        https_req_size.setdefault(host, []).append(d['httpsRequestSize'])
        https_res_size.setdefault(host, []).append(d['httpsResponseSize'])
        http2_req_size.setdefault(host, []).append(d['http2RequestSize'])
        http2_res_size.setdefault(host, []).append(d['http2ResponseSize'])
    hosts = {d['hostName'] for d in data}
    https_better_res = 0
    http2_better_res = 0
    https_better_req = 0
    http2_better_req = 0
    for host in hosts:
        hs_req_size = https_req_size.get(host)
        hs_res_size = https_res_size.get(host)
        h2_req_size = http2_req_size.get(host)
        h2_res_size = http2_res_size.get(host)
        if h2_req_size > hs_req_size:
            https_better_req += 1
        else:
            http2_better_req += 1
        if h2_res_size > hs_res_size:
            https_better_res += 1
        else:
            http2_better_res += 1
    print(http2_better_req * 100 / float(http2_better_req + https_better_req))
    print(http2_better_res * 100 / float(http2_better_res + https_better_res))


def https_ip_size():
    traffic_data = load_traffic_data()
    https_req_size = {}
    https_res_size = {}
    for d in traffic_data:
        host = d['hostName']
        https_req_size.setdefault(host, []).append(d['httpsRequestSize'])
        https_res_size.setdefault(host, []).append(d['httpsResponseSize'])
    hosts = {d['hostName'] for d in traffic_data}
    req_var = {}
    req_avg = {}
    res_var = {}
    res_avg = {}
    for host in hosts:
        req_size = https_req_size.get(host)
        res_size = https_res_size.get(host)
        req_avg[host] = numpy.average(req_size)
        res_avg[host] = numpy.average(res_size)
        req_var[host] = numpy.std(req_size)
        res_var[host] = numpy.std(res_size)
    req_avg_avg = avg(req_avg.values())
    req_avg_var = numpy.std(req_avg.values())
    res_avg_avg = avg(res_avg.values())
    res_avg_var = numpy.std(res_avg.values())
    print('host num: ' + str(len(hosts)))
    print(req_avg_avg)
    print(req_avg_var)
    print(res_avg_avg)
    print(res_avg_var)


def http2_ip_size():
    traffic_data = load_traffic_data()
    http2_req_size = {}
    http2_res_size = {}
    for d in traffic_data:
        host = d['hostName']
        http2_req_size.setdefault(host, []).append(d['http2RequestSize'])
        http2_res_size.setdefault(host, []).append(d['http2ResponseSize'])
    hosts = {d['hostName'] for d in traffic_data}
    req_var = {}
    req_avg = {}
    res_var = {}
    res_avg = {}
    for host in hosts:
        req_size = http2_req_size.get(host)
        res_size = http2_res_size.get(host)
        req_avg[host] = numpy.average(req_size)
        res_avg[host] = numpy.average(res_size)
        req_var[host] = numpy.std(req_size)
        res_var[host] = numpy.std(res_size)
    req_avg_avg = avg(req_avg.values())
    req_avg_var = numpy.std(req_avg.values())
    res_avg_avg = avg(res_avg.values())
    res_avg_var = numpy.std(res_avg.values())
    print('host num: ' + str(len(hosts)))
    print({d['targetUrl'] for d in traffic_data})
    print(req_avg_avg)
    print(req_avg_var)
    print(res_avg_avg)
    print(res_avg_var)


def cmp_ip_size():
    data = load_traffic_data()
    https_req_size = {}
    https_res_size = {}
    http2_req_size = {}
    http2_res_size = {}
    for d in data:
        host = d['hostName']
        https_req_size.setdefault(host, []).append(d['httpsRequestSize'])
        https_res_size.setdefault(host, []).append(d['httpsResponseSize'])
        http2_req_size.setdefault(host, []).append(d['http2RequestSize'])
        http2_res_size.setdefault(host, []).append(d['http2ResponseSize'])
    hosts = {d['hostName'] for d in data}
    https_better_res = 0
    http2_better_res = 0
    https_better_req = 0
    http2_better_req = 0
    for host in hosts:
        hs_req_size = https_req_size.get(host)
        hs_res_size = https_res_size.get(host)
        h2_req_size = http2_req_size.get(host)
        h2_res_size = http2_res_size.get(host)
        if h2_req_size > hs_req_size:
            https_better_req += 1
        else:
            http2_better_req += 1
        if h2_res_size > hs_res_size:
            https_better_res += 1
        else:
            http2_better_res += 1
    print(http2_better_req * 100 / float(http2_better_req + https_better_req))
    print(http2_better_res * 100 / float(http2_better_res + https_better_res))


def main():
    # https_tcp_size()
    # http2_tcp_size()
    # http2_ip_size()
    cmp_tcp_size()
    cmp_ip_size()


# parse_hosts()
# parse_single_request()
# parse_requests()
# query_ip(['planetlab1.cs.ucla.edu'])


if __name__ == '__main__':
    main()
