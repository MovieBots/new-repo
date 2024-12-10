import re
import os
from os import environ
from pyrogram import enums
from Script import script
import asyncio
import json
from collections import defaultdict
from pyrogram import Client

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

#main variables
API_ID = int(environ.get('API_ID', '29236719'))
API_HASH = environ.get('API_HASH', '1ccf1bd0a86af974e3210a55f662c062')
BOT_TOKEN = environ.get('BOT_TOKEN', '')
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '893383574').split()]
USERNAME = environ.get('USERNAME', 'https://t.me/Arpitbotmovies')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002074744533'))
MOVIE_GROUP_LINK = environ.get('MOVIE_GROUP_LINK', '')
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002222465571').split()]
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://arpitgavla121:vWDED1tOOmdV0mAq@cluster0.kic1m.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_URI2 = environ.get('DATABASE_URI2', "mongodb+srv://arpitgavla121:vWDED1tOOmdV0mAq@cluster0.kic1m.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "Arpit")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'ArpitBots')
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-1002074744533'))
QR_CODE = environ.get('QR_CODE', 'https://telegra.ph/file/378a08d7e1bca338db963-d05a2ded13e2ffa4dd.jpg')

#this vars is for when heroku or koyeb acc get banned, then change this vars as your file to link bot name
BIN_CHANNEL = int(environ.get('BIN_CHANNEL', '-1002074744533'))
URL = environ.get('URL', '166.0.242.207:12731')

# verify system vars
IS_VERIFY = is_enabled('IS_VERIFY', True)
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1002074744533'))
TUTORIAL = environ.get("TUTORIAL", "https://t.me/+RsQwXu9PiiQ1MjNl")
TUTORIAL2 = environ.get("TUTORIAL2", "https://t.me/+RsQwXu9PiiQ1MjNl")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg")
SHORTENER_API = environ.get("SHORTENER_API", "4d0ef91df5b74f843ba1ef1223d66d86b6f6f81a")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "instantearn.in")
SHORTENER_API2 = environ.get("SHORTENER_API2", "4d0ef91df5b74f843ba1ef1223d66d86b6f6f81a")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "instantearn.in")
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "43200"))

# languages search
LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam"]

auth_channel = environ.get('AUTH_CHANNEL', '-1002314687215')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '-1002074744533'))

# hastags request features
request_channel = environ.get('REQUEST_CHANNEL', '-1002074744533')
REQUEST_CHANNEL = int(request_channel) if request_channel and id_pattern.search(request_channel) else None

# bot settings
IS_PM_SEARCH = is_enabled('IS_PM_SEARCH', True)
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
PORT = os.environ.get('PORT', '8081')
MAX_BTN = int(environ.get('MAX_BTN', '8'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 1200))
IMDB = is_enabled('IMDB', False)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', True)
