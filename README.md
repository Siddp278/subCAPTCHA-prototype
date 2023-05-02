# subCAPTCHA-prototype
Created a vide based CAPTCHA where users have to transcribe a video clip from movies

Overview:
ReCAPTCHAs are getting more and more difficult. It interrupts the user's flow and provides a bad user experience. The idea is to switch the difficult image labeling and identification tasks with a video subtitling task. The users will be shown a short clip (i.e. 5-7 seconds clip) taken from a movie, tv show, or other media source, and would be asked to transcribe the text being spoken in the clip, which later can help in generating subtitles and closed captioning for the clips presented. 

Plan for evaluation:
To determine the effectiveness of this proposed system, we intend to compare this to the existing image-based ReCAPTCHA system. Our first evaluation method will be to compare the user experiences of each system. We will look to see if users have a positive or negative outlook on video transcriping tasks while also asking how difficult the task was.
Next we will try the state of the art models for ASR to see if they are able to perform well on the transcription, to see if we are still able to distinguish between humans and bots (the purpose of CAPTCHAs duh!).

Future work:
Splitting of video (movies or tv shows) in a better manner, where subtitiling can be done easily and spacing between scenes and subtitle is appropriate.
