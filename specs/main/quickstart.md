# Quickstart Guide: Simple CLI Todo App

## Prerequisites
- Python 3.13+ installed on your system
- Basic command line knowledge

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd todo-app
   ```

2. Install dependencies (using UV as specified in the constitution):
   ```bash
   uv install
   ```

## Usage

### Adding a Task
```bash
python main.py add "Task description"
```
Example:
```bash
python main.py add "Buy groceries"
```

### Listing All Tasks
```bash
python main.py list
```
Example output:
```
1. [ ] Buy groceries
2. [X] Complete project
```

### Marking a Task as Complete
```bash
python main.py complete <task_id>
```
Example:
```bash
python main.py complete 1
```

### Updating a Task
```bash
python main.py update <task_id> "New task description"
```
Example:
```bash
python main.py update 1 "Buy groceries and cook dinner"
```

### Deleting a Task
```bash
python main.py delete <task_id>
```
Example:
```bash
python main.py delete 1
```

## Development

### Running Tests
```bash
python -m pytest tests/
```

### Running the Application in Development Mode
```bash
python main.py [command] [arguments]
```

## Project Structure
- `src/models/task.py` - Task data model
- `src/services/todo_service.py` - Business logic for todo operations
- `src/ui/cli.py` - CLI interface and user interaction
- `main.py` - Entry point for the application
- `tests/` - Test files