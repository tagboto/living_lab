from bottle import route, run, static_file, response, hook
import time
import json
from random import randint
import os

@hook('after_request')
def enable_cors():
    """
    You need to add some headers to each request.
    Don't use the wildcard '*' for Access-Control-Allow-Origin in production.
    """
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'


@route('/data')
def index():
    x = time.time()*1000
    y = randint(0,100)
    response.content_type = "application/json"
    return json.dumps([x,y])

@route('/')
def index2():
    return static_file('my_graph.html', root=os.getcwd())


if __name__ == "__main__":
    run(host='localhost', port=8080)

