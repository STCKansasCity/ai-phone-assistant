# utils.py
import openai
import csv
from datetime import datetime
from flask import Response
from google.cloud import texttospeech

# CONFIG: Set your OpenAI and Google API keys here or via config.py
openai.api_key = "your-openai-api-key"

# CSV Log File
CSV_FILE = "responses.csv"

def log_response(data):
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def transcribe_audio(audio_bytes):
    response = openai.Audio.transcribe("whisper-1", audio_bytes)
    return response["text"]

def generate_gpt_response(prompt):
    reply = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an employee check-in assistant."},
                  {"role": "user", "content": prompt}]
    )
    return reply["choices"][0]["message"]["content"]

def speak_text(text):
    client = texttospeech.TextToSpeechClient()
    input_text = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", name="en-US-Wavenet-D"
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )
    response = client.synthesize_speech(
        input=input_text, voice=voice, audio_config=audio_config
    )
    with open("response.mp3", "wb") as out:
        out.write(response.audio_content)
    return "response.mp3"

def handle_call_event(event_data):
    print(f"Call started: {event_data}")

from flask import Response

def process_audio_stream(request):
    event = request.json
    print("Streaming event received:", event)

    # Respond with OK so Telnyx knows we're listening
    return Response("OK", status=200)

