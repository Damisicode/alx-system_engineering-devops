#!/usr/bin/python3
"""
Extend the python script from exercise 0 to export data in JSON format.
Record all tasks that owned by the employees.
Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": "TASK_COMPLETED_STATUS", "username": "USERNAME"}, ... ], "USER_ID": [{"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS", "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": "TASK_COMPLETED_STATUS", "username": "USERNAME"}, ...]}
File name must be: todo_all_employees.json
"""
import requests
import json

if __name__ == "__main__":
    users = requests.get("http://jsonplaceholder.typicode.com/users").json()
    tasks = requests.get("http://jsonplaceholder.typicode.com/todos").json()
    store = {}

    for user in users:
        usr_id = user.get("id")
        username = user.get("username")
        all_tasks = []

        for task in tasks:
            if (task.get("userId") == int(usr_id) and task.get("completed")):
                temp = {}
                temp["task"] = task.get("title")
                temp["completed"] = task.get("completed")
                temp["username"] = username
                all_tasks.append(temp)
        store[usr_id] = all_tasks

    with open("todo_all_employees.json", 'w+') as jsonfile:
        json.dump(store, jsonfile)
