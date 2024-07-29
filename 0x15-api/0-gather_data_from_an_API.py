#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

def main(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/"
    
    # Fetch employee data
    user_response = requests.get(f"{base_url}users/{employee_id}")
    if user_response.status_code != 200:
        print(f"Error: Unable to fetch user data for ID {employee_id}")
        return
    
    user = user_response.json()
    user_name = user.get("name")
    
    # Fetch TODO list
    todos_response = requests.get(f"{base_url}todos", params={"userId": employee_id})
    if todos_response.status_code != 200:
        print(f"Error: Unable to fetch TODO list for ID {employee_id}")
        return
    
    todos = todos_response.json()

    # Calculate completed tasks
    completed = [t.get("title") for t in todos if t.get("completed")]

    # Print result
    print(f"Employee {user_name} is done with tasks({len(completed)}/{len(todos)}):")
    for task in completed:
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
