#!/usr/bin/python3
""" Python script to export data in the JSON format."""
import json
import requests
import sys


if __name__ = "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users_id = sys.argv[1]
    ser = requests.get(url + "users/{}".format(users_id)).json()
    user_name = user.get("username")
    todo = requests.get(url + "todos", params={"userId": users_id}).json()

    with open("{}.json".format(users_id), "w") as file_json:
        json.dump({users_id: [{"task": h.get("title"),
                               "completed": h.get("completed"),
                               "username": user_name} for h in todo]},
                  file_json)

