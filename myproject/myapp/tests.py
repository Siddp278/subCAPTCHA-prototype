# import requests
# import os
# from dotenv import load_dotenv

# import django
# from django.test import TestCase
# from .models import MyModel

# django.setup()
# load_dotenv()

# audio_clip_dir = os.getenv('audio_clip_dir')

# API_TOKEN = os.getenv('API_TOKEN')

# API_URL = os.getenv('API_URL')
# headers = {"Authorization": f"Bearer {API_TOKEN}"}


# def query(filename):
#     with open(filename, "rb") as f:
#         data = f.read()
#     response = requests.post(API_URL, headers=headers, data=data)
#     return response.json()

# class MTest(TestCase):

#     def call_data(self):
#         obs = MyModel.objects.all()
#         obs_need = obs.values('path_of_audio_file', 'transcription')
#         print(obs_need)

# call_data()    

# output = []
# audio_list = call_data(audio_clip_dir)
# for audio in audio_list:
#     output.append(query(audio_clip_dir + audio))
# print(output)

from django.test import TestCase
from .models import MyModel

class MyTestCase(TestCase):
    #  Each test case method should start with the prefix "test_" and should contain the code you want to test.
    def test_addition(self):
        print("Hello World!")

    def test_data_retrieve(self):
        obs = MyModel.objects.all()
        obs_need = obs.values('path_of_audio_file', 'transcription')
        expected = []*10
        self.assertCountEqual(obs_need, expected)