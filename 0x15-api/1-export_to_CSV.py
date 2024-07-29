#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""

import csv
import requests
import sys


def export_todo_list(user_id):
    """Exports to-do list information for a given employee ID to CSV format."""
    url = "https://jsonplaceholder.typicode.com/"
    
    user_response = requests.get(url + f"users/{user_id}")
    if user_response.status_code != 200:
        print(f"Error fetching user information for ID {user_id}: "
              f"{user_response.text}")
        return

    user = user_response.json()
    username = user.get("username")

    params = {"userId": user_id}
    todos_response = requests.get(url + "todos", params=params)
    if todos_response.status_code != 200:
        print(f"Error fetching to-do list for user ID {user_id}: "
              f"{todos_response.text}")
        return

    todos = todos_response.json()

    with open(f"{user_id}.csv", "w", newline="") as csvfile:
        fieldnames = ["User ID", "Username", "Completed", "Title"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for todo in todos:
            writer.writerow({
                "User ID": user_id,
                "Username": username,
                "Completed": todo.get("completed"),
                "Title": todo.get("title")
            })


if __name__ == "__main__":
    user_id = sys.argv[1]
    export_todo_list(user_id)
    