import os
TODO_FILE = 'todo.txt'

# Load
def load_todos():
    # Check if 'TODO_FILE' exists
    if os.path.exists(TODO_FILE):
        # If success, open file in read mode, read, strip, and store items in 'todos' list.
        with open(TODO_FILE, 'r') as file:
            todos = [line.strip() for line in file.readlines()]
    else:
        # If failure, initialize empty 'todos' list.
        todos = []
    return todos

# View
def view_todos():
    # If 'todos' has content
    if todos:
        # Print todo items with index number
        print("\nTodo List:")
        for idx, todo in enumerate(todos, start=1):
            print(f"{idx}. {todo}")
    # If 'todos' is empty
    else:
        # Inform user of empty list
        print("\nYour todo list is empty.")

# Add
def add_todo():
    # Prompt user to add new todo item.
    todo = input("Enter a new todo item: ")
    # Add new item to 'todos' list.
    todos.append(todo)
    # Update 'todos' list
    save_todos(todos)
    print(f'Added: {todo}')

# Save
def save_todos(todos):
    # Open 'TODO_FILE' in write mode.
    with open(TODO_FILE, 'w') as file:
        for todo in todos:
            # Add item and create new line for next item.
            file.write(todo + '\n')

# Delete
def delete_todo():
    # Display list of current todo items.
    view_todos()
    try:
        # Prompt user to select item for deletion and convert selection to zero-indexed format
        todo_index = int(input("Enter the number to the todo to delete: ")) - 1
        # Check if choice is valid
        if 0 <= todo_index < len(todos):
            # Remove item
            removed = todos.pop(todo_index)
            # Re-create 'todos' list
            saved_todos(todos) # type: ignore
            print(f"Deleted: {removed}")
        else:
            print("Invalid number.")
    except ValueError:
        # Throw error on invalid choice.
        print("Please enter a valid number.")

# Create Interface

# Initial load and user interface
def show_menu():
    print("\nTodo List Menu")
    print("1. View todos")
    print("2. Add a todo")
    print("3. Delete a todo")
    print("4. Exit")

# Application entry point
def main():
    # Declare global variables
    global todos
    # Load 'todos'
    todos = load_todos()

    # Enter infinite loop for display and user input handling
    while True:
        show_menu()
        # Prompt user for choice
        choice = input("Choose an option: ")

        # Handle input choice
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
            # Throw error on invalid number
            print("Invalid choice. Please select a valid option.")

# Check for direct, not module, usage and start application
if __name__ == "__main__":
    main()