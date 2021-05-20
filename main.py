import requests
import os

from dotenv import load_dotenv
load_dotenv()

bearer = os.getenv("BEARER")
database_id = os.getenv("DATABASE_ID")

req = requests.get("https://api.notion.com/v1/databases")
