# AI_ATL
Project for AI Atlanta Hackathon.
# Speech Processing with OpenAI and Python

This Python script utilizes various libraries to interact with OpenAI's API for both speech-to-text (STT) and text-to-speech (TTS) functionalities. Additionally, it includes features for saving speech as an audio file, triggering audio recordings based on a specified word, and playing audio files.

## Dependencies

Ensure you have the following Python libraries installed:

requests
pygame
os
speech_recognition (install with pip install SpeechRecognition)
pydub (install with pip install pydub)
langchain_implementation (ensure you have the required module)
Set Up OpenAI API Key

Before using the script, replace the api_key variable with your OpenAI API key.
Before using the script, replace the api_key variable with your OpenAI API key.

api_key = "your_openai_api_key"
Functions

Speech-to-Text (STT)
The stt function converts audio files to text using OpenAI's STT API.

stt(file)
Text-to-Speech (TTS)
The tts function generates audio files from text using OpenAI's TTS API.


tts(file, txt)
Save Speech as Audio File
The listen function listens for a trigger word and saves the subsequent speech as an audio file.

listen(trigger_word, output_file_path, timeout=5)
Play Audio File
The play_audio function plays an audio file using the pygame library.

play_audio(file_path)
Usage Example

# Example STT
stt_result = stt("audio_file")
print("Transcription:", stt_result)

# Example TTS
tts("output_audio", "Hello, how are you today?")

# Example Save Speech as Audio File
audio_file_path = listen("hello", "output_audio.wav", timeout=5)

# Example Play Audio File
play_audio(audio_file_path)
Feel free to modify and integrate these functions into your projects!
