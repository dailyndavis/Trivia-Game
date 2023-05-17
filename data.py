# ✨👩🏻‍💻 Challenge 👩🏻‍💻✨
# 1 - Modify the data.py file (don't change main.py)
# 2 - Make a get() request to fetch 10 true/false questions
# 3 - Parse the JSON response and replace the value of question_data (don't change
#     the variable name) 
#     Hint: Create a Python dictionary for the amount and type parameters 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
import requests

parameters = {
    "amount": 10,
    "type": "boolean"
    }

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()

question_data = data["results"]