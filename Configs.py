import os

class Config(object):
    APP_ID = int(os.environ.get("APP_ID", 6))
    API_HASH = os.environ.get("API_HASH", None)
    TOKEN = os.environ.get("TOKEN", None)
    BOT_US = os.environ.get("BOT_US", "")
    WELCOME_TEXT = os.environ.get("WELCOME_TEXT", None)
    RULES = os.environ.get("RULES", None)
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "BAZIGARXD")
    BOT_US = os.environ.get("BOT_USERNAME", "NOINOI_BOT")
