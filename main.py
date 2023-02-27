import requests
from datetime import datetime

TOKEN = YOUR TOKEN
USERNAME = YOUR USERNAME
GRAPH_ID = "graph1"

"""Below i created an account and a graph on pixela"""
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

"""Below i posted on my graph and also backed-dated it with D keyword (post)."""
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hour",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixela_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()  # datetime(year=2022, month=8, day=17) --> Dis line of code in gray is use for back dating date.
# print(today.strftime("%Y%m%d"))  # D "today.strftime()" is use for formatting d appearance of date.

pixela_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you code today? "),
}

# response = requests.post(url=pixela_creation_endpoint, json=pixela_data, headers=headers)
# print(response.text)

"""Below i updated my post on my graph with D keyword (put)"""
pixela_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

pixela_update_data = {
    "quantity": input("update the hour you coded? ")
}

# response = requests.put(url=pixela_update_endpoint, json=pixela_update_data, headers=headers)
# print(response.text)

"""Below i deleted my post on my graph with D keyword (delete)"""
pixela_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=pixela_update_endpoint, headers=headers)
# print(response.text)
