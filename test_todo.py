import unittest
from unittest.mock import patch, mock_open

# Import the functions from the todo module
from todo import load_todos, save_todos, add_todo, view_todos, delete_todo, edit_todo, TODO_FILE

class TestTodoList(unittest.TestCase):

    def setUp(self):
        """
        Set up the test environment before each test method is run.
        Initializes a sample list of todos and sets up a mock for file operations.
        """
        self.todos = ['Task 1', 'Task 2', 'Task 3']
        # Mocking open to simulate file operations with sample data
        self.mock_open = mock_open(read_data='\n'.join(self.todos) + '\n')

    @patch('todo.open', new_callable=mock_open, read_data='Task 1\nTask 2\nTask 3\n')
    @patch('os.path.exists', return_value=True)
    def test_load_todos(self, mock_exists, mock_open):
        """
        Test the load_todos function to ensure it correctly loads todos from a file.
        Mocks os.path.exists to simulate the presence of the TODO_FILE.
        Mocks open to simulate reading from the file.
        """
        # Call the function to load todos
        todos = load_todos()
        # Check that the loaded todos match the sample data
        self.assertEqual(todos, self.todos)
        # Ensure the file was opened in read mode
        mock_open.assert_called_once_with(TODO_FILE, 'r')
        # Ensure os.path.exists was called to check the file's existence
        mock_exists.assert_called_once_with(TODO_FILE)

    @patch('todo.open', new_callable=mock_open)
    def test_save_todos(self, mock_open):
        """
        Test the save_todos function to ensure it correctly saves todos to a file.
        Uses mock_open to simulate file writing operations.
        """
        # Call the function to save todos
        save_todos(self.todos)
        # Ensure the file was opened in write mode
        mock_open.assert_called_once_with(TODO_FILE, 'w')
        # Check that the correct data was written to the file
        mock_open().write.assert_called_with('Task 1\nTask 2\nTask 3\n')

    @patch('todo.input', return_value='New Task')
    @patch('todo.save_todos')
    def test_add_todo(self, mock_save_todos, mock_input):
        """
        Test the add_todo function to ensure it correctly adds a new todo item.
        Mocks input to simulate user input and save_todos to avoid actual file operations.
        """
        # Mock print to avoid output during tests
        with patch('builtins.print'):
            # Call the function to add a new todo
            add_todo()
        # Check that the new todo item is in the list
        self.assertIn('New Task', todos)
        # Ensure the save_todos function was called to save the updated list
        mock_save_todos.assert_called_once_with(todos)

    @patch('builtins.print')
    def test_view_todos(self, mock_print):
        """
        Test the view_todos function to ensure it correctly displays the list of todos.
        Mocks print to capture and verify the output.
        """
        # Use the sample list of todos for this test
        with patch('todo.todos', self.todos):
            # Call the function to view todos
            view_todos()
        # Check that print was called to display the todos
        mock_print.assert_called()

    @patch('todo.input', return_value='1')
    @patch('todo.save_todos')
    @patch('builtins.print')
    def test_delete_todo_valid(self, mock_print, mock_save_todos, mock_input):
        """
        Test the delete_todo function with a valid index to ensure it correctly deletes the specified todo item.
        Mocks input to simulate user input, save_todos to avoid actual file operations, and print to capture output.
        """
        # Use a copy of the sample list of todos for this test
        with patch('todo.todos', self.todos.copy()):
            # Call the function to delete a todo
            delete_todo()
        # Check that the specified todo item was removed
        self.assertNotIn('Task 1', todos)
        # Ensure the save_todos function was called to save the updated list
        mock_save_todos.assert_called_once_with(todos)
        # Check that print was called to display confirmation
        mock_print.assert_called()

    @patch('todo.input', return_value='10')
    @patch('builtins.print')
    def test_delete_todo_invalid(self, mock_print, mock_input):
        """
        Test the delete_todo function with an invalid index to ensure it handles out-of-range input correctly.
        Mocks input to simulate user input and print to capture output.
        """
        # Use a copy of the sample list of todos for this test
        with patch('todo.todos', self.todos.copy()):
            # Call the function to delete a todo
            delete_todo()
        # Check that the list length remains unchanged
        self.assertEqual(len(todos), len(self.todos))
        # Check that an error message was printed
        mock_print.assert_called_with('Invalid number.')

    @patch('todo.input', side_effect=ValueError)
    @patch('builtins.print')
    def test_delete_todo_invalid_input(self, mock_print, mock_input):
        """
        Test the delete_todo function with invalid (non-integer) input to ensure it handles input errors correctly.
        Mocks input to simulate user input and print to capture output.
        """
        # Use a copy of the sample list of todos for this test
        with patch('todo.todos', self.todos.copy()):
            # Call the function to delete a todo
            delete_todo()
        # Check that the list length remains unchanged
        self.assertEqual(len(todos), len(self.todos))
        # Check that an error message was printed
        mock_print.assert_called_with('Please enter a valid number.')

    @patch('todo.open', new_callable=mock_open)
    @patch('os.path.exists', return_value=False)
    def test_load_todos_empty_file(self, mock_exists, mock_open):
        """
        Test the load_todos function when the TODO_FILE does not exist.
        Ensures it returns an empty list.
        Mocks:
        - os.path.exists: Simulates the file not existing by returning False.
        - open: Simulates the open function to avoid actual file operations.
        Assertions:
        - Checks that the load_todos function returns an empty list.
        - Verifies that os.path.exists was called once with the TODO_FILE.
        """
        # Call the load_todos function, which should return an empty list
        todos = load_todos()
        # Assert that the returned list is empty
        self.assertEqual(todos, [])
        # Verify that os.path.exists was called once with the correct file path
        mock_exists.assert_called_once_with(TODO_FILE)

    @patch('todo.open', new_callable=mock_open, read_data='')
    @patch('os.path.exists', return_value=True)
    def test_load_todos_no_content(self, mock_exists, mock_open):
        """
        Test the load_todos function when the TODO_FILE exists but is empty.
        Ensures it returns an empty list.
        Mocks:
        - os.path.exists: Simulates the file existing by returning True.
        - open: Simulates the open function to read an empty file.
        Assertions:
        - Checks that the load_todos function returns an empty list.
        - Verifies that the open function was called once in read mode with the TODO_FILE.
        - Verifies that os.path.exists was called once with the TODO_FILE.
        """
        # Call the load_todos function, which should return an empty list
        todos = load_todos()
        # Assert that the returned list is empty
        self.assertEqual(todos, [])
        # Verify that the open function was called once with the correct file path in read mode
        mock_open.assert_called_once_with(TODO_FILE, 'r')
        # Verify that os.path.exists was called once with the correct file path
        mock_exists.assert_called_once_with(TODO_FILE)

    @patch('todo.input', return_value='New Task')
    @patch('todo.save_todos')
    def test_add_todo_empty_list(self, mock_save_todos, mock_input):
        """
        Test the add_todo function to ensure it correctly adds a new todo item to an empty list.
        Mocks input to simulate user input and save_todos to avoid actual file operations.
        Mocks:
        - input: Simulates user input by returning 'New Task'.
        - save_todos: Mocks the save_todos function to avoid actual file operations.
        Assertions:
        - Checks that the new todo item is added to the list.
        - Verifies that the save_todos function was called once with the updated list.
        """
        global todos
        # Initialize todos as an empty list for this test
        todos = []
        # Mock print to avoid output during tests
        with patch('builtins.print'):
            # Call the add_todo function, which should add 'New Task' to the list
            add_todo()
        # Assert that 'New Task' is in the todos list
        self.assertIn('New Task', todos)
        # Verify that the save_todos function was called once with the updated list
        mock_save_todos.assert_called_once_with(todos)

    @patch('todo.input', return_value='0')
    @patch('builtins.print')
    def test_delete_todo_zero_index(self, mock_print, mock_input):
        """
        Test the delete_todo function with a zero index to ensure it handles the input correctly.
        Mocks input to simulate user input and print to capture output.
        Mocks:
        - input: Simulates user input by returning '0'.
        - print: Mocks the print function to capture and verify output.
        Assertions:
        - Checks that the todos list remains unchanged.
        - Verifies that an 'Invalid number.' message is printed.
        """
        # Use a copy of the sample list of todos for this test
        with patch('todo.todos', self.todos.copy()):
            # Call the delete_todo function with a zero index
            delete_todo()
        # Assert that the todos list remains unchanged
        self.assertEqual(len(todos), len(self.todos))
        # Verify that 'Invalid number.' was printed
        mock_print.assert_called_with('Invalid number.')

    @patch('todo.input', return_value='1')
    @patch('todo.save_todos')
    @patch('builtins.print')
    def test_delete_todo_last_item(self, mock_print, mock_save_todos, mock_input):
        """
        Test the delete_todo function to ensure it correctly deletes the last todo item.
        Mocks input to simulate user input, save_todos to avoid actual file operations, and print to capture output.
        Mocks:
        - input: Simulates user input by returning '1'.
        - save_todos: Mocks the save_todos function to avoid actual file operations.
        - print: Mocks the print function to capture and verify output.
        Assertions:
        - Checks that the last todo item is removed from the list.
        - Verifies that the save_todos function was called once with the updated list.
        - Verifies that a confirmation message was printed.
        """
        # Use a single-item list for this test
        with patch('todo.todos', ['Task 1']):
            # Call the delete_todo function to delete the last item
            delete_todo()
        # Assert that 'Task 1' is not in the todos list
        self.assertNotIn('Task 1', todos)
        # Verify that the save_todos function was called once with the updated list
        mock_save_todos.assert_called_once_with(todos)
        # Verify that a confirmation message was printed
        mock_print.assert_called()

    @patch('todo.input', return_value='1')
    @patch('todo.input', return_value='Updated Task')
    @patch('todo.save_todos')
    @patch('builtins.print')
    def test_edit_todo_valid(self, mock_print, mock_save_todos, mock_input):
        """
        Test the edit_todo function to ensure it correctly updates the specified todo item.
        Mocks input to simulate user input for selecting and updating the todo item,
        save_todos to avoid actual file operations, and print to capture output.
        Mocks:
        - input: Simulates user input for selecting and updating the todo item.
        - save_todos: Mocks the save_todos function to avoid actual file operations.
        - print: Mocks the print function to capture and verify output.
        Assertions:
        - Checks that the specified todo item is updated in the list.
        - Verifies that the save_todos function was called once with the updated list.
        - Verifies that a confirmation message was printed.
        """
        # Use a copy of the sample list of todos for this test
        with patch('todo.todos', self.todos.copy()):
            # Call the edit_todo function to update the first item
            edit_todo()
        # Assert that 'Updated Task' is in the todos list
        self.assertIn('Updated Task', todos)
        # Assert that 'Task 1' is not in the todos list
        self.assertNotIn('Task 1', todos)
        # Verify that the save_todos function was called once with the updated list
        mock_save_todos.assert_called_once_with(todos)
        # Verify that a confirmation message was printed
        mock_print.assert_called()

    @patch('todo.input', return_value='10')
    @patch('builtins.print')
    def test_edit_todo_invalid(self, mock_print, mock_input):
        """
        Test the edit_todo function with an invalid index to ensure it handles out-of-range input correctly.
        Mocks input to simulate user input and print to capture output.
        Mocks:
        - input: Simulates user input by returning '10'.
        - print: Mocks the print function to capture and verify output.
        Assertions:
        - Checks that the todos list remains unchanged.
        - Verifies that an 'Invalid number.' message is printed.
        """
        # Use a copy of the sample list of todos for this test
        with patch('todo.todos', self.todos.copy()):
            # Call the edit_todo function with an invalid index
            edit_todo()
        # Assert that the todos list remains unchanged
        self.assertEqual(len(todos), len(self.todos))
        # Verify that 'Invalid number.' was printed
        mock_print.assert_called_with('Invalid number.')

    @patch('todo.input', side_effect=ValueError)
    @patch('builtins.print')
    def test_edit_todo_invalid_input(self, mock_print, mock_input):
        """
        Test the edit_todo function with invalid (non-integer) input to ensure it handles input errors correctly.
        Mocks input to simulate user input and print to capture output.
        Mocks:
        - input: Simulates invalid user input (non-integer) by raising a ValueError.
        - print: Mocks the print function to capture and verify output.
        Assertions:
        - Checks that the todos list remains unchanged.
        - Verifies that a 'Please enter a valid number.' message is printed.
        """
        # Use a copy of the sample list of todos for this test
        with patch('todo.todos', self.todos.copy()):
            # Call the edit_todo function with invalid input
            edit_todo()
        # Assert that the todos list remains unchanged
        self.assertEqual(len(todos), len(self.todos))
        # Verify that 'Please enter a valid number.' was printed
        mock_print.assert_called_with('Please enter a valid number.')

if __name__ == '__main__':
    unittest.main()