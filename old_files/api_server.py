import flask
import test_data
import json

from old_files.parse_webrtc_dump import iterate_through_peer_connections

def parse_webrtc_dump():
    with open('test.txt') as raw_stats:
        all_data = json.load(raw_stats)
        parsed_peer_connections_data = iterate_through_peer_connections(all_data)
        return parsed_peer_connections_data


data = test_data.data


app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    parsed_peer_connections_data = parse_webrtc_dump()
    return parsed_peer_connections_data

app.run()