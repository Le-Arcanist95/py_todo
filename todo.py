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
def save_todos(todos):
    with open(TODO_FILE, 'w') as file:
        for todo in todos:
            file.write(todo + '\n')

# Delete
def delete_todo():
    view_todos()
    try:
        todo_index = int(input("Enter the number to the todo to delete: ")) - 1
        if 0 <= todo_index < len(todos):
            removed = todos.pop(todo_index)
            saved_todos(todos) # type: ignore
            print(f"Deleted: {removed}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

# Create Interface
def show_menu():
    print("\nTodo List Menu")
    print("1. View todos")
    print("2. Add a todo")
    print("3. Delete a todo")
    print("4. Exit")

def main():
    global todos
    todos = load_todos()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            view_todos()
        elif choice == '2':
            add_todo()
        elif choice == '3':
            delete_todo()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()