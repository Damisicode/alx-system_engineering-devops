#!/usr/bin/python3
"""
Extend the python script from exercise 0 to export data in JSON format.
Record all tasks that owned by the employee.
Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": "TASK_COMPLETED_STATUS", "username": "USERNAME"}, ... ]}
File name must be: USER_ID.json
"""
import requests
from sys import argv

if __name__ == "__main__":
    usr_id = argv[1]
    username = requests.get("http://jsonplaceholder.typicode.com/users/{}".format(usr_id)).json().get("username")
    all_tasks = []
    r = requests.get("http://jsonplaceholder.typicode.com/todos").json()

    for task in r:
        if (task.get("userId") == int(usr_id)):
            temp = {}
            temp["task"] = task.get("title")
            temp["completed"] = task.get("completed")
            temp["username"] = username
            all_tasks.append(temp)

    with open("{}.json".format(usr_id), 'w+') as jsonfile:
        json.dump({usr_id: all_tasks}, jsonfile)
