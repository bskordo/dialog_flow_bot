## Telegram and VK which have been integrated with Google dialogflow(working version you can find @hr_job_jumush_bad_bot,for vk is chat_dvmb)



Below parameters declared as environment variables, don't forget to set up:
```
export TELEGRAM_TOKEN='telegram token'
export TELEGRAM_USER_CHAT_ID='telegram_user_chat id'
export NOTIFICATION_TELEGRAM_TOKEN = 'second telegram token'
export PROJECT_ID='project id'
export VK_KEY = 'vk key'

```


### How to Use
Step 1. Need to create project on DialogFlow 

Step 2. Register new telegram bot for development purposes, get the new token. [@BotFather](https://telegram.me/botfather)

Step 3. Create a new group from VK and get token

Step 4. Install modules from requirements

Step 5. Launch bots


Example of creating a new virtual environments and launch on Linux , Python 3.5:

```
virtualenv "name_of_virtualenv"
source "name_of_virtualenv"/bin/activate
pip install -r requirements.txt
python3 telegram_bot.py
python3 vk_bot.py
```


### How to deploy on Heroku(before need to install heroku cli)


```
heroku login -i
heroku create
git push heroku master
heroku config:set TELEGRAM_TOKEN='1134349295:AAFbzt8f41Y4gVVuJhLFuxZ_N_p5wfXbLLM'
heroku config:set PROJECT_ID='project id'
heroku config:set VK_KEY='vk key'
heroku config:set TELEGRAM_USER_CHAT_ID='telegram_user_chat id'
heroku config:set NOTIFICATION_TELEGRAM_TOKEN = 'second telegram token'
heroku ps:scale bot-vk=1
heroku ps:scale bot-tg=1
```

