# CLI Command Contracts: Simple CLI Todo App

## Command Structure
All commands follow the pattern: `python main.py [command] [arguments]`

## Available Commands

### Add Task
- **Command**: `add`
- **Arguments**: `"task_title"`
- **Description**: Creates a new task with the given title
- **Example**: `python main.py add "Buy groceries"`
- **Success Response**: "Task [ID] added."
- **Error Response**: "Error: [error message]" to stderr

### List Tasks
- **Command**: `list`
- **Arguments**: None
- **Description**: Displays all tasks with their completion status
- **Example**: `python main.py list`
- **Success Response**: 
  ```
  1. [ ] Buy groceries
  2. [X] Complete project
  ```
- **Error Response**: "Error: [error message]" to stderr

### Complete Task
- **Command**: `complete`
- **Arguments**: `task_id`
- **Description**: Marks the specified task as completed
- **Example**: `python main.py complete 1`
- **Success Response**: "Task [ID] marked completed."
- **Error Response**: "Error: [error message]" to stderr

### Update Task
- **Command**: `update`
- **Arguments**: `task_id` `"new_title"`
- **Description**: Updates the title of the specified task
- **Example**: `python main.py update 1 "Buy groceries and cook dinner"`
- **Success Response**: "Task [ID] updated."
- **Error Response**: "Error: [error message]" to stderr

### Delete Task
- **Command**: `delete`
- **Arguments**: `task_id`
- **Description**: Removes the specified task from the list
- **Example**: `python main.py delete 1`
- **Success Response**: "Task [ID] removed."
- **Error Response**: "Error: [error message]" to stderr