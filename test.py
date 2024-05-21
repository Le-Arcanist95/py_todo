# Import modules
import unittest
from unittest.mock import patch, mock_open
import os

# Import functions from todo.py
from todo import load_todos, save_todos, add_todo, view_todos, delete_todo, TODO_FILE

# Create Test Class
class TestTodoList(unittest.TestCase):

    # Define set-up function
    def setUp(self):
        self.todos = ['Task 1', 'Task 2', 'Task 3']
        # Mock opening to simulate operations
        self.mock_open = mock_open(read_data='\n'.join(self.todos) + '\n')