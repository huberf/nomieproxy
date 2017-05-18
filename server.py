import os
from flask import Flask
from flask import request
import requests as r
app = Flask(__name__)

api_head = 'https://api.nomie.io/v2/'
api_key = os.environ['NOMIE_API_KEY']
auth_key = os.environ['PROXY_KEY']

replacements = {
        'pee': '#1'
        }

@app.route("/")
def main():
    return "Server is functioning."

@user.route('/<auth_input>/<tracker_name>', defaults={'value': None})
@app.route("/<auth_input>/<tracker_name>/<value>")
def basic_track(auth_input, tracker_name, value):
    success = True
    if auth_input == auth_key:
        try:
            final_tracker = tracker_name
            try:
                final_tracker = replacements[tracker_name]
            except:
                do_nothing = True
            url_to_hit = api_head + 'push/' + api_key + '/label=' + final_tracker
            if not value == None:
                url_to_hit += '/value=' + value
            r.get(url_to_hit)
        except:
            success = False
    else:
        success = False
    return success

@app.route("/secure", methods=['POST'])
def parse_request():
    # Preparing for future developments
    return "None"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 4000))
    app.run(host='0.0.0.0', port=port, debug=True)
