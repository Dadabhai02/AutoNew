import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '17765492'))
API_HASH = environ.get('API_HASH', '88682d63aba6c3036eda72a70924b577')
BOT_TOKEN = environ.get('BOT_TOKEN', '5843935085:AAHvfex6wmvr6Yx1RZaUvaiTQH3j4LWL2Gw')
# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
PICS = (environ.get('PICS', 'https://telegra.ph/file/51ee26a64cbb7d344347e.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1046893783').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001925918410').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL','-1001810314862')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Leo:Loki@cluster0.mskg6xh.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Leo")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001654788559'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'DaDa_linkz')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "True")), False)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "<b>📝𝑭𝒊𝒍𝒆 𝑵𝒂𝒎𝒆</b> : `{file_name}` \n\n<b>🖇️ 𝑺𝒊𝒛𝒆</b> - {file_size} \n\n<b>𝐽𝑜𝑖𝑛 𝑀𝑜𝑣𝑖𝑒𝑠 𝑈𝑝𝑑𝑎𝑡𝑒𝑠</b> <b>[ DaDa Linkz ](T.me/dada_linkz)</b>")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "**🎞 Tɪᴛʟᴇ** : <a href={url}>{title}</a> \n\n**🎭 Gᴇɴʀᴇᴤ** : </b>: {genres} \n\n**📆 Yᴇᴀʀ** : <a href={url}/releaseinfo>{year}</a> \n\n**🌟 Rᴀᴛɪɴɢ** : <a href={url}/ratings>{rating}</a> \n\n**📀 Rᴜɴᴛɪᴍᴇ** :  {runtime} Minutes \n\n**📆 Rᴇʟᴇᴀᴤᴇ Iɴғᴏ** : {release_date} \n\n**✅ Powered by** : **[ DaDa Linkz ](t.me/dada_linkz)**")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "False")), False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"

HOW_TO_DOWNLOAD =  environ.get('HOW_TO_DOWNLOAD', 'https://t.me/DaDaXBhai/16')

AUTO_DELETE_SECONDS = int(environ.get('AUTO_DELETE_SECONDS', 100))

FILE_REQ_CHANNEL = int(environ.get('FILE_REQ_CHANNEL', LOG_CHANNEL))

SHORTNER_SITE =  environ.get('SHORTNER_SITE', 'shorturllinks.com') #Put Only Shortner Site domain don't put like this https://tnlink.in/

SHORTNER_API =  environ.get('SHORTNER_API', '138545371bfff0b5aa2328f6ac12b5ee7ada0365')

AUTO_DELETE =  environ.get('AUTO_DELETE', 'True')
