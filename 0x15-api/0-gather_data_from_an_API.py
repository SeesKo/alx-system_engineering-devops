#!/usr/bin/python3
"""
Script to fetch and display TODO list progress
for a given employee using an API.
"""
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]

    # Base URL for the REST API
    base_url = 'https://jsonplaceholder.typicode.com/'

    # Get employee information
    user_url = '{}users/{}'.format(base_url, employee_id)
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Get TODO list information
    todos_url = '{}todos?userId={}'.format(base_url, employee_id)
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Filter completed tasks
    completed_tasks = [task for task in todos if task.get("completed")]

    # Display the TODO list progress
    print(
        f"Employee {employee_name} is done with tasks"
        f"({len(completed_tasks)}/{len(todos)}):"
    )
    for task in completed_tasks:
        print("\t", task.get("title"))
