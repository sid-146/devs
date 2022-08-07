import json

with open('./test2.json') as file:
    data = json.loads(file)

    print(data)