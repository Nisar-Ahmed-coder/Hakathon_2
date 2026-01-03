# Quickstart Guide: Todo CLI Application

## Prerequisites
- Python 3.13+
- UV package manager

## Installation
1. Clone the repository
2. Install dependencies using UV: `uv sync` (or `pip install` if using standard Python)

## Running the Application
Execute the main application file from the command line:
```bash
python todo_app.py
```

## Available Commands
Once the application is running, you can use the following commands:

- `add "title" "description"` - Add a new task with title and description
- `view` - View all tasks with their ID, title, and completion status
- `update <id> "new_title" "new_description"` - Update title and/or description of a task
- `complete <id>` - Mark a task as complete
- `incomplete <id>` - Mark a task as incomplete
- `delete <id>` - Delete a task
- `help` - Show available commands
- `quit` or `exit` - Exit the application

## Example Usage
```
> add "Buy groceries" "Milk, bread, eggs"
Task added with ID: 1

> add "Finish report" "Complete the quarterly report"
Task added with ID: 2

> view
ID: 1 | Title: Buy groceries | Description: Milk, bread, eggs | Status: Incomplete
ID: 2 | Title: Finish report | Description: Complete the quarterly report | Status: Incomplete

> complete 1
Task 1 marked as complete

> view
ID: 1 | Title: Buy groceries | Description: Milk, bread, eggs | Status: Complete
ID: 2 | Title: Finish report | Description: Complete the quarterly report | Status: Incomplete

> quit
```

## In-Memory Behavior
Note that all tasks are stored only in memory and will be lost when the application is restarted.