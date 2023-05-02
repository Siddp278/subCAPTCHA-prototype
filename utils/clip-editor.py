from moviepy.editor import VideoFileClip
from dotenv import load_dotenv
import os

load_dotenv()

# Access environment variables
movie_dir = os.getenv('movie_dir')
clip_dir = os.getenv('clip_dir')

# Load the video file
video = VideoFileClip(movie_dir)

# Define the clip duration
clip_duration = 7

# Get the total duration of the video in seconds
total_duration = video.duration

# Extract the audio clips
for i in range(0, int(total_duration), clip_duration):
    if i <= 701:
        start = i
        end = min(i + clip_duration, total_duration)
        clip = video.subclip(start, end)
        # audio_codec ensurs the video file has audio with it.
        clip.write_videofile(clip_dir + f"movie-clip{i}.mp4", 
                            audio_codec='aac',
                            bitrate="2249k", # see the properties of the movie file to fill bitrate and audio_bitrate
                            audio_bitrate="288k",  
                            fps=20)
    else:
        break                        