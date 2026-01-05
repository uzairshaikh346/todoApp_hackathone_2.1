"""
Todo service for the CLI Todo application.
Implements business logic for todo operations with file-based persistence.
"""
import json
from typing import List, Optional
from ..models.task import Task


class TodoService:
    """
    Service class that handles all todo operations with file-based persistence.
    """

    def __init__(self, storage_file: str = "todo_data.json"):
        """Initialize the service with file-based storage."""
        self._storage_file = storage_file
        self._tasks: List[Task] = []
        self._next_id: int = 1
        self._load_from_file()

    def _load_from_file(self):
        """Load tasks from the storage file."""
        try:
            with open(self._storage_file, 'r') as f:
                data = json.load(f)
                self._tasks = [Task(**task_data) for task_data in data['tasks']]
                self._next_id = data['next_id']
        except FileNotFoundError:
            # File doesn't exist yet, start with empty list
            self._tasks = []
            self._next_id = 1
        except (json.JSONDecodeError, KeyError, TypeError):
            # File is corrupted or has invalid format, start with empty list
            self._tasks = []
            self._next_id = 1

    def _save_to_file(self):
        """Save tasks to the storage file."""
        data = {
            'tasks': [task.__dict__ for task in self._tasks],
            'next_id': self._next_id
        }
        with open(self._storage_file, 'w') as f:
            json.dump(data, f)
    
    def add_task(self, title: str) -> Task:
        """
        Add a new task with the given title.

        Args:
            title: The title for the new task

        Returns:
            The newly created Task object

        Raises:
            ValueError: If the title is empty
        """
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")

        task = Task(id=self._next_id, title=title.strip(), completed=False)
        self._tasks.append(task)
        self._next_id += 1
        self._save_to_file()
        return task
    
    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks in the system.

        Returns:
            List of all Task objects
        """
        return self._tasks.copy()  # Return a copy to prevent external modification
    
    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Find a specific task by its ID.
        
        Args:
            task_id: The ID of the task to find
            
        Returns:
            The Task object if found, None otherwise
        """
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None
    
    def mark_task_complete(self, task_id: int) -> bool:
        """
        Mark the specified task as completed.

        Args:
            task_id: The ID of the task to mark as completed

        Returns:
            True if the task was found and updated, False otherwise
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.completed = True
            self._save_to_file()
            return True
        return False
    
    def mark_task_incomplete(self, task_id: int) -> bool:
        """
        Mark the specified task as incomplete.

        Args:
            task_id: The ID of the task to mark as incomplete

        Returns:
            True if the task was found and updated, False otherwise
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.completed = False
            self._save_to_file()
            return True
        return False
    
    def update_task(self, task_id: int, new_title: str) -> bool:
        """
        Update the title of the specified task.

        Args:
            task_id: The ID of the task to update
            new_title: The new title for the task

        Returns:
            True if the task was found and updated, False otherwise
        """
        if not new_title or not new_title.strip():
            raise ValueError("Task title cannot be empty")

        task = self.get_task_by_id(task_id)
        if task:
            task.title = new_title.strip()
            self._save_to_file()
            return True
        return False
    
    def delete_task(self, task_id: int) -> bool:
        """
        Remove the specified task from the list.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if the task was found and deleted, False otherwise
        """
        task = self.get_task_by_id(task_id)
        if task:
            self._tasks.remove(task)
            self._save_to_file()
            return True
        return False