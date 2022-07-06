import requests

BASE_URL ="http://127.0.0.1:5000/"

data = [
    {"array": [1,2,4,5,5,6,3]},
    {"array": [1,2,4,3]},
    {"array": [2,2334,3]},
]


for i in range(len(data)):
    response = requests.post(BASE_URL + 'Que/', data[i])
    print(response.json())


response2 = requests.get(BASE_URL + 'Que/1')
print(response2.json())