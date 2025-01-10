import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "rydersharpe"
TOKEN = "12345678"
GRAPH_ID = "mygraph1"

website = "https://pixe.la/v1/users/rydersharpe/graphs/mygraph1.html"
print(f"\n\n{website}\n\n")

# DATE STUFF-----------------
today = datetime.now()
# print(today)

formatted_date = today.strftime("%Y%m%d")
# print(d)

#------------------

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "mygraph1",
    "name": "Music Practise Graph",
    "unit": "hours",
    "type": "float",
    "color": "momiji"
}

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_date}"

headers = {
    "X-USER-TOKEN": TOKEN
}



pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "0",
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

response = requests.put(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

