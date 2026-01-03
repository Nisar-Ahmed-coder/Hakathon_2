# Todo-In-Memory-Python-Console-App

A menu-driven command-line todo application with in-memory storage for tasks. The application provides a clear numbered menu interface allowing users to add, view, update, delete, and mark tasks as complete/incomplete. Tasks are stored in memory using a dictionary structure keyed by unique zero-padded auto-incrementing numeric IDs.

## Features

- Menu-driven interface with numbered options (1-6)
- Zero-padded numeric IDs (001, 002, 003, etc.)
- Add tasks with title and description
- View all tasks in tabular format
- Update existing tasks
- Delete tasks
- Mark tasks as complete/incomplete
- Clean console output with visual separators
- In-memory storage (tasks lost on restart)

## Requirements

- Python 3.13+

## Installation

1. Clone the repository
2. Navigate to the project directory

## Usage

Run the application:

```bash
python src/todo_app.py
```

## Menu Options

1. Add Task - Prompts for title first, then description
2. View Tasks - Displays all tasks in tabular format
3. Update Task - Update title/description using task ID
4. Delete Task - Remove task using task ID
5. Mark Complete/Incomplete - Toggle completion status
6. Exit - Exit the application

## Example Usage

```
============================================================
                    TODO APPLICATION
  1. Add Task
  2. View Tasks
  3. Update Task
  4. Delete Task
  5. Mark Complete / Incomplete
  6. Exit
============================================================
Enter your choice (1-6): 1

--- Add Task ---
Enter task title: Buy groceries
Enter task description: Milk, bread, eggs
Task added with ID: 001

============================================================
                    TODO APPLICATION
  1. Add Task
  2. View Tasks
  3. Update Task
  4. Delete Task
  5. Mark Complete / Incomplete
  6. Exit
============================================================
Enter your choice (1-6): 2

--- View Tasks ---
ID    | Title                | Description          | Status
------------------------------------------------------------
001   | Buy groceries        | Milk, bread, eggs    | Incomplete

============================================================
                    TODO APPLICATION
  1. Add Task
  2. View Tasks
  3. Update Task
  4. Delete Task
  5. Mark Complete / Incomplete
  6. Exit
============================================================
Enter your choice (1-6): 5
--- Mark Complete / Incomplete ---
Enter task ID: 001
Task 001 marked as complete.

============================================================
                    TODO APPLICATION
  1. Add Task
  2. View Tasks
  3. Update Task
  4. Delete Task
  5. Mark Complete / Incomplete
  6. Exit
============================================================
Enter your choice (1-6): 6
Goodbye!
Application closed.
```

## Architecture

- `src/models/task.py` - Task data model with zero-padded ID support
- `src/services/task_manager.py` - In-memory storage and operations
- `src/cli/menu_interface.py` - Menu-driven command-line interface logic
- `src/todo_app.py` - Main application entry point# Todo-In-Memory-Python-Console-App
