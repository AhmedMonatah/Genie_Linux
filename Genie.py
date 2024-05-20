import requests
import json
import sys
import emoji
from tqdm import tqdm
# we used gemini api 
API_KEY = ""
user_question = ""
checking_question = ""
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=" + API_KEY
if len(sys.argv) > 1:
        checking_question= "is "+sys.argv[1]+"?question about  Linux terminal i just want yes or no answer one word"
        user_question= sys.argv[1] + " in Linux terminal ? i want a simple answer in shorten way and simple example usage"
else:
    exit()
# we preparing our questions
data = {
    "contents": [
        {
            "parts": [{"text": user_question }]
        }
    ]
}
data2 = {
    "contents": [
        {
            "parts": [
                {"text": checking_question}
            ]
        }
    ]
}
# Headers
headers = {"Content-Type": "application/json"}
#loading animation and adding emoji
print("Loading ..." +emoji.emojize(":thinking_face:") )
with tqdm(total=2, desc="API Requests") as pbar:
    response = requests.post(url, headers=headers, json=data2)
    pbar.update(1)
    response1 = requests.post(url, headers=headers, json=data)
    pbar.update(1)
# Send the POST request and return the answers   
response_checking = requests.post(url, headers=headers, json=data2)
response_user = requests.post(url, headers=headers, json=data)
# Check for if it is about terimnal
checker = ""
if response_checking.status_code == 200:
    response_data = response_checking.json().get('candidates')[0].get('content').get('parts')[0].get('text')
    if response_data == "No" or response_data == "no" or response_data == "NO":
        checker = "NO"
    else:
        checker = "Yes"
else:
    print(f"Error: {response.status_code}")
    print(response_checking.text)
#if it is about linux terimnal print the answer for the user
if checker == "Yes":
    if response_user.status_code == 200:
        response_data1 = response_user.json().get('candidates')[0].get('content').get('parts')[0].get('text')
        print(response_data1) 
    else:
        print(f"Error: {response1.status_code}")
        print(response_user.text)  
else:
     print("I'm sorry, I only answer bash specific questions"+emoji.emojize(":frowning_face:"))
