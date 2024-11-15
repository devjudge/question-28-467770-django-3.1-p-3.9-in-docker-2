import requests

endpoint = 'http://0.0.0.0:8080/api/add'
payload = {"number1": 1, "number2": 2}
response = requests.post(endpoint, json=payload)
print(response)