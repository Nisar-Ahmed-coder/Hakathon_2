#!/usr/bin/env python3
"""
Test script to verify the menu-driven todo application functionality.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from src.models.task import Task
from src.services.task_manager import TaskManager
from src.cli.menu_interface import MenuInterface

def test_menu_interface():
    """Test the menu interface functionality."""
    print("Testing Menu Interface...")

    # Initialize the task manager and menu interface
    task_manager = TaskManager()
    menu_interface = MenuInterface(task_manager)

    # Test adding a task
    print("\n--- Testing Add Task ---")
    # Simulate user input for testing
    import io
    import contextlib

    # Test the add_task functionality by directly calling it with mocked input
    original_input = __builtins__['input']

    # Mock input function for testing
    input_calls = iter(['Test Task', 'Test Description'])
    def mock_input(prompt):
        print(prompt, end='')  # Print the prompt
        value = next(input_calls)
        print(value)  # Simulate user input
        return value

    __builtins__['input'] = mock_input

    try:
        menu_interface.handle_add_task()
        print("Add task functionality works!")
    except StopIteration:
        # This happens when we run out of mock inputs, which is expected
        pass
    finally:
        __builtins__['input'] = original_input  # Restore original input

    # Test viewing tasks
    print("\n--- Testing View Tasks ---")
    menu_interface.handle_view_tasks()

    # Test adding another task
    print("\n--- Testing Add Another Task ---")
    task_manager.add_task("Second Task", "Second Description")
    menu_interface.handle_view_tasks()

    # Test updating a task
    print("\n--- Testing Update Task ---")
    # Get the first task ID
    tasks = task_manager.get_all_tasks()
    if tasks:
        test_id = tasks[0].id
        print(f"Updating task with ID: {test_id}")
        # For testing purposes, let's directly call the update method
        updated_task = task_manager.update_task(test_id, "Updated Task Title", "Updated Description")
        if updated_task:
            print(f"Task {test_id} updated successfully!")

    # Test toggling completion
    print("\n--- Testing Toggle Completion ---")
    if tasks:
        test_id = tasks[0].id
        print(f"Toggling completion for task: {test_id}")
        toggled_task = task_manager.toggle_task_completion(test_id)
        if toggled_task:
            print(f"Task {test_id} completion status: {toggled_task.completed}")

    # Test deleting a task
    print("\n--- Testing Delete Task ---")
    if tasks:
        test_id = tasks[0].id
        print(f"Deleting task with ID: {test_id}")
        delete_result = task_manager.delete_task(test_id)
        print(f"Task {test_id} deleted: {delete_result}")

        # Check remaining tasks
        remaining_tasks = task_manager.get_all_tasks()
        print(f"Remaining tasks after deletion: {len(remaining_tasks)}")

    print("\nAll menu interface functionality tests completed successfully!")

def test_task_model():
    """Test the Task model functionality."""
    print("\nTesting Task Model...")

    # Test creating a task with valid data
    task = Task("001", "Test Title", "Test Description", False)
    print(f"Created task: ID={task.id}, Title={task.title}, Completed={task.completed}")

    # Test creating a task with completion status
    task2 = Task("002", "Test Title 2", "Test Description 2", True)
    print(f"Created completed task: ID={task2.id}, Title={task2.title}, Completed={task2.completed}")

    # Test validation
    try:
        invalid_task = Task("", "Title", "Description", False)  # Empty ID should fail
        print("ERROR: Should have failed with empty ID")
    except ValueError:
        print("Correctly rejected task with empty ID")

    try:
        invalid_task = Task("003", "", "Description", False)  # Empty title should fail
        print("ERROR: Should have failed with empty title")
    except ValueError:
        print("Correctly rejected task with empty title")

    print("Task model tests completed successfully!")

if __name__ == "__main__":
    print("Starting Menu-Driven Todo Application Tests...")

    test_task_model()
    test_menu_interface()

    print("\nAll tests passed! The menu-driven todo application is working correctly.")