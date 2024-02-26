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
API_ID = int(environ.get('API_ID', '21723146'))
API_HASH = environ.get('API_HASH', '07cd9c82699c28111cb33693ecbd9116')
BOT_TOKEN = environ.get('BOT_TOKEN', '')
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1030335104').split()]
USERNAME = environ.get('USERNAME', 'https://t.me/Attitude2688')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001896609847'))
MOVIE_GROUP_LINK = environ.get('MOVIE_GROUP_LINK', 'https://t.me/DD_Movies_Request')
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001569815531').split()]
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_URI2 = environ.get('DATABASE_URI2', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Aks2")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Aks')
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-1001626107740'))
QR_CODE = environ.get('QR_CODE', 'https://telegra.ph/file/1ad00e3b6ec43062e72b8.jpg')

#this vars is for when heroku or koyeb acc get banned, then change this vars as your file to link bot name
BIN_CHANNEL = int(environ.get('BIN_CHANNEL', '-1001896609847'))
URL = environ.get('URL', 'aks-file-to-link-525cd78edc50.herokuapp.com')

# verify system vars
IS_VERIFY = is_enabled('IS_VERIFY', True)
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1001720210775'))
TUTORIAL = environ.get("TUTORIAL", "https://t.me/bots_up")
TUTORIAL2 = environ.get("TUTORIAL2", "https://t.me/bots_up/165")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg")
SHORTENER_API = environ.get("SHORTENER_API", "388ed97f90606d81da656088cc6721395b699bba")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "ziplinker.net")
SHORTENER_API2 = environ.get("SHORTENER_API2", "1153050002b2b2f39c7e58be093cc72f6c576649")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "onepagelink.in")
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "600"))

# languages search
LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam"]

AUTH_CHANNEL = [int(auth_channels) for auth_channels in environ.get('AUTH_CHANNEL', '-1001954276464').split()]
if len(AUTH_CHANNEL) == 0:
    print('Info - AUTH_CHANNEL is empty')
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '-1001998528019'))

# hastags request features
request_channel = environ.get('REQUEST_CHANNEL', '-1002018748408')
REQUEST_CHANNEL = int(request_channel) if request_channel and id_pattern.search(request_channel) else None

# bot settings
IS_PM_SEARCH = is_enabled('IS_PM_SEARCH', False)
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
PORT = os.environ.get('PORT', '8080')
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
