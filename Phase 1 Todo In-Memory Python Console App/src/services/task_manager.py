"""
Task Manager Service
Handles in-memory storage and operations for tasks.
"""

from typing import Dict, List, Optional
from src.models.task import Task


class TaskManager:
    """
    Manages tasks in memory with zero-padded ID support.
    Stores tasks in a dictionary keyed by task ID containing Task objects.
    """

    def __init__(self):
        """Initialize the task manager with an empty dictionary and counter."""
        self.tasks: Dict[str, Task] = {}
        self._next_id = 1

    def _generate_zero_padded_id(self) -> str:
        """Generate the next zero-padded ID in the sequence (001, 002, etc.)."""
        id_str = f"{self._next_id:03d}"  # Format as 3-digit zero-padded string
        self._next_id += 1
        return id_str

    def add_task(self, title: str, description: str) -> Task:
        """
        Add a new task with auto-generated zero-padded ID and set completion status to false.

        Args:
            title: The task title
            description: The task description

        Returns:
            The created Task object with zero-padded ID
        """
        task_id = self._generate_zero_padded_id()
        task = Task(id=task_id, title=title, description=description, completed=False)
        self.tasks[task_id] = task
        return task

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks in the system.

        Returns:
            List of all Task objects
        """
        return list(self.tasks.values())

    def get_task(self, task_id: str) -> Optional[Task]:
        """
        Retrieve a task by its zero-padded ID.

        Args:
            task_id: The zero-padded task ID (e.g., "001", "002")

        Returns:
            The Task object if found, None otherwise
        """
        return self.tasks.get(task_id)

    def update_task(self, task_id: str, title: Optional[str] = None, description: Optional[str] = None) -> Optional[Task]:
        """
        Update the title and/or description of an existing task.

        Args:
            task_id: The zero-padded task ID to update
            title: New title (optional)
            description: New description (optional)

        Returns:
            The updated Task object if successful, None if task not found
        """
        if task_id not in self.tasks:
            return None

        task = self.tasks[task_id]

        if title is not None:
            task.title = title
        if description is not None:
            task.description = description

        return task

    def delete_task(self, task_id: str) -> bool:
        """
        Remove a task from storage by its zero-padded ID.

        Args:
            task_id: The zero-padded task ID to delete

        Returns:
            True if the task was successfully deleted, False if not found
        """
        if task_id not in self.tasks:
            return False

        del self.tasks[task_id]
        return True

    def toggle_task_completion(self, task_id: str) -> Optional[Task]:
        """
        Toggle the completion status of a task by its zero-padded ID.

        Args:
            task_id: The zero-padded task ID to toggle

        Returns:
            The updated Task object if successful, None if task not found
        """
        if task_id not in self.tasks:
            return None

        task = self.tasks[task_id]
        task.completed = not task.completed
        return task

    def mark_task_complete(self, task_id: str) -> Optional[Task]:
        """
        Mark a task as complete by its zero-padded ID.

        Args:
            task_id: The zero-padded task ID to mark complete

        Returns:
            The updated Task object if successful, None if task not found
        """
        if task_id not in self.tasks:
            return None

        task = self.tasks[task_id]
        task.completed = True
        return task

    def mark_task_incomplete(self, task_id: str) -> Optional[Task]:
        """
        Mark a task as incomplete by its zero-padded ID.

        Args:
            task_id: The zero-padded task ID to mark incomplete

        Returns:
            The updated Task object if successful, None if task not found
        """
        if task_id not in self.tasks:
            return None

        task = self.tasks[task_id]
        task.completed = False
        return task