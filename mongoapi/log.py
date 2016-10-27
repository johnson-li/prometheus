import time

from bson import ObjectId
from pymongo import MongoClient
from util import codec

from api.base import restful_request
from flask import Blueprint

mongo_log_api = Blueprint('mongo_log', __name__)

__author__ = 'johnson'

client = MongoClient()
db = client.poseidon_database
collection = db.poseidon_collection


@mongo_log_api.route("/mongo_log/poseidon", methods=['POST'])
@restful_request
def poseidon_mongo_log(config, http1_data, http2_data, http2_unsupported, note=None):
    time_stamp = int(time.time() * 1000)
    data = {"timeStamp": time_stamp,
            "config": config,
            'http1Data': http1_data,
            'http2Data': http2_data,
            'http2Unsupported': http2_unsupported,
            'note': note}
    inserted_id = collection.insert_one(codec.encode_mongo_data(data)).inserted_id
    return collection.find_one({'_id': inserted_id})


@mongo_log_api.route("/mongo_log/poseidon/all", methods=['GET'])
@restful_request
def poseidon_mongo_log_all(inserted_id=None, time_stamp=None, note=None):
    if inserted_id is not None:
        inserted_id = inserted_id.encode('ascii', 'ignore')
        return collection.find_one({'_id': ObjectId(inserted_id)})
    if time_stamp is not None:
        time_stamp = int(time_stamp)
        return collection.find({'timeStamp': time_stamp})
    if note is not None:
        note = note.encode('ascii', 'ignore')
        return collection.find({'note': note})
    return collection.find()
