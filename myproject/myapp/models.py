from django.db import models

# Create your models here.

class MyModel(models.Model):
    id = models.AutoField(primary_key=True)
    path_of_file = models.CharField(max_length=300)
    path_of_audio_file = models.CharField(max_length=300)
    transcription = models.CharField(max_length=500)

    def __int__(self):
        return self.id
