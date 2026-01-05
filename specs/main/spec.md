# Simple CLI Todo App — Specification

This specification defines the behavior, features, and requirements for a simple Command Line Interface (CLI) based Todo application. The goal is to build a minimal in-memory todo tool that runs in the terminal and manages tasks without external dependencies.

## 1. Overview
The Todo app must provide basic task management through a CLI. Tasks are stored only in memory (no database) and last only during runtime.

## 2. Goals

- Create an in-memory todo list
- Support essential CLI operations
- Follow clean code standards and modular architecture
- Prepare for future extension

## 3. Features

### 3.1 Add Task
Add a new task with a title.
Usage example:

```
todo add "Task Title"
```

### 3.2 View Task List
Display all tasks with status (completed or not).
Usage example:

```
todo list
```

### 3.3 Mark Task Complete
Mark a specific task as completed.
Usage example:

```
todo complete <task_id>
```

### 3.4 Delete Task
Remove a specific task from the list.
Usage example:

```
todo delete <task_id>
```

### 3.5 Update Task
Modify the title of an existing task.
Usage example:

```
todo update <task_id> "New Task Title"
```

## 4. Task Model
Each task must include the following fields:

- id: unique integer
- title: string
- completed: boolean (True or False)

Example in memory representation:

```
{
  id: 1,
  title: "Buy groceries",
  completed: False
}
```

## 5. Task ID Rules

- Task IDs start at 1
- Each new task gets the next available ID
- IDs remain unique during the program session

## 6. Directory Structure

```
/src
  /models
  /services
  /ui
main.py
pyproject.toml
README.md
/tests
.gitignore
```

## 7. Technical Requirements

- Python version must be 3.13+
- No external dependencies (standard library only)
- Code must follow PEP 8
- Use type hints for all functions and methods

## 8. CLI Commands Overview

| Command | Description |
|--------|-------------|
| `todo add "title"` | Create a new task |
| `todo list` | Show all tasks |
| `todo complete <id>` | Mark a task as completed |
| `todo delete <id>` | Remove a task |
| `todo update <id> "new"` | Rename a task |

## 9. Acceptance Criteria

- CLI commands work as defined
- Tasks remain in memory during execution
- App handles invalid input gracefully
- User receives clear feedback on operations
- Code is structured (models, services, ui)

## 10. Example Interactions

Add a task:

```
> todo add "Learn Python"
Task 1 added.
```

View tasks:

```
> todo list
1. [ ] Learn Python
```

Mark complete:

```
> todo complete 1
Task 1 marked completed.
```

Update a task:

```
> todo update 1 "Learn Advanced Python"
Task 1 updated.
```

Delete a task:

```
> todo delete 1
Task 1 removed.
```

## 11. Testing Strategy

- Add multiple tasks and verify list output
- Mark tasks complete and verify status
- Update task titles and confirm changes
- Delete tasks and ensure removal
- Handle invalid commands or IDs

## 12. Summary
This specification defines a minimal CLI Todo application with essential CRUD features. It ensures a clean, modular architecture, no external dependencies, and simple command-based interaction for managing tasks in memory.