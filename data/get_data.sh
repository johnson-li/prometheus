#!/usr/bin/env bash

#wget http://prometheus-1151.appspot.com/log/http2_check_all -O 'resource/http2_check.json'

#wget http://prometheus-1151.appspot.com/log/all -O 'resource/api_request_data.json'

#wget http://prometheus-1151.appspot.com/log/traffic_size_all -O 'resource/traffic_size_all.json'

#wget http://prometheus-1151.appspot.com/log/full_web_all -O 'resource/full_web_all.json'

#wget http://prometheus-1151.appspot.com/log/poseidon_all -O 'resource/poseidon_all.json'

for i in `echo {0..10}`
do
    mv "resource/poseidon_all.json.$i" "resource/poseidon_all.json.old.$i"
    proxychains4 wget http://prometheus-1153.appspot.com/log/poseidon_all\?page_size\=1000\&index\=$i -O "resource/poseidon_all.json.new.$i"
    mv "resource/poseidon_all.json.new.$i" "resource/poseidon_all.json.$i"
done

#proxychains4 wget http://prometheus-1151.appspot.com/log/poseidon_all\?page_size\=2000\&index\=0 -O 'resource/poseidon_all.json.new.0'
#proxychains4 wget http://prometheus-1151.appspot.com/log/poseidon_all\?page_size\=2000\&index\=1 -O 'resource/poseidon_all.json.new.1'
#proxychains4 wget http://prometheus-1151.appspot.com/log/poseidon_all\?page_size\=2000\&index\=2 -O 'resource/poseidon_all.json.new.2'
#proxychains4 wget http://prometheus-1151.appspot.com/log/poseidon_all\?page_size\=2000\&index\=3 -O 'resource/poseidon_all.json.new.3'

#mv resource/poseidon_all.json.new.0 resource/poseidon_all.json.0
#mv resource/poseidon_all.json.new.1 resource/poseidon_all.json.1
#mv resource/poseidon_all.json.new.2 resource/poseidon_all.json.2
#mv resource/poseidon_all.json.new.3 resource/poseidon_all.json.3

