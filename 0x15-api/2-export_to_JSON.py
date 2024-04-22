#!/usr/bin/python3
"""
Script to fetch employee TODO list and export it to a JSON file.
"""
import json
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_data = requests.get(user_url).json()
    todos_url = (
        f"https://jsonplaceholder.typicode.com/todos"
        f"?userId={employee_id}"
    )
    todos_data = requests.get(todos_url).json()

    employee_username = user_data.get("username")

    # Create a list of task information formatted as required
    employee_tasks = [
        {
            "task": task.get("title", "Untitled Task"),
            "completed": task.get("completed", False),
            "username": employee_username,
        }
        for task in todos_data
    ]

    # Create the JSON data with the specified format
    json_data = {str(employee_id): employee_tasks}

    # Define the JSON file name based on the employee ID
    json_filename = f"{employee_id}.json"

    # Write the JSON data to the file
    with open(json_filename, 'w', encoding='utf-8') as jsonfile:
        json.dump(json_data, jsonfile)
