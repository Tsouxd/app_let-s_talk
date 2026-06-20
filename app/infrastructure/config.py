import os
from dotenv import load_dotenv

# Charge les variables d'un fichier .env s'il existe à la racine
load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    GOOGLE_CREDENTIALS_PATH = os.getenv("GOOGLE_CREDENTIALS_PATH")
    SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")