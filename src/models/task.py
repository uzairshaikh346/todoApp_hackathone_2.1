"""
Task data model for the CLI Todo application.
"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    """
    Represents a single task in the todo list.
    
    Attributes:
        id: Unique identifier for the task, starting from 1
        title: The task description/title provided by the user
        completed: Whether the task has been completed (True/False)
    """
    id: int
    title: str
    completed: bool = False

    def __post_init__(self):
        """Validate the task attributes after initialization."""
        if not isinstance(self.id, int) or self.id <= 0:
            raise ValueError(f"Task ID must be a positive integer, got {self.id}")
        
        if not isinstance(self.title, str) or not self.title.strip():
            raise ValueError(f"Task title must be a non-empty string, got {self.title}")
        
        if not isinstance(self.completed, bool):
            raise ValueError(f"Task completed status must be a boolean, got {self.completed}")