import requests

API = 'http://ip-api.com/json'


def query_ip_info(ip):
    """
    server document http://ip-api.com/docs/api:json
    json format
    {
    "status": "success",
    "country": "COUNTRY",
    "countryCode": "COUNTRY CODE",
    "region": "REGION CODE",
    "regionName": "REGION NAME",
    "city": "CITY",
    "zip": "ZIP CODE",
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "timezone": "TIME ZONE",
    "isp": "ISP NAME",
    "org": "ORGANIZATION NAME",
    "as": "AS NUMBER / NAME",
    "query": "IP ADDRESS USED FOR QUERY"
    }
    :param ip:
    :return: json
    """
    url = API + '/' + ip
    r = requests.get(url)
    return r.json()
