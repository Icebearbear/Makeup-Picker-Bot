# Makeup Picker Bot

## Introduction
A Chat Bot that gives makeup product recommendation based on the given information/description of their desired products from users. This Bot will recommend the best product in the market and where to get them.

## Features
- Product recommendation based on user input
- Suggest location to purchase the product in SG
- Suggest online resources to purchase the product
- Show people opinion about the product on Twitter
- Tells pun jokes/memes about makeup (optional)

## Tech
- Google API for products, address, reviews and links
- Twitter API for comments
- Jokes API (optional)
- [Python Telegram Bot](https://github.com/python-telegram-bot/python-telegram-bot)

## The Flow of the Bot 
- Introduction - what does this bot do 
- Start button - to start the Bot
- Product Type - category of the product e.g blush, foundation (button form)
- Product Brand - user's desired brand (button form)
- Product Tag List - additional info e.g vegan , alcohol free (button form)
- Price - <$20 , $20 - $60 ,  $60 - $100 , > $100 (button form)
- skip - to skip the queries (button)
- /help - instructions to use the bot
- /done - to finish

## Intallation
Ensure that pip and python is installed

install pipenv for dependencies management. List of dependencies will be listed on Pipfile. Make sure that pipenv path is added to the system.
```sh
pip install --user pipenv
```

install python-telegram-bot library
```sh
pipenv install python-telegram-bot
```

### Python Telegram Bot Setup
It is a library provides a pure Python interface for Telegram Bot API.
First, generate an access token by talking to [BotFather](https://t.me/botfather) by following these steps https://core.telegram.org/bots#6-botfather. Now you are ready to create the bot!
There are two most important classes in the bot:
1. Updater 
    it continuously fetches all updates from telegram and passes them to Dispatcher
2. Dispatcher
    Updater object will then create a Dispathcer and link them with a Queue.
    User will then register handlers in the Dispatcher which will sort the updates fetched by the Updater and deliver back a callback function

After adding all the classes with handlers and callback functions, it is time to start the bot by running :
```py
updater.start_polling()
```

In order to stop the bot, run :
```py
updater.stop()
```

Or use Ctrl + C to receive signals (SGINT/SIGTERM/SIGABRT) to stop the bot, run:
```py
updater.idle()
```

