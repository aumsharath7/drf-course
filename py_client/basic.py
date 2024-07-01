import requests


#endpoint = "https://httpbin.org/status/200"
endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.post(endpoint, json={
    "title": "Abc123", "content":  "Hello World", "price":"abc1233"}) # Http Request

#print(get_response.headers)
#print(get_response.text) # print raw text response


#print(get_response.text)
#print(get_response.status_code)
#print(get_response.json()['message'])
print(get_response.json())



