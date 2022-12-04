class Config(object):
    LOGGER = True

  # Get this value from my.telegram.org/apps
    API_ID = "25626457"
    API_HASH = "9ec8d26f11d68ff7a0371c6988a12c42"

    CASH_API_KEY = "Y15S02GIYRRD03FV"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://izxddlvy:D5nYlGskeU18MW3LCLfvE0wAnRHOvcFY@mouse.db.elephantsql.com/izxddlvy"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1001507509483)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://userbot:userbot@cluster0.x6kstu2.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

  # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/8b94867323e64dd9c8ef8.jpg"

    SUPPORT_CHAT = "NOOBCREATOR"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "5662659781:AAF62BhvZDg9fCmxwZ47i0lGNF3az9oOsAA"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "6YJXZEE7GJOE"  # Get this value from https://timezonedb.com/api

    OWNER_ID = "5656382791"  # User id of your telegram account (Must be integer)

  # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

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
