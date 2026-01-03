# Menu Command Contracts: Menu-Driven Todo CLI Application

## Menu Interface Definition

### Main Menu Display
- **Interface**: Displays centered title between separator lines followed by numbered options
- **Options**: 1. Add Task, 2. View Tasks, 3. Update Task, 4. Delete Task, 5. Mark Complete / Incomplete, 6. Exit
- **Input**: User enters number (1-6)
- **Output**: Executes corresponding action or shows error for invalid input

### Option 1: Add Task Command
- **Input**: Prompts for title first, then description
- **Output**: Success message with zero-padded task ID or error message
- **Behavior**: Creates a new task with auto-generated zero-padded ID and sets completion status to false

### Option 2: View Tasks Command
- **Input**: None
- **Output**: List of all tasks showing zero-padded ID, title, description, and completion status in tabular format
- **Behavior**: Displays all tasks in a readable format with visual separators

### Option 3: Update Task Command
- **Input**: Zero-padded task ID, new title (optional), new description (optional)
- **Output**: Success confirmation or error message
- **Behavior**: Updates the title and/or description of the specified task

### Option 4: Delete Task Command
- **Input**: Zero-padded task ID
- **Output**: Success confirmation or error message
- **Behavior**: Removes the specified task from storage

### Option 5: Mark Complete/Incomplete Command
- **Input**: Zero-padded task ID
- **Output**: Success confirmation or error message
- **Behavior**: Toggles the completion status of the specified task

### Option 6: Exit Command
- **Input**: None
- **Output**: None
- **Behavior**: Terminates the application