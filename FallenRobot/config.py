class Config(object):
    LOGGER = True

  # Get this value from my.telegram.org/apps
    API_ID = "10524301"
    API_HASH = "ba97f182c073dabab267d17baac778df"

    CASH_API_KEY = "BEB4W88XDFMXZTV3"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://vuoximxk:3orHmCe73S0Be4yG7s1NQGb-rR0QCi5Y@snuffleupagus.db.elephantsql.com/vuoximxk"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1001600409884)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://Mr_rian:Fuckyou143@cluster0.rarfs7k.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

  # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://telegra.ph/file/b50e108760a3f95dc0369.mp4"

    SUPPORT_CHAT = "ABOUT_ME143"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "5466910276:AAE5veKZKFGQ_ciDMgsI7sd3gJDUGIaEUxI"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "NQ6CZIENW3CM"  # Get this value from https://timezonedb.com/api

    OWNER_ID = "5983697928"  # User id of your telegram account (Must be integer)

  # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = [5983697928]  # User id of sudo users
    DEV_USERS = [5983697928]  # User id of dev users
    DEMONS = [5983697928]  # User id of support users
    TIGERS = [5983697928]  # User id of tiger users
    WOLVES = [5983697928]  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = (8)

class Production(Config):
    LOGGER = True

class Development(Config):
    LOGGER = True
