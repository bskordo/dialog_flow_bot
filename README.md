### Telegram and VK bots which have been integrated with Google dialogflow



Below parameters declared as environment variables, don't forget to set up:
```
export TELEGRAM_TOKEN='telegram token'
export TELEGRAM_USER_CHAT_ID='telegram_user_chat id'
export NOTIFICATION_TELEGRAM_TOKEN = 'second telegram token'
export PROJECT_ID='project id'
export VK_KEY = 'vk key'
export TELEGRAM_TOKEN='telegram token'
export GOOGLE_APPLICATION_CREDENTIALS='path where is located json file with credentials'
```


### How to Use
Step 1. Create project on DialogFlow (need also create agent)

Step 2. Get google application credential

Step 3. Register new telegram bot for development purposes, get the new token. [@BotFather](https://telegram.me/botfather)

Step 4. Create a new group from VK and get token

Step 5. Install modules from requirements

Step 6. Launch bots


Example of creating a new virtual environments and launch on Linux ,by running create_sample_json.py will be prepared sample phrases
which you can use to create intent(sample version you can find [@hr_job_jumush_bad_bot](https://telegram.me/hr_job_jumush_bad_bot),for vk is chat_dvmb)):

```
virtualenv "name_of_virtualenv"
source "name_of_virtualenv"/bin/activate
pip install -r requirements.txt
python3 create_sample_json.py
python3 create_intent.py sample.json
python3 telegram_bot.py
python3 vk_bot.py
```


How to deploy on Heroku(before need to install heroku cli),need to set up google api credentials json on heroku
information about it you can find [here](https://stackoverflow.com/questions/47446480/how-to-use-google-api-credentials-json-on-heroku)



```
heroku login -i
heroku create
git push heroku master
heroku config:set TELEGRAM_TOKEN='telegram token'
heroku config:set PROJECT_ID='project id'
heroku config:set VK_KEY='vk key'
heroku config:set TELEGRAM_USER_CHAT_ID='telegram_user_chat id'
heroku config:set NOTIFICATION_TELEGRAM_TOKEN = 'second telegram token'
heroku buildpacks:add  https://github.com/gerywahyunugraha/heroku-google-application-credentials-buildpack
heroku ps:scale bot-vk=1
heroku ps:scale bot-tg=1
```

