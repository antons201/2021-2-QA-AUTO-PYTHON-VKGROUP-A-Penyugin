import threading

import settings

from flask import Flask, jsonify, request
from werkzeug.serving import WSGIRequestHandler

from utils import responses

app = Flask(__name__)


USERS = {}


@app.route('/get_surname/<name>', methods=['GET'])
def get_get_user_surname(name):
    if surname := USERS.get(name):
        return jsonify(surname=surname), 200
    else:
        return jsonify(responses.USER_NOT_FOUND.format(name)), 404


@app.route('/update_name/<name>/<new_surname>', methods=['PUT'])
def put_update_user_surname(name, new_surname):
    if USERS.get(name):
        USERS[name] = new_surname
        return jsonify(surname=USERS[name]), 200
    else:
        return jsonify(responses.USER_NOT_FOUND.format(name)), 404


@app.route('/delete_name/<name>', methods=['DELETE'])
def delete_delete_user(name):
    if USERS.get(name):
        surname = USERS.pop(name)
        return jsonify(responses.USER_DELETED.format(name, surname)), 200
    else:
        return jsonify(responses.USER_NOT_FOUND.format(name)), 404


def shutdown_mock():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/shutdown')
def shutdown():
    shutdown_mock()
    return jsonify(f'Ok, exiting'), 200


def run_mock():
    server = threading.Thread(target=app.run, kwargs={
        'host': settings.MOCK_HOST,
        'port': settings.MOCK_PORT
    })

    WSGIRequestHandler.protocol_version = "HTTP/1.1"

    server.start()
    return server
