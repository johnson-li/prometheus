#!/usr/bin/env bash

wget http://prometheus-1151.appspot.com/log/http2_check_all -O 'resource/http2_check.json'

wget http://prometheus-1151.appspot.com/log/all -O 'resource/api_request_data.json'

wget http://prometheus-1151.appspot.com/log/traffic_size_all -O 'resource/traffic_size_all.json'

wget http://prometheus-1151.appspot.com/log/full_web_all -O 'resource/full_web_all.json'
