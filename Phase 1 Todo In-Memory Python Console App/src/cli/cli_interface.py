"""
CLI Interface Handler
Handles command parsing and user interaction for the todo application.
"""

import re
from typing import List, Optional
from services.task_manager import TaskManager


class CLIInterface:
    """
    Handles command-line interface interactions for the todo application.
    """

    def __init__(self, task_manager: TaskManager):
        """
        Initialize the CLI interface.

        Args:
            task_manager: TaskManager instance to handle task operations
        """
        self.task_manager = task_manager
        self.running = True

    def run(self):
        """
        Start the main application loop.
        """
        while self.running:
            try:
                command_input = input("todo> ").strip()
                if not command_input:
                    continue

                self.process_command(command_input)
            except KeyboardInterrupt:
                print("\nExiting...")
                break
            except EOFError:
                print("\nExiting...")
                break

    def process_command(self, command_input: str):
        """
        Parse and execute a command from user input.

        Args:
            command_input: Raw command string from user
        """
        # Split command and arguments, handling quoted strings
        parts = self.parse_command(command_input)
        if not parts:
            return

        command = parts[0].lower()

        # Route command to appropriate handler
        if command == "add":
            self.handle_add(parts[1:])
        elif command == "view":
            self.handle_view()
        elif command == "update":
            self.handle_update(parts[1:])
        elif command in ["complete", "done"]:
            self.handle_complete(parts[1:])
        elif command == "incomplete":
            self.handle_incomplete(parts[1:])
        elif command in ["delete", "del"]:
            self.handle_delete(parts[1:])
        elif command == "help":
            self.handle_help()
        elif command in ["quit", "exit", "q"]:
            self.handle_quit()
        else:
            print(f"Unknown command: {command}. Type 'help' for available commands.")

    def parse_command(self, command_input: str) -> List[str]:
        """
        Parse command input, handling quoted strings as single arguments.

        Args:
            command_input: Raw command string

        Returns:
            List of command parts (command + arguments)
        """
        # This regex handles quoted strings and normal words
        pattern = r'"([^"]*)"|\'([^\']*)\'|(\S+)'
        matches = re.findall(pattern, command_input)
        # Each match is a tuple of 3 elements, only one will be non-empty
        parts = [match[0] or match[1] or match[2] for match in matches]
        return parts

    def handle_add(self, args: List[str]):
        """
        Handle the 'add' command to add a new task.

        Args:
            args: List of arguments [title, description]
        """
        if len(args) < 1:
            print("Usage: add \"title\" [\"description\"]")
            return

        title = args[0]
        description = args[1] if len(args) > 1 else ""

        try:
            task = self.task_manager.add_task(title, description)
            print(f"Task added with ID: {task.id}")
        except ValueError as e:
            print(f"Error: {e}")

    def handle_view(self, args: Optional[List[str]] = None):
        """
        Handle the 'view' command to display all tasks.

        Args:
            args: Optional arguments (not used)
        """
        tasks = self.task_manager.get_all_tasks()

        if not tasks:
            print("No tasks found.")
            return

        print("ID  | Title                | Description          | Status")
        print("--- | -------------------- | -------------------- | ------")
        for task in tasks:
            status = "Complete" if task.completed else "Incomplete"
            # Truncate long titles and descriptions for display
            title = task.title[:18] + "..." if len(task.title) > 18 else task.title
            desc = task.description[:18] + "..." if len(task.description) > 18 else task.description
            print(f"{task.id:<3} | {title:<20} | {desc:<20} | {status}")

    def handle_update(self, args: List[str]):
        """
        Handle the 'update' command to update a task.

        Args:
            args: List of arguments [id, title, description]
        """
        if len(args) < 2:
            print("Usage: update <id> \"new_title\" [\"new_description\"]")
            return

        try:
            task_id = int(args[0])
        except ValueError:
            print("Error: Task ID must be a number")
            return

        new_title = args[1] if len(args) > 1 else None
        new_description = args[2] if len(args) > 2 else None

        try:
            result = self.task_manager.update_task(task_id, new_title, new_description)
            if result:
                print(f"Task {task_id} updated successfully")
            else:
                print(f"Error: Task with ID {task_id} not found")
        except ValueError as e:
            print(f"Error: {e}")

    def handle_complete(self, args: List[str]):
        """
        Handle the 'complete' command to mark a task as complete.

        Args:
            args: List of arguments [id]
        """
        if len(args) < 1:
            print("Usage: complete <id>")
            return

        try:
            task_id = int(args[0])
            task = self.task_manager.mark_task_complete(task_id)
            if task:
                print(f"Task {task_id} marked as complete")
            else:
                print(f"Error: Task with ID {task_id} not found")
        except ValueError:
            print("Error: Task ID must be a number")

    def handle_incomplete(self, args: List[str]):
        """
        Handle the 'incomplete' command to mark a task as incomplete.

        Args:
            args: List of arguments [id]
        """
        if len(args) < 1:
            print("Usage: incomplete <id>")
            return

        try:
            task_id = int(args[0])
            task = self.task_manager.mark_task_incomplete(task_id)
            if task:
                print(f"Task {task_id} marked as incomplete")
            else:
                print(f"Error: Task with ID {task_id} not found")
        except ValueError:
            print("Error: Task ID must be a number")

    def handle_delete(self, args: List[str]):
        """
        Handle the 'delete' command to delete a task.

        Args:
            args: List of arguments [id]
        """
        if len(args) < 1:
            print("Usage: delete <id>")
            return

        try:
            task_id = int(args[0])
            success = self.task_manager.delete_task(task_id)
            if success:
                print(f"Task {task_id} deleted successfully")
            else:
                print(f"Error: Task with ID {task_id} not found")
        except ValueError:
            print("Error: Task ID must be a number")

    def handle_help(self, args: Optional[List[str]] = None):
        """
        Handle the 'help' command to display available commands.

        Args:
            args: Optional arguments (not used)
        """
        print("\nAvailable commands:")
        print("  add \"title\" [\"description\"]    - Add a new task")
        print("  view                          - View all tasks")
        print("  update <id> \"title\" [\"desc\"] - Update a task")
        print("  complete <id>                 - Mark task as complete")
        print("  incomplete <id>               - Mark task as incomplete")
        print("  delete <id>                   - Delete a task")
        print("  help                          - Show this help message")
        print("  quit/exit/q                   - Exit the application\n")

    def handle_quit(self, args: Optional[List[str]] = None):
        """
        Handle the 'quit' command to exit the application.

        Args:
            args: Optional arguments (not used)
        """
        self.running = False
        print("Goodbye!")