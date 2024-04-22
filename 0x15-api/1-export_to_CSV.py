#!/usr/bin/python3
"""
Script to fetch and export employee TODO list data to a CSV file.
"""
import csv
import requests
import sys


if __name__ == "__main__":
    # Get the employee ID from the command line argument
    ID = int(sys.argv[1])

    # Fetch the employee information
    user_url = f"https://jsonplaceholder.typicode.com/users/{ID}"
    user_data = requests.get(user_url).json()

    # Fetch the employee's 'TODO' list
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={ID}"
    todos_data = requests.get(todos_url).json()

    # Get the employee's name
    employee_username = user_data.get("username")

    # Define the CSV filename based on the employee ID
    csv_filename = f"{ID}.csv"

    # Open a CSV file for writing
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        # Create a CSV writer object
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        # Write the employee's 'TODO' data to the CSV
        for task in todos_data:
            csv_writer.writerow([
                ID, employee_username, str(task['completed']),
                task['title']
            ])
