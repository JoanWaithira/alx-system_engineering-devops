#!/usr/bin/python3
""" A script that returns infrmatin about an employee"""
import sys
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_name = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todo = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed_tasks = [h.get("title") for h in todo if h.get("completed")
                       is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user_name.get("name"), len(completed_tasks), len(todo)))
    [print("\t {}".format(i)) for i in completed_tasks]
