#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""

import requests
import sys
from urllib.parse import urljoin

def main(employee_id):
    """Fetch and print the to-do list progress for the given employee ID."""
    base_url = "https://jsonplaceholder.typicode.com/"
    user_url = urljoin(base_url, f"users/{employee_id}")
    todos_url = urljoin(base_url, "todos")

    # Fetch employee data
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"Error: Unable to fetch user data for ID {employee_id}")
        return
    
    user = user_response.json()
    employee_name = user.get("name", "Unknown Employee")
    
    # Fetch TODO list
    todos_response = requests.get(todos_url, params={"userId": employee_id})
    if todos_response.status_code != 200:
        print(f"Error: Unable to fetch TODO list for ID {employee_id}")
        return
    
    todos = todos_response.json()

    # Calculate completed tasks
    completed_tasks = [task.get("title") for task in todos if task.get("completed")]
    total_tasks = len(todos)
    completed_count = len(completed_tasks)

    # Print result
    print(f"Employee {employee_name} is done with tasks({completed_count}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        main(employee_id)
    except ValueError:
        print("Error: The employee ID must be an integer.")
        sys.exit(1)
