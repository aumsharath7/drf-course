import requests

headers = {
    'Authorization': 'Bearer 07c5ffec168d62953ef9466fb6f27144230e7b6d'
    }

endpoint = "http://127.0.0.1:8000/api/products/"

data = {
    'title': 'This field is done 1',
    'price': 32.99
}

get_response = requests.post(endpoint, json=data, headers=headers) 

print(get_response.json())



