class Config(object):
    LOGGER = True

  # Get this value from my.telegram.org/apps
    API_ID = 
    API_HASH = ""

  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key
    CASH_API_KEY = ""

  # A sql database url from elephantsql.com
    DATABASE_URL = ""

  # Event logs channel to note down important bot level events
    EVENT_LOGS = ()

  # Get ths value from cloud.mongodb.com
    MONGO_DB_URI = ""

  # Telegraph link of the image which will be shown at start command.
    START_IMG = ""

  # Your Telegram support group chat username where your users will go and bother you
    SUPPORT_CHAT = ""

  # Get bot token from @BotFather on Telegram
    TOKEN = ""

  # Get this value from https://timezonedb.com/api
    TIME_API_KEY = ""

  # User id of your telegram account (Must be integer)
    OWNER_ID = 

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
