# Allow users to add, view, delete, and save items
# Store items in list
# List should be saved to file and loaded on application start

import os

TODO_FILE = 'todo.txt'

# Load
def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            todos = [line.strip() for line in file.readlines()]
    else:
        todos = []
    return todos

# View
def view_todos():
    if todos:
        print("\nTodo List:")
        for idx, todo in enumerate(todos, start=1):
            print(f"{idx}. {todo}")
    else:
        print("\nYour todo list is empty.")

# Add
def add_todo(todos):
    with open(TODO_FILE, 'w') as file:
        for todo in todos:
            file.write(todo + '\n')
# Save


# Delete


# Create Interface