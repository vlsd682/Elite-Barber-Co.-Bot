import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    DATABASE_URL = 'database url'
    CURRENCY_API_URL = 'api url'
    PROFANITY_FILTER = ["badword1", "badword2"]
