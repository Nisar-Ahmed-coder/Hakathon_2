# Quickstart Guide: Menu-Driven Todo CLI Application

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

## Available Menu Options
Once the application is running, you will see a numbered menu:

```
==================== TODO APPLICATION ====================
  1. Add Task
  2. View Tasks
  3. Update Task
  4. Delete Task
  5. Mark Complete / Incomplete
  6. Exit
==========================================================
Enter your choice (1-6):
```

Select an option by entering the corresponding number:

### Option 1: Add Task
- Prompts for task title first
- Then prompts for task description
- Task is added only after both inputs are provided
- Assigns a zero-padded numeric ID (e.g., 001, 002)

### Option 2: View Tasks
- Displays all tasks in a tabular format
- Shows zero-padded ID, title, and status
- Uses visual separators for clarity

### Option 3: Update Task
- Prompts for the zero-padded task ID
- Allows updating title and/or description
- Confirms update in console

### Option 4: Delete Task
- Prompts for the zero-padded task ID
- Removes task from memory
- Confirms deletion in console

### Option 5: Mark Complete / Incomplete
- Prompts for the zero-padded task ID
- Toggles completion status
- Prints status confirmation

### Option 6: Exit
- Exits the application

## Example Usage
```
==================== TODO APPLICATION ====================
  1. Add Task
  2. View Tasks
  3. Update Task
  4. Delete Task
  5. Mark Complete / Incomplete
  6. Exit
==========================================================
Enter your choice (1-6): 1
Enter task title: Buy groceries
Enter task description: Milk, bread, eggs
Task added with ID: 001

==================== TODO APPLICATION ====================
  1. Add Task
  2. View Tasks
  3. Update Task
  4. Delete Task
  5. Mark Complete / Incomplete
  6. Exit
==========================================================
Enter your choice (1-6): 2
ID  | Title           | Description      | Status
----|-----------------|------------------|--------
001 | Buy groceries   | Milk, bread, eggs| Incomplete

==================== TODO APPLICATION ====================
  1. Add Task
  2. View Tasks
  3. Update Task
  4. Delete Task
  5. Mark Complete / Incomplete
  6. Exit
==========================================================
Enter your choice (1-6): 5
Enter task ID: 001
Task 001 marked as complete

==================== TODO APPLICATION ====================
  1. Add Task
  2. View Tasks
  3. Update Task
  4. Delete Task
  5. Mark Complete / Incomplete
  6. Exit
==========================================================
Enter your choice (1-6): 2
ID  | Title           | Description      | Status
----|-----------------|------------------|--------
001 | Buy groceries   | Milk, bread, eggs| Complete

==================== TODO APPLICATION ====================
  1. Add Task
  2. View Tasks
  3. Update Task
  4. Delete Task
  5. Mark Complete / Incomplete
  6. Exit
==========================================================
Enter your choice (1-6): 6
Goodbye!
```

## In-Memory Behavior
Note that all tasks are stored only in memory and will be lost when the application is restarted.