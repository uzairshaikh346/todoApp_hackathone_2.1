"""User interface for the todo application.

Implements the CLI interface that connects user commands to the task service.
"""
from typing import Optional
from src.services.task_service import TaskService


class TodoCLI:
    """Command-line interface for the todo application."""

    def __init__(self, task_service: TaskService):
        """Initialize the CLI with a task service."""
        self.task_service = task_service

    def add_task(self, title: str, description: Optional[str] = None) -> str:
        """Add a new task."""
        try:
            task = self.task_service.add_task(title, description)
            return f"Task added successfully! ID: {task.id}, Title: {task.title}"
        except ValueError as e:
            return f"Error adding task: {str(e)}"

    def list_tasks(self) -> str:
        """List all tasks."""
        tasks = self.task_service.get_all_tasks()

        if not tasks:
            return "No tasks found."

        result = "\nAll Tasks:"
        for task in tasks:
            status = "✓" if task.completed else "☐"
            result += f"\n  [{status}] ID: {task.id} - {task.title}"
            if task.description:
                result += f"\n      Description: {task.description}"
        return result

    def update_task(
        self, task_id: int, title: Optional[str] = None, description: Optional[str] = None
    ) -> str:
        """Update a task."""
        try:
            if self.task_service.update_task(task_id, title, description):
                return f"Task {task_id} updated successfully!"
            return f"Task {task_id} not found!"
        except ValueError as e:
            return f"Error updating task: {str(e)}"

    def delete_task(self, task_id: int) -> str:
        """Delete a task."""
        if self.task_service.delete_task(task_id):
            return f"Task {task_id} deleted successfully!"
        return f"Task {task_id} not found!"

    def toggle_task(self, task_id: int) -> str:
        """Toggle task completion status."""
        if self.task_service.toggle_task_completion(task_id):
            task = self.task_service.get_task_by_id(task_id)
            status = "completed" if task.completed else "incomplete"
            return f"Task {task_id} marked as {status}!"
        return f"Task {task_id} not found!"

    def show_help(self) -> str:
        """Show help information."""
        return """
Available commands:
  add <title> [description]     - Add a new task
  list, ls                     - List all tasks
  update <id> [title] [desc]   - Update a task
  delete <id>                  - Delete a task
  toggle <id>                  - Toggle task completion status
  help, h                      - Show this help message
  quit, exit, q                - Exit the application
        """.strip()