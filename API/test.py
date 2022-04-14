# from urllib import response
import requests

BASE_URL = "http://127.0.0.1:5000/"

response = requests.get(BASE_URL + "HP")
post_response = requests.post(BASE_URL + "HP")

param_response = requests.get(BASE_URL + "para/SK")
param2_response = requests.get(BASE_URL + "para/Rio")
param3_response = requests.get(BASE_URL + "para/Oli")

video_response = requests.put(BASE_URL + "Video/1", {"name":"XYZ", "likes": 100, "views": 100000})
video_response2 = requests.put(BASE_URL + "Video/2", {"name":"ABC", "likes": 100})

n = input("enter")

video_response3 = requests.get(BASE_URL+ "Video/{0}".format(n))

print(response.json())
print(post_response.json())
print(param_response.json())
print(param2_response.json())
print(param3_response.json())
print(video_response.json())
print(video_response2.json())
print(video_response3.json())
