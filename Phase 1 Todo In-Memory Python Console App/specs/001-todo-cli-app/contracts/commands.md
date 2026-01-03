# CLI Command Contracts: Todo CLI Application

## Command Interface Definition

### Add Task Command
- **Command**: `add "title" "description"`
- **Input**: Title (string), Description (string)
- **Output**: Success message with assigned task ID or error message
- **Behavior**: Creates a new task with auto-generated ID and sets completion status to false

### View Tasks Command
- **Command**: `view`
- **Input**: None
- **Output**: List of all tasks showing ID, title, description, and completion status
- **Behavior**: Displays all tasks in a readable format

### Update Task Command
- **Command**: `update <id> "new_title" "new_description"`
- **Input**: Task ID (integer), New Title (string), New Description (string)
- **Output**: Success confirmation or error message
- **Behavior**: Updates the title and/or description of the specified task

### Complete Task Command
- **Command**: `complete <id>`
- **Input**: Task ID (integer)
- **Output**: Success confirmation or error message
- **Behavior**: Sets the completion status of the specified task to true

### Incomplete Task Command
- **Input**: Task ID (integer)
- **Output**: Success confirmation or error message
- **Behavior**: Sets the completion status of the specified task to false

### Delete Task Command
- **Command**: `delete <id>`
- **Input**: Task ID (integer)
- **Output**: Success confirmation or error message
- **Behavior**: Removes the specified task from storage

### Help Command
- **Command**: `help`
- **Input**: None
- **Output**: List of available commands with usage instructions
- **Behavior**: Displays help information

### Quit/Exit Command
- **Command**: `quit` or `exit`
- **Input**: None
- **Output**: None
- **Behavior**: Terminates the application