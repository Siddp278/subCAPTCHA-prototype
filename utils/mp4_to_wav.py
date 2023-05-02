from moviepy.video.io.VideoFileClip import VideoFileClip
from dotenv import load_dotenv
import os
import glob

load_dotenv()

# Access environment variables
movie_dir = os.getenv('movie_dir')
clip_dir = os.getenv('clip_dir')
audio_clip_dir = os.getenv('audio_clip_dir')

data_where = clip_dir

def call_data(link):
    audio = []
    for names in glob.glob(link + "*"):
        audio.append(names.split("\\")[1])

    return audio 

# print(call_data(data_where))

def mp4towav(clip):
    print(clip_dir + clip)
    video = VideoFileClip(clip_dir + clip)
    audio = video.audio
    audio.write_audiofile(audio_clip_dir + clip.split(".")[0] + ".wav")
    video.close()


if __name__ == "main":

    lis = call_data(data_where)

    for audio in lis:
        mp4towav(audio)