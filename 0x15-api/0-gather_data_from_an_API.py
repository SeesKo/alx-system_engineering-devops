#!/usr/bin/python3
"""
Script to fetch and display TODO list progress
for a given employee using an API.
"""
import requests
import sys


if __name__ == "__main__":
    # Getting employee ID from the command line argument
    ID = int(sys.argv[1])

    # Fetching employee information
    user_url = f"https://jsonplaceholder.typicode.com/users/{ID}"
    user_data = requests.get(user_url).json()

    # Fetching employee's 'TODO' list
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={ID}"
    todos_data = requests.get(todos_url).json()

    # List of completed tasks
    completed_tasks = [
        task['title']
        for task in todos_data
        if task['completed']
    ]

    # Getting employee's name
    employee_name = user_data.get("name")

    # Displaying the required output
    print(
        f"Employee {employee_name} is done with tasks "
        f"({len(completed_tasks)}/{len(todos_data)}):"
    )
    for task in completed_tasks:
        print(f"\t {task}")
