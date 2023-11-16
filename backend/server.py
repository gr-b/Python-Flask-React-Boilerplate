import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from math import floor
from flask import Flask, request, send_from_directory
from flask_cors import CORS
import json

from dotenv import load_dotenv

from flask import Flask, redirect, request, url_for, session, Response

load_dotenv()

static_folder = '../app/frontend/build' if os.path.exists('../app/frontend/build') else '../frontend/build/' if os.path.exists('../app/frontend/build') else '../app/build'

app = Flask(__name__, static_url_path='', static_folder=static_folder)
CORS(app)

@app.route('/')
def serve():
    return index()

def index(filename = 'index.html'):
    print(filename, file=sys.stderr)
    print(app.static_folder, file=sys.stderr)
    return send_from_directory(app.static_folder, filename)

@app.route('/img/<filename>')
def img(filename): 
    print(filename, file=sys.stderr)
    return send_from_directory(os.path.join(app.static_folder, 'img'), filename, mimetype='image/vnd.microsoft.icon')

@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(app.static_folder, 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/logo192.png')
def logo192():
    return send_from_directory(app.static_folder, 'logo192.png', mimetype='image/vnd.microsoft.icon')

###########################

@app.route('/api/test')
def test():
   return "Hello World!"



def format_sse(data: str, event=None) -> str:
    """
    Formats a string as a Server-Sent Event message
    """
    msg = f'data: {data}\n\n'
    if event is not None:
        msg = f'event: {event}\n{msg}'
    return msg

def stream_of_events(events):
    """
    Returns flask Response stream of the given list of events.
    Events is a list of dict, where each dict is:
    { "event_type": "<event_type>", "message": "<message>"}
    """
    def stream():
        for event in events:
            yield format_sse(json.dumps(event))

    return Response(stream(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)#, ssl_context="adhoc")
