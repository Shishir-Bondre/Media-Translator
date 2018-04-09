## Media Translator
> ### Application for generating **transcript,translated,subtitle file** in **multiple indian languages** for the spoken words of the given audio/video or recorded audio/video file.

### Features:
> 1) Transcript/Translation in 10 + Indian Languages
> 2) Subtitle files along with Audio/Video Player
> 3) Processing for 120MB files/ 60 minutes 
> 4) Input for audio/video Files
> 5) Recording option
> 6) Sharing option over facebook
> 7) Store the files, also can browse history

### Contents :
    1) Installation Guide  
    2) Technology Used  
    3) How to use it

### 1) Installation Guide :
    i) Requires Python 3.6.4
    ii) Requires Python Virtual Enviornment
    iii) Requires Node installed
    iv) Requires Sqlite installed
    v) pip install -r requirements.txt
    vi) You need a google.developer account setup, so as to access the google translate API.

> ### Steps for setting up the google account
> ## Type the commands in your console
> 1) Create the service account. Replace [NAME] with your desired service account name.
>> gcloud iam service-accounts create [NAME]
> 2) Grant permissions to the service account. Replace [PROJECT_ID] with your project ID.
>> gcloud projects add-iam-policy-binding [PROJECT_ID] --member "serviceAccount:[NAME]@[PROJECT_ID].iam.gserviceaccount.com" --role "roles/owner"
> 3) Generate the key file. Replace [FILE_NAME] with a name for the key file.
>> gcloud iam service-accounts keys create [FILE_NAME].json --iam-account [NAME]@[PROJECT_ID].iam.gserviceaccount.com
> 4) Replace [PATH] with the file path of the JSON file that contains your service account key.
>> export GOOGLE_APPLICATION_CREDENTIALS="[PATH]"
> 5) example
>> export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/service-account-file.json"


### 2) Technology Stack
    > Application is developed in Django-Framework and uses Node-js as a glue. 
    > Used relational database for storing and authentication purpose.
    > Used google and Facebook O'auth for authentication.
    > Facebook Messenger Api
    > google translate Api
    > used generating SRT file an open source project by MIT licinese

### 3) How to use it
    Run the following commands from terminal(linux or macOS)
    > pipenv shell
    > python manage.py runserver
    > open browser and type http://127.0.0.1:8000

### project will run happy browsing :)









