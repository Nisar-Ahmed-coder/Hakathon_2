from typing import Optional
from src.services.task_manager import TaskManager


class MenuInterface:
    """
    Handles the menu-driven command-line interface logic for the todo application.
    Provides methods for displaying menus and processing user selections.
    """

    def __init__(self, task_manager: TaskManager):
        """
        Initialize the menu interface with a task manager.

        Args:
            task_manager: The TaskManager instance to use for task operations
        """
        self.task_manager = task_manager

    def display_menu(self):
        """Display the main menu with centered title and separator lines."""
        print("\n" + "=" * 60)
        print("                    TODO APPLICATION                    ")
        print("  1. Add Task                                           ")
        print("  2. View Tasks                                         ")
        print("  3. Update Task                                        ")
        print("  4. Delete Task                                        ")
        print("  5. Mark Complete / Incomplete                         ")
        print("  6. Exit                                               ")
        print("=" * 60)

    def get_user_choice(self) -> str:
        """
        Get the user's menu choice.

        Returns:
            The user's choice as a string
        """
        return input("Enter your choice (1-6): ").strip()

    def handle_add_task(self):
        """Handle the add task functionality."""
        print("\n--- Add Task ---")
        title = input("Enter task title: ").strip()

        if not title:
            print("Error: Task title cannot be empty.")
            return

        description = input("Enter task description: ").strip()
        try:
            task = self.task_manager.add_task(title, description)
            print(f"Task added with ID: {task.id}")
        except ValueError as e:
            print(f"Error adding task: {e}")

    def handle_view_tasks(self):
        """Handle the view tasks functionality."""
        print("\n--- View Tasks ---")
        tasks = self.task_manager.get_all_tasks()

        if not tasks:
            print("No tasks found.")
            return

        # Print table header with separators
        print(f"{'ID':<5} | {'Title':<20} | {'Description':<20} | {'Status':<12}")
        print("-" * 60)

        # Print each task
        for task in tasks:
            status = "Complete" if task.completed else "Incomplete"
            print(f"{task.id:<5} | {task.title[:18]:<20} | {task.description[:18]:<20} | {status:<12}")

    def handle_update_task(self):
        """Handle the update task functionality."""
        print("\n--- Update Task ---")
        task_id = input("Enter task ID: ").strip()

        # Validate that the task exists
        existing_task = self.task_manager.get_task(task_id)
        if not existing_task:
            print(f"Error: Task with ID '{task_id}' not found.")
            return

        # Get new values (or keep existing if empty input)
        print(f"Current title: {existing_task.title}")
        new_title = input("Enter new title (or press Enter to keep current): ").strip()
        if new_title == "":
            new_title = None

        print(f"Current description: {existing_task.description}")
        new_description = input("Enter new description (or press Enter to keep current): ").strip()
        if new_description == "":
            new_description = None

        # Update the task
        try:
            updated_task = self.task_manager.update_task(task_id, new_title, new_description)
            if updated_task:
                print(f"Task {task_id} updated successfully.")
            else:
                print(f"Error: Failed to update task {task_id}.")
        except ValueError as e:
            print(f"Error updating task: {e}")

    def handle_delete_task(self):
        """Handle the delete task functionality."""
        print("\n--- Delete Task ---")
        task_id = input("Enter task ID: ").strip()

        success = self.task_manager.delete_task(task_id)
        if success:
            print(f"Task {task_id} deleted successfully.")
        else:
            print(f"Error: Task with ID '{task_id}' not found.")

    def handle_toggle_completion(self):
        """Handle the mark complete/incomplete functionality."""
        print("\n--- Mark Complete / Incomplete ---")
        task_id = input("Enter task ID: ").strip()

        # Validate that the task exists
        existing_task = self.task_manager.get_task(task_id)
        if not existing_task:
            print(f"Error: Task with ID '{task_id}' not found.")
            return

        # Toggle the completion status
        updated_task = self.task_manager.toggle_task_completion(task_id)
        if updated_task:
            status = "complete" if updated_task.completed else "incomplete"
            print(f"Task {task_id} marked as {status}.")
        else:
            print(f"Error: Failed to update task {task_id}.")

    def handle_exit(self):
        """Handle the exit functionality."""
        print("Goodbye!")
        return True  # Return True to indicate exit