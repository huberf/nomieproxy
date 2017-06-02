import os
from flask import Flask
from flask import request
import requests as r
app = Flask(__name__)

api_head = 'https://api.nomie.io/v2/'
api_key = os.environ['NOMIE_API_KEY']
auth_key = os.environ['PROXY_KEY']

replacements = {
        'pee': '#1',
        'peed': '#1',
        'poo': '#2',
        'pooed': '#2',
        'angry': 'Angry',
        'eat': 'Eat',
        'ate': 'Eat',
        'gamed': 'Gamed',
        'shaved': 'Shave',
        'shave': 'Shave',
        'lonely': 'Lonely',
        'flossed': 'Floss',
        'shower': 'Shower',
        'fingernails': 'Fingernails',
        'shave': 'Shave',
        'cleansed': 'Wash Underarms/Face',
        'soylent': 'Soylent',
        'joylent': 'Soylent'
        }

def url_encode(string):
    # Cleanup later maybe with external library
    return string.replace('/', '%2F').replace(' ', '%20').replace('#', '%23')

@app.route("/")
def main():
    return "Server is functioning."

@app.route('/<auth_input>/<tracker_name>', defaults={'value': None})
@app.route("/<auth_input>/<tracker_name>/<value>")
def h(auth_input, tracker_name, value):
    success = True
    if auth_input == auth_key:
        try:
            final_tracker = tracker_name
            try:
                final_tracker = replacements[tracker_name]
            except:
                do_nothing = True
            cleaned_tracker = url_encode(final_tracker)
            url_to_hit = api_head + 'push/' + api_key + '/action=track/label=' + cleaned_tracker
            if not value == None:
                url_to_hit += '/value=' + value
            r.get(url_to_hit)
        except:
            success = False
    else:
        success = False
    if success:
        return '{"success": "true"}'
    else:
        return '{"success": "false"}'

@app.route('/note/<auth_input>/<text>')
def note(auth_input, text):
    success = True
    if auth_input == auth_key:
        try:
            cleaned_text = url_encode(text)
            url_to_hit = api_head + 'push/' + api_key + '/action=create-note/note=' + cleaned_text
            r.get(url_to_hit)
        except:
            success = False
    if success:
        return '{"success": "true"}'
    else:
        return '{"success": "false"}'

@app.route("/secure", methods=['POST'])
def parse_request():
    # Preparing for future developments
    return "None"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 4000))
    app.run(host='0.0.0.0', port=port, debug=True)
