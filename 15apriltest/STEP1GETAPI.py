import statistics
import requests

# '''
# #! {"Data":"[138, 492, 743, 589, 476, 371, 280, 215, 756, 216, 900, 730, 939, 723, 632, 411]","Secret":"CLJEW9"}
# '''

# BASE_URL = "https://dev-api.healthrx.co.in/campus-hiring/input"
# SECERT = "CLJEW9"

# response = requests.get(BASE_URL, params=PARAM)

# jsonData = response.json()
# print(jsonData)




# dict = {'Data': '[922, 799, 572, 1000, 673, 119, 460, 120, 130, 255, 983, 194, 673, 175, 945, 480, 745, 786, 451, 772]', 'Secret': 'Q7GRUV'}

# data = dict['Data']
# print(data)

BASE_URL = "https://dev-api.healthrx.co.in/campus-hiring/input"
SECERT = "CLJEW9"
# PARAM = {"email":"sudhanwakaveeshwarci19@acropolis.in"}
PARAM = {"email":"skdlstudies@gmail.com"}

response = requests.get(BASE_URL, params=PARAM)

jsonData = response.json()

print(jsonData)
# data = jsonData['Data']

# data = data.spilt