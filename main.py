import requests
import json

import configparser

config = configparser.ConfigParser()
config.read('config.ini')

USERS_URL = config.get('API', 'URL')

response = requests.get(USERS_URL)


if response.status_code == 200:

    users = response.json()


    for user in users:
        print(f"Name: {user['firstName']}, Surname: {user['lastName']}")
else:
    print(f"Failed to fetch data: {response.status_code}")