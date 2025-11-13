# app.py
from flask import Flask, request, jsonify
from utils import process_audio_stream, handle_call_event

app = Flask(__name__)

@app.route("/telnyx/call", methods=["POST"])
def telnyx_call():
    event_data = request.json
    handle_call_event(event_data)
    return "OK", 200

@app.route("/telnyx/stream", methods=["GET", "POST"])
def telnyx_stream():
    return process_audio_stream(request)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
