"""
Task Model
Represents a single task with ID, title, description, and completion status.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    """
    Represents a task in the todo application with zero-padded ID, title, description, and completion status.

    Attributes:
        id: Zero-padded numeric identifier assigned automatically to each task (e.g., "001", "002", "003")
        title: Title of the task provided by the user
        description: Description of the task provided by the user
        completed: Boolean indicating whether the task is complete (true) or incomplete (false)
    """

    id: str  # Zero-padded numeric ID (e.g., "001", "002", "003")
    title: str
    description: str
    completed: bool = False

    def __post_init__(self):
        """Validate the task after initialization."""
        if not isinstance(self.id, str) or not self.id.strip():
            raise ValueError("Task ID must be a non-empty string in zero-padded format")

        if not isinstance(self.title, str) or not self.title.strip():
            raise ValueError("Task title must be a non-empty string")

        if not isinstance(self.description, str):
            raise ValueError("Task description must be a string")

        if not isinstance(self.completed, bool):
            raise ValueError("Task completed status must be a boolean")