# Allow users to add, view, delete, and save items
# Store items in list
# List should be saved to file and loaded on application start

import os

TODO_FILE = 'todo.txt'

# Add
def add_todo(todos):
    with open(TODO_FILE, 'w') as file:
        for todo in todos:
            file.write(todo + '\n')

# View

# Delete

# Save

# Load

# Create Interface