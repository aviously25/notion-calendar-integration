import requests
import json
import os
from datetime import date

from dotenv import load_dotenv
load_dotenv()

bearer = os.getenv("BEARER")
database_id = os.getenv("DATABASE_ID")

url = "https://api.notion.com/v1/databases/{}/query".format(database_id)
headers = {
    "Authorization": "Bearer {}".format(bearer),
    "Notion-Version": "2021-05-13",
    "Content-Type": "application/json"
}
params = {
    'filter': {
        "property": "Due",
        "date": {
            "after": date.today().isoformat()
        }
    }
}
res = requests.post(url, headers=headers, data=json.dumps(params))

print(res.json())
