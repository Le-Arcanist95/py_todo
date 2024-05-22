# todo.py

import os

TODO_FILE = 'todo.txt'

def load_todos():
    """
    Load todos from the TODO_FILE.
    If the file exists, read the todos line by line and strip newline characters.
    If the file does not exist, return an empty list.
    """
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            todos = [line.strip() for line in file.readlines()]
    else:
        todos = []
    return todos

def save_todos(todos):
    """
    Save todos to the TODO_FILE.
    Overwrite the file with the current list of todos, each followed by a newline.
    """
    with open(TODO_FILE, 'w') as file:
        for todo in todos:
            file.write(todo + '\n')

def add_todo():
    """
    Add a new todo item to the list.
    Prompt the user to enter a new todo, append it to the list, and save the updated list.
    """
    todo = input("Enter a new todo item: ")
    todos.append(todo)
    save_todos(todos)
    print(f'Added: {todo}')

def view_todos():
    """
    Display the current list of todos.
    If the list is not empty, print each todo with its index.
    If the list is empty, print a message indicating that the list is empty.
    """
    if todos:
        print("\nTodo List:")
        for idx, todo in enumerate(todos, start=1):
            print(f"{idx}. {todo}")
    else:
        print("\nYour todo list is empty.")

def delete_todo():
    """
    Delete a todo item from the list.
    Display the list of todos, prompt the user to enter the number of the todo to delete,
    remove the specified todo from the list, and save the updated list.
    Handle invalid input gracefully.
    """
    view_todos()
    try:
        todo_index = int(input("Enter the number of the todo to delete: ")) - 1
        if 0 <= todo_index < len(todos):
            removed = todos.pop(todo_index)
            save_todos(todos)
            print(f"Deleted: {removed}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def edit_todo():
    """
    Edit an existing todo item in the list.
    Display the list of todos, prompt the user to enter the number of the todo to edit,
    prompt the user to enter the new todo item, update the specified todo, and save the updated list.
    Handle invalid input gracefully.
    """
    view_todos()
    try:
        todo_index = int(input("Enter the number of the todo to edit: ")) - 1
        if 0 <= todo_index < len(todos):
            new_todo = input("Enter the new todo item: ")
            todos[todo_index] = new_todo
            save_todos(todos)
            print(f"Updated: {new_todo}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def show_menu():
    """
    Display the menu options to the user.
    """
    print("\nTodo List Menu")
    print("1. View todos")
    print("2. Add a todo")
    print("3. Delete a todo")
    print("4. Edit a todo")
    print("5. Exit")

def main():
    """
    Main function to run the todo application.
    Load the existing todos, display the menu, and handle user input to perform various actions.
    """
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
            edit_todo()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()