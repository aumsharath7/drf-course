import requests


#endpoint = "https://httpbin.org/status/200"
endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.get(endpoint, json={"Query": "Hello La"}) # Http Request

print(get_response.headers)
print(get_response.text) # print raw text response


#print(get_response.text)
#print(get_response.status_code)
#print(get_response.json()['message'])
#print(get_response.json())



