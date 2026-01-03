# Data Model: Todo CLI Application

## Task Entity

### Fields
- **id** (integer): Unique numeric identifier assigned automatically to each task
- **title** (string): Title of the task provided by the user
- **description** (string): Description of the task provided by the user
- **completed** (boolean): Status indicating whether the task is complete (true) or incomplete (false)

### Relationships
- No relationships with other entities (standalone entity)

### Validation Rules
- id: Must be unique, auto-generated, positive integer
- title: Must be provided (not empty), string type
- description: Optional, string type
- completed: Boolean value, defaults to false when task is created

### State Transitions
- New task: completed = false
- Mark complete: completed = true
- Mark incomplete: completed = false

## In-Memory Storage Structure

### Data Structure
- **tasks** (dictionary): Dictionary keyed by task ID containing Task objects
  - Key: task ID (integer)
  - Value: Task object with {id, title, description, completed}

### Operations
- Add: Insert new task object into dictionary with unique ID as key
- Retrieve: Access task object by ID key
- Update: Modify fields of existing task object in dictionary
- Delete: Remove task object from dictionary by ID key
- List: Iterate through all values in the dictionary