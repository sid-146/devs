# from urllib import response
import requests

BASE_URL = "http://127.0.0.1:5000/"

response = requests.get(BASE_URL + "HP")
post_response = requests.post(BASE_URL + "HP")

param_response = requests.get(BASE_URL + "para/SK")
param2_response = requests.get(BASE_URL + "para/Rio")
param3_response = requests.get(BASE_URL + "para/Oli")

print(response.json())
print(post_response.json())
print(param_response.json())
print(param2_response.json())
print(param3_response.json())
