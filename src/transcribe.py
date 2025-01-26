import speech_recognition as sr
from pydub import AudioSegment
import os

def convert_to_wav(file_path):
    if not file_path.endswith(".wav"):
        audio = AudioSegment.from_file(file_path)
        wav_path = os.path.splitext(file_path)[0] + ".wav"
        audio.export(wav_path, format="wav")
        return wav_path
    return file_path

def transcribe_audio(file_path):
    # Convert to WAV if necessary
    file_path = convert_to_wav(file_path)

    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(file_path) as source:
            audio = recognizer.record(source)
        transcription = recognizer.recognize_google(audio)
        return transcription
    except sr.UnknownValueError:
        return "Could not understand the audio."
    except sr.RequestError as e:
        return f"API request failed; {e}"
    except ValueError as e:
        return f"Error: {e}"