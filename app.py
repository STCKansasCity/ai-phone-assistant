# app.py
from flask import Flask, request, jsonify
from utils import process_audio_stream, handle_call_event

app = Flask(__name__)

@app.route("/telnyx/call", methods=["POST"])
def telnyx_call():
    bxml = """<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <SpeakSentence voice="female">Welcome to Smart Traffic. Please say your name after the beep.</SpeakSentence>
    <Record />
</Response>"""
    return bxml, 200, {'Content-Type': 'application/xml'}


@app.route("/telnyx/stream", methods=["GET", "POST"])
def telnyx_stream():
    return process_audio_stream(request)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
