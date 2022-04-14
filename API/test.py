# from urllib import response
import requests

BASE_URL = "http://127.0.0.1:5000/"

response = requests.get(BASE_URL + "HP")
post_response = requests.post(BASE_URL + "HP")

param_response = requests.get(BASE_URL + "para/SK")
param2_response = requests.get(BASE_URL + "para/Rio")
param3_response = requests.get(BASE_URL + "para/Oli")

video_response = [
    { "name" : "How to Noodle", "views": 1000000, "likes": 19478399,},
    { "name" : "Tenz", "views": 10044242, "likes": 198399,},
    { "name" : "Shazam", "views": 1053540, "likes": 194339,},
    { "name" : "Pokimane", "views": 4927200, "likes": 1318399,},
    { "name" : "Dapr", "views": 9000000, "likes": 111499,},
]


for i in range(len(video_response)):
    response = requests.put(BASE_URL+ "Video/" + str(i), video_response[i])

n = input("enter (0,4)")

response2 = requests.get(BASE_URL+ "Video/{0}".format(n))

# print(response.json())
# print(post_response.json())
# print(param_response.json())
# print(param2_response.json())
# print(param3_response.json())

print(response2)
print(response2.json())