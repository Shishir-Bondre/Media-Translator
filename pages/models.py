from django.db import models

# Create your models here.
class ProfileImage(models.Model):
    image = models.FileField(upload_to='serverFiles')

class Login_Details(models.Model):
    username = models.CharField(max_length=20)
    email =models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class Recording_Details(models.Model):
    username        = models.CharField(max_length=5)
    audio_file      = models.FileField()
    translate_lang  = models.CharField(max_length=5)
    transcript_lang  = models.CharField(max_length=5)
    session_key     = models.CharField(max_length=100)
    extension       = models.CharField(max_length=5)

