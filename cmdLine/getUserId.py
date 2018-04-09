import requests

headers = {'Authorization' : 'Token 6663b83d1c5d1243a3aaa0ccddfc87e4e52cef18'}
data = {'device_id' : '73107B33313E17C1' ,'platform' : 'shell'}
url = 'https://dev.liv.ai/liv_transcription_api/appusers/'
res = requests.post(url, headers = headers, data = data)
data = res.json()
print(data)