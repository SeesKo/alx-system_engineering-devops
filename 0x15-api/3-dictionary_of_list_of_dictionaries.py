#!/usr/bin/python3
"""
Script to fetch TODO list of all employees
and export it to a single JSON file.
"""
import requests
import json


if __name__ == "__main__":
    # Define the URLs for users and todos
    USERS_URL = "https://jsonplaceholder.typicode.com/users"
    TODOS_URL = "https://jsonplaceholder.typicode.com/todos"

    # Get all users
    users_response = requests.get(USERS_URL)
    users = users_response.json()

    # Get all todos
    todos_response = requests.get(TODOS_URL)
    todos = todos_response.json()

    # Group tasks by user ID
    all_tasks = {}

    for todo in todos:
        user_id = todo["userId"]
        if user_id not in all_tasks:
            all_tasks[user_id] = []
        all_tasks[user_id].append({
            "username": next(
                user["username"] for user in users if user["id"] == user_id
            ),
            "task": todo["title"],
            "completed": todo["completed"]
        })

    # Export to JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file)
