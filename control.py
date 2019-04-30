from bottle import route, run, static_file, response, hook 
import time
import json
import random 
from humidity_sensor import check_humidity
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

# This function will get the data from the data base and return it to the javascript graph
@route('/data1')
def index():
    x = time.time()*1000
    #y = random.uniform(86,95)
    y = check_humidity()[0]
    response.content_type = "application/json"
    return json.dumps([x,y])

@route('/data2')
def index():
    x = time.time()*1000
    #y = random.uniform(27,30)
    y = check_humidity()[1]
    response.content_type = "application/json"
    return json.dumps([x,y])

#This displays the page with the interactive graph
@route('/')
def index2():
    return static_file('index.html', root=os.getcwd())

# This returns all the images in the folder
@route('/images/<filepath:path>')
def server_images(filepath):
    return static_file(filepath, root=os.path.join(os.getcwd(), 'images'))

#This returns all the other css folders
@route('/vendors/<filepath:path>')
def server_vendors(filepath):
    return static_file(filepath, root=os.path.join(os.getcwd(), 'vendors'))

#This also returns the css folders
@route('/css/<filepath:path>')
def server_css(filepath):
    return static_file(filepath, root=os.path.join(os.getcwd(), 'css'))

#This runs the file on the server. Will be put onto the Ashesi Server eventually
if __name__ == "__main__":
    run(host='localhost', port=8080)
