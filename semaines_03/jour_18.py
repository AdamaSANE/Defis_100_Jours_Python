# Mini To-Do Application using JSON
import json
import os

# File for storing tasks
TASKS_FILE = 'my_tasks.json'

# Ensure the tasks file exists
if not os.path.exists(TASKS_FILE):
    with open(TASKS_FILE, 'w') as file:
        json.dump([], file)

# step 1: Load Tasks from JSON 
def load_tasks():
    with open(TASKS_FILE, 'r') as file:
        return json.load(file)
    
# step 2: Save Tasks to JSON
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=2)

# step 3: Add a New Task
def add_task(task):
    task_name = input("Enter the task name: ").strip()
    tasks = load_tasks()
    tasks.append({"Task": task_name, "Status": "Incomplete"})
    save_tasks(tasks)
    print(f'Task "{task_name}" added successfully.')

# step 4: View All Tasks
def view_tasks():
    tasks = load_tasks()
    if tasks:
        print("\n--- To-Do List ---")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task['Task']} - {task['Status']}")
    else:
        print("No tasks found.")

# step 5: update Task Status
def update_task_status():
    tasks = load_tasks()
    view_tasks()
    try:
        task_index = int(input("Enter the task number to update its status: ")) - 1
        if 0 <= task_index < len(tasks):
            new_status = input("Enter new status (Incomplete/Complete): ").strip()
            tasks[task_index]['Status'] = new_status
            save_tasks(tasks)
            print("Task status updated successfully.")
        else:
            print("Invalid task number.") 
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# step 6: Delete a Task
def delete_task():
    tasks = load_tasks()
    view_tasks()
    try:
        task_index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            save_tasks(tasks)
            print(f'Task "{removed_task["Task"]}" deleted successfully.')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Step 7: Display Menu and Handle User Choices
def display_menu():
   
    print("\n--- To-Do Application Menu ---")
    print("1. Add a new Task")
    print("2. View all Tasks")
    print("3. Update Task Status")
    print("4. Delete Task")
    print("5. Exit")

# Step 8: Main program Loop
def main(): 
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()
        if choice == '1':
            add_task(input)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            update_task_status()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")     