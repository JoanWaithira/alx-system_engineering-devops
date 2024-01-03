#!/usr/bin/python3
""" Python script to export data in the CSV format."""
import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(users_id)).json()
    user_name = user.get("username")
    todo = requests.get(url + "todos", params={"userId": users_id}).json()

    with open("{}.csv".format(users_id), "w") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow([users_id, user_name, h.get("completed"),
                          h.get("title")]) for h in todo]
