import os
from dotenv import load_dotenv

load_dotenv()

# ==========================================
# 1. FLAT VARIABLES (For Old Files like userbot.py & __init__.py)
# ==========================================
API_ID = int(os.getenv("API_ID", "6435225"))
API_HASH = os.getenv("API_HASH", "4e984ea35f854762dcde906dce426c2d")
BOT_TOKEN = os.getenv("BOT_TOKEN", None)
STRING1 = os.getenv("STRING_SESSION", None)

OWNER_ID = int(os.getenv("OWNER_ID", "7995626429"))
SUPPORT_GRP = "ARISHFA_UPDATE"
UPDATE_CHNL = "THUNDERDEVS"
OWNER_USERNAME = "ll_ISTKHAR_BABY_lll"

# Yeh line purani files ko crash hone se bachayegi
MONGO_URL = os.getenv("MONGO_URL", "")

# Advanced V2 Keys
_openrouter_keys = [
    os.getenv("OPENROUTER_KEY_1", ""),
    os.getenv("OPENROUTER_KEY_2", ""),
    os.getenv("OPENROUTER_KEY_3", "")
]
OPENROUTER_KEYS = [key for key in _openrouter_keys if key]

_mongo_urls = [
    MONGO_URL, # Primary DB
    os.getenv("MONGO_URL_2", ""),
    os.getenv("MONGO_URL_3", "")
]
MONGO_URLS = [url for url in _mongo_urls if url]


# ==========================================
# 2. CLASS VARIABLES (For New V2 Files like Chatgpt.py)
# ==========================================
class Config:
    API_ID = API_ID
    API_HASH = API_HASH
    BOT_TOKEN = BOT_TOKEN
    STRING1 = STRING1
    
    OWNER_ID = OWNER_ID
    SUPPORT_GRP = SUPPORT_GRP
    UPDATE_CHNL = UPDATE_CHNL
    OWNER_USERNAME = OWNER_USERNAME
    
    MONGO_URL = MONGO_URL  # Added for backwards compatibility
    MONGO_URLS = MONGO_URLS
    OPENROUTER_KEYS = OPENROUTER_KEYS
