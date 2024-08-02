from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch
from api.elastic_test import connect_elasticsearch
from config.config_handling import get_config_value

app = Flask(__name__)

from api.insert_data import *
from api.retrieve_data import *

def connect_elasticsearch(**kwargs):
    _es_config = get_config_value('elastic', 'es_host')
    _es_hosts = [_es_config]
    if 'hosts' in kwargs:
        _es_hosts = kwargs['hosts']
    _es_obj = Elasticsearch(hosts=_es_hosts, timeout=10)
    if _es_obj.ping():
        print('Yay Connect')
    else:
        print('Aww it could not connect!')
    return _es_obj
    
es = connect_elasticsearch()

@app.route('/add_user', methods=['POST'])
def add_user():
    user_id = request.form['id']
    first_name = request.form['fname']
    last_name = request.form['lname']
    job = request.form['job']

    user_obj = {
        'id': user_id,
        'name': f'{first_name} {last_name}',
        'occupation': job
    }
    result = es.index(index='user', id=user_id, body=user_obj, request_timeout=30)
    return jsonify(result)

@app.route('/update_user/<user_id>', methods=['PUT'])
def update_user(user_id):
    update_dict = {
        'doc': {
            'name': 'New Name'
        }
    }
    response = es.update(index='user', id=user_id, body=update_dict)
    return jsonify(response)

@app.route('/search_user', methods=['GET'])
def search_user():
    query_body = {
        "query": {
            "match": {
                "name": 'Name you want to search'
            }
        }
    }
    res = es.search(index="user", body=query_body)
    return jsonify(res)

@app.route('/get_user/<user_id>', methods=['GET'])
def get_user(user_id):
    results = es.get(index='user', id=user_id)
    return jsonify(results)

if __name__ == '__main__':
    app.run()
