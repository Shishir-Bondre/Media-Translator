from django.shortcuts import render

from django.http import HttpResponse

from django.views.generic import TemplateView
#from django.views.generic import request
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage

import requests
import time
import urllib.request

# this for google Translate

from google.cloud import translate


# this is for blob conversion into data

import numpy as np
import scipy.io.wavfile
import math

# this is for decoding

import base64
import os

# this is for converting into audio file from video



class HomePageView(TemplateView):
    template_name = 'index.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

def getInput(request):
    LivApikey ='Token  e984c8f57689cd880514fdfcc26d85ea06a1a081'
    LivApiuserId = '16616'
    transcript=''
    translateFile=''
    if request.method == "POST":
        # this is the code for getting the audio file and saving on client-side        
        audioInputFile = request.FILES['audioFile']
        audioContent=audioInputFile.read()
        # checking the file format
        videoFormats=['mp4','mkv','avi','3gp','mov']
        audioName=audioInputFile.name.split('.')[0]
        ext = audioInputFile.name.split('.')[1]
        # convert video into audio
        if ext in videoFormats:
            fs = FileSystemStorage()
            audioFile = fs.save('pages/uploadedFiles/'+audioName+'.ogg',audioInputFile)
            audioFileUrl = fs.url(audioFile)    
            print(audioInputFile.name)
        else:
            fs = FileSystemStorage()
            audioFile = fs.save('pages/uploadedFiles/'+audioInputFile.name,audioInputFile)
            audioFileUrl = fs.url(audioFile)
        
        # getting the audio language and translatation language
        inputLang=request.POST['inputLang']
        sourceLang=inputLang
        

        # checking whether to call Liv.AI Api or gspeech
        if(inputLang=='EN' or inputLang=='HI' or inputLang=='MX'):
            if(inputLang=='MX'):
                inputLang='EN'
            
            # for Liv.AI
            headers = {'Authorization' :LivApikey }
            
            print(LivApikey)

            #invoking API
            sessionId = LivApiGetSessionId(headers,LivApiuserId,inputLang,audioFileUrl)
            print(sessionId)
            status = LivApiStatus(headers,sessionId)
            print(status)
            if(status):
                transcript=LivApiProcessAudio(headers,sessionId)
                print(transcript)
            else:
                errorMsg= "Could Not Process"
        else:
            # processed to english only

            inputLang='HI'
            headers = {'Authorization' :LivApikey }
            
            print(LivApikey)

            #invoking API
            sessionId = LivApiGetSessionId(headers,LivApiuserId,inputLang,audioFileUrl)
            print(sessionId)
            status = LivApiStatus(headers,sessionId)
            print(status)
            if(status):
                transcript=LivApiProcessAudio(headers,sessionId)
                print(transcript)
            else:
                errorMsg= "Could Not Process"

        # getting iso formats

        #input langauge
        #getting the output language    
        targetLang = request.POST['outputLang']
        print("=========================",targetLang)
        translateFile = getTranslation(transcript['transcript'],sourceLang,targetLang)
        accuracy=transcript['accuracy']*100
        print(accuracy)
        print('=======this is reuslt of return',translateFile)
        return render(request,'output.html',{'transcript':translateFile['sourceText'],'transcriptLang':sourceLang,'translate':translateFile['TargetText'],'translateLang':targetLang,'accuracy':accuracy})
    return render(request,'input.html')

def getOutput(request):
    if request.method == "POST":
        transcript=request.POST['gettranslate']
        targetLang =request.POST['outputLang']
        sourceLang ='EN'
        translateFile = getTranslation(transcript,sourceLang,targetLang)
        return render(request,'output.html',{'transcript':translateFile['sourceText'],'transcriptLang':sourceLang,'translate':translateFile['TargetText'],'translateLang':targetLang,'accuracy':'85.17%'})
    return render(request,'output.html')
            
def LivApiGetSessionId(headers,LivApiuserId,inputLang,audioFileUrl):
    print('This is in getSession1 ',headers)
    data = {'user' : LivApiuserId ,'language' : inputLang ,'transcribe' : 1}
    files = {'audio_file' : open(audioFileUrl,'rb')}
    url = 'https://dev.liv.ai/liv_speech_api/recordings/'
    res = requests.post(url, headers=headers, data=data, files=files)
    data = res.json()
    print(data)
    app_session_id=data['app_session_id']
    return app_session_id

def LivApiStatus(headers,sessionId):
    print('This is in getSession2',headers)
    params = {'app_session_id' : sessionId}
    url = 'https://dev.liv.ai/liv_speech_api/session/status/'
    res = requests.get(url, headers = headers, params = params)
    res=res.json()
    print(res)
    if res['transcribed_status']:
        print("this will return true")
        return res['transcribed_status']
    else:
        return LivApiStatus(headers,sessionId)

def LivApiProcessAudio(headers,sessionId):
    print('This is in getSession3',headers)
    params = {'app_session_id' : sessionId}
    url = 'https://dev.liv.ai/liv_speech_api/session/transcriptions/'
    res = requests.get(url, headers = headers, params = params)
    res=res.json()
    dataSend={'transcript':res['transcriptions'][0]['utf_text'],'accuracy':res['transcriptions'][0]['confidence_score']}
    return dataSend

def getTranslation(transcript,sourceLang,targetLang):
    translate_client = translate.Client()
    # The text to translate
    text = transcript

    # The target language
    target = targetLang
    # Translates some text into Russian
    translation = translate_client.translate(text,target_language= target)
    print(u'Text: {}'.format(text))
    # this is 
    print(u'Translation: {}'.format(translation['translatedText']))
    finalData={'sourceText':format(text),'TargetText':format(translation['translatedText'])}
    print('this is in getTranslation',finalData)
    return finalData


def handle_uploaded_file(file, filename):
    if not os.path.exists('upload/'):
        os.mkdir('upload/')
    b = bytes(file, 'utf-8')
    print(b)
    audioDecode = base64.decodestring(b)
    print(audioDecode)
    # audioResult = open('upload/sample05.ogg','wb') # create a writable image and write the decoding result
    # audioResult.write(audioDecode)

# this is for handling the login and other details


def save_rec(c_username,c_audio_file, c_translate_lang, c_transcript_lang,c_session_key,c_extension):
    record = Recording_Details(
        username=c_username,
        audio_file = c_audio_file,
        translate_lang = c_translate_lang,
        transcript_lang = c_transcript_lang,
        session_key = c_session_key,
        extension = c_extension
    )

    record.save()

# def getRegisterDetails(request):
#     if request.method == "POST":
#         _username = request.POST['uname']
#         _email = request.POST['email']
#         _password = request.POST['pwd']
#         if _username and _password:
#             log = Login_Details.objects.all()
#             for record in log:
#                 if record.username == _username:
#                     return render(request,'input.html',_username)
#             save_login = Login_Details(username=_username,email=_email,password=_password)
#             save_login.save()
#             request.session['username'] = _username
#         return render(request,'input.html',_username)
#     return render(request,'index.html')     

# def getLoginDetails(request):
#     if request.session.has_key('username'):
#         username = request.session['username']
#         print("has session key")
#         return render(request,'input.html',_username)
#     else:
#         #fetch data from login page
#         username = request.POST['email']
#         password = request.POST['pwd']
        
#         #check user authentication
#         log = Login_Details.objects.all()
#         for record in log:
#             if record.username == username and record.password == password:
#                 return redirect('',_username)
#             else:
#                 return redirect('/')

# def user_logout(request):
#     if request.session.has_key('username'):
#         logout(request)
#     return HttpResponse("logged out") 