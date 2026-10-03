import requests 

user_message ="Can you tell me about black holes in 3-4 lines"

request_message = {"message": user_message}

url = "http://localhost:5678/webhook-test/420facc7-ff45-4e7d-8409-b2f6c063d726"

response = requests.post(url, json=request_message)

print(response.status_code)

print(response.json()[0]["output"])