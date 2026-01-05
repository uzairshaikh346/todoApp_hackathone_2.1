"""
CLI interface for the Todo application.
Handles user interaction and output formatting.
"""
from typing import Optional
from src.services.todo_service import TodoService


class TodoCLI:
    """
    CLI interface class that handles user interaction and output formatting.
    """
    
    def __init__(self, service: TodoService):
        """
        Initialize the CLI interface with a TodoService.
        
        Args:
            service: The TodoService to use for operations
        """
        self.service = service
    
    def add_task(self, title: str) -> None:
        """
        Add a new task and display confirmation.
        
        Args:
            title: The title of the task to add
        """
        try:
            task = self.service.add_task(title)
            print(f"Task {task.id} added.")
        except ValueError as e:
            print(f"Error: {e}", file=__import__('sys').stderr)
    
    def list_tasks(self) -> None:
        """
        List all tasks with their completion status.
        """
        tasks = self.service.get_all_tasks()
        if not tasks:
            print("No tasks found.")
            return
        
        for task in tasks:
            status = "X" if task.completed else " "
            print(f"{task.id}. [{status}] {task.title}")
    
    def complete_task(self, task_id: int) -> None:
        """
        Mark a task as complete and display confirmation.
        
        Args:
            task_id: The ID of the task to mark as complete
        """
        success = self.service.mark_task_complete(task_id)
        if success:
            print(f"Task {task_id} marked completed.")
        else:
            print(f"Error: Task with ID {task_id} not found.", file=__import__('sys').stderr)
    
    def update_task(self, task_id: int, new_title: str) -> None:
        """
        Update a task's title and display confirmation.
        
        Args:
            task_id: The ID of the task to update
            new_title: The new title for the task
        """
        try:
            success = self.service.update_task(task_id, new_title)
            if success:
                print(f"Task {task_id} updated.")
            else:
                print(f"Error: Task with ID {task_id} not found.", file=__import__('sys').stderr)
        except ValueError as e:
            print(f"Error: {e}", file=__import__('sys').stderr)
    
    def delete_task(self, task_id: int) -> None:
        """
        Delete a task and display confirmation.
        
        Args:
            task_id: The ID of the task to delete
        """
        success = self.service.delete_task(task_id)
        if success:
            print(f"Task {task_id} removed.")
        else:
            print(f"Error: Task with ID {task_id} not found.", file=__import__('sys').stderr)