# Data Model: Simple CLI Todo App

## Task Entity

### Fields
- **id**: `int` - Unique identifier for the task, starting from 1
- **title**: `str` - The task description/title provided by the user
- **completed**: `bool` - Whether the task has been completed (True/False)

### Example Representation
```python
{
    "id": 1,
    "title": "Buy groceries",
    "completed": False
}
```

### Validation Rules
- `id` must be a positive integer
- `title` must be a non-empty string
- `completed` must be a boolean value

### State Transitions
- A task can transition from `completed=False` to `completed=True` when marked complete
- A task can transition from `completed=True` to `completed=False` when marked incomplete
- A task is created with `completed=False` by default

## Todo List Container

### Fields
- **tasks**: `List[Task]` - A list of all tasks in the system
- **next_id**: `int` - The next available ID to assign to a new task

### Operations
- Add a new task to the list
- Remove a task from the list by ID
- Update a task's properties by ID
- Retrieve all tasks
- Find a specific task by ID