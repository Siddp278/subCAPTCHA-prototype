from django.http import HttpResponse
from .models import MyModel
from django.shortcuts import render

import requests
import os
import random
from dotenv import load_dotenv

load_dotenv()



def my_view(request):
    return HttpResponse("Hello, world!")


def bot_test(request):
    API_TOKEN = os.getenv('API_TOKEN')
    API_URL = os.getenv('API_URL')
    headers = {"Authorization": f"Bearer {API_TOKEN}"}

    index = random.randint(1, 10)
    rr = MyModel.objects.filter(id=index)
    print(rr.values('path_of_audio_file'))
    filename = rr.values('path_of_audio_file')[0]["path_of_audio_file"]    

    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    res = response.json()

    context = {'my_model_instance': rr, 'bot_result': res}
    return render(request, 'bot_test.html', context)


def user_captcha(request):
    pass