#!/usr/bin/python3
"""
Extend the python script from exervise 0 to export daa in CSV format.
Record all tasks that owned by the employee.
Format must be: "USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"
Field name must be: USER_ID.csv
"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    usr_id = argv[1]
    username = requests.get("http://jsonplaceholder.typicode.com/users/{}".format(usr_id)).json().get("username")
    all_tasks = []
    r = requests.get("http://jsonplaceholder.typicode.com/todos").json()

    for task in r:
        if (task.get("userId") == int(usr_id)):
            temp = []
            temp.extend((eid, username, task.get("completed"), task.get("title")))
        all_tasks.append(temp)

    with open("{}.csv".format(usr_id), 'w+') as csvfile:
        writer = csv.writer(csvfile, delimiter=', ', quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerows(all_tasks)
