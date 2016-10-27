def encode_mongo_data(data):
    if isinstance(data, (list, tuple)):
        return [encode_mongo_data(d) for d in data]
    if isinstance(data, dict):
        keys_to_wrap = filter(lambda k: '.' in k, data.keys())
        for key in keys_to_wrap:
            data[key.replace('.', '^')] = data.pop(key)
        return {key: encode_mongo_data(val) for key, val in data.iteritems()}
    return data


def decode_mongo_data(data):
    if isinstance(data, (list, tuple)):
        return [decode_mongo_data(d) for d in data]
    if isinstance(data, dict):
        keys_to_unwrap = filter(lambda k: '^' in k, data.keys())
        for key in keys_to_unwrap:
            print(key)
            data[key.replace('^', '.')] = data.pop(key)
        return {key: decode_mongo_data(val) for key, val in data.iteritems()}
    return data


def decode_mongo_key(key):
    return key.replace('^', '.')
