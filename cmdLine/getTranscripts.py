import requests
headers = {'Authorization' : 'Token e984c8f57689cd880514fdfcc26d85ea06a1a081'}
params = {'app_session_id' : '4da752af-fc39-43ff-a7a9-65912748eebb'}
url = 'https://dev.liv.ai/liv_speech_api/session/transcriptions/'
res = requests.get(url, headers = headers, params = params)
data1=res.json()
print(data1)