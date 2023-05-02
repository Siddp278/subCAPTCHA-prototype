import requests
import os
from dotenv import load_dotenv
from utils import mp4_to_wav

load_dotenv()

audio_clip_dir = os.getenv('audio_clip_dir')

API_TOKEN = os.getenv('API_TOKEN')

API_URL = os.getenv('API_URL')
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

output = []
audio_list = mp4_to_wav.call_data(audio_clip_dir)
for audio in audio_list:
    output.append(query(audio_clip_dir + audio))
print(output)

    