import json


def load_http2_support_data():
    f = open('resource/http2_check.json')
    data_str = f.read()
    data = json.loads(data_str)['content']
    return {d['host']: d for d in data}


def load_top_pages_data():
    f = open('resource/top500pages.json')
    data_str = f.read()
    return json.loads(data_str)


def main():
    pages = load_top_pages_data()
    data = load_http2_support_data()
    support = []
    for page in pages[0:500]:
        d = data.get(page, None)
        if d and d['support']:
            support.append(page)
    print len(support)
    print json.dumps(support, indent=2)


if __name__ == '__main__':
    main()
