import json
import os
from datetime import datetime

# File paths
TASKS_FILE = "tasks.json"
DELETED_TASKS_FILE = "deleted_tasks.json"


def get_current_time():
    """Return the current time as a formatted string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def load_tasks():
    """Load tasks from the JSON file, or return an empty list if file doesn't exist."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    """Save the list of tasks to the JSON file."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def save_deleted_task(task):
    """Save a deleted task with a deletion timestamp to a separate JSON file."""
    task["deleted_at"] = get_current_time()

    if os.path.exists(DELETED_TASKS_FILE):
        with open(DELETED_TASKS_FILE, "r") as file:
            deleted = json.load(file)
    else:
        deleted = []

    deleted.append(task)

    with open(DELETED_TASKS_FILE, "w") as file:
        json.dump(deleted, file, indent=4)


def add_task(tasks):
    """Prompt the user to add a new task and save it."""
    task_text = input("Enter your task here: ").strip()
    if not task_text:
        print("Task cannot be empty.\n")
        return

    task = {
        "description": task_text,
        "created_at": get_current_time()
    }

    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task_text}' added to the list.\n")


def list_tasks(tasks):
    """Display the list of current tasks."""
    if not tasks:
        print("There are no tasks.\n")
    else:
        print("\nCurrent Tasks:")
        print("----------------")
        for index, task in enumerate(tasks):
            print(f"Task #{index}: {task['description']} (added at {task['created_at']})")
        print("")


def remove_task(tasks):
    """Prompt the user to remove a task by index, and log it as deleted."""
    if not tasks:
        print("No tasks to remove.\n")
        return

    list_tasks(tasks)

    try:
        task_index = int(input("Enter task number to delete: "))
        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            save_tasks(tasks)
            save_deleted_task(removed_task)
            print(f"Task '{removed_task['description']}' has been removed.\n")
        else:
            print(f"Task #{task_index} was not found.\n")
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")


def main():
    """Main loop of the To-Do List App."""
    print("Welcome to the To-Do List App :)")
    tasks = load_tasks()

    while True:
        print("Please select one of the following options:")
        print("------------------------------------------")
        print("1. Add New Task")
        print("2. Delete a Task")
        print("3. Check All Tasks")
        print("4. Quit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            list_tasks(tasks)
        elif choice == "4":
            print("Goodbye :)")
            break
        else:
            print("Invalid input. Please try again.\n")


if __name__ == "__main__":
    main()

 
