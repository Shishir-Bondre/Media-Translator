import requests
headers = {'Authorization' : 'Token  e984c8f57689cd880514fdfcc26d85ea06a1a081'}
data = {'user' : '16616' ,'language' : 'EN','transcribe' : 1}
files = {'audio_file' : open('/media/sursur/Developer Zone/Media-Translator/development/pages/audio-files/sample03.ogg','rb')}
url = 'https://dev.liv.ai/liv_speech_api/recordings/'
res = requests.post(url, headers=headers, data=data, files=files)

data=res.json()
print(data)