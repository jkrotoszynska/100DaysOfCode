import requests

QUEST_AMOUNT = 10 
QUEST_TYPES = "boolean"

param = {
    "amount": QUEST_AMOUNT,
    "type": QUEST_TYPES
}


response = requests.get(url="https://opentdb.com/api.php", params=param)

response.raise_for_status()
data = response.json()
question_data = data["results"]