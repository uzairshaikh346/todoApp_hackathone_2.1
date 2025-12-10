"""Data model for a Todo task.

According to the constitution, each task should have:
- Title: required, max 100 characters
- Description: optional, max 500 characters
- Auto-generated unique ID
- Status: defaults to "incomplete"
"""
from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class Task:
    """Represents a single todo task."""
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False
    created_at: datetime = None

    def __post_init__(self):
        """Validate the task after initialization."""
        if len(self.title) > 100:
            msg = f"Title exceeds maximum length of 100 characters: {len(self.title)}"
            raise ValueError(msg)

        if self.description and len(self.description) > 500:
            msg = f"Description exceeds maximum length of 500 characters: {len(self.description)}"
            raise ValueError(msg)

        if self.created_at is None:
            self.created_at = datetime.now()

    def __str__(self) -> str:
        """String representation of the task."""
        status = "✓" if self.completed else "☐"
        return f"[{status}] {self.id}: {self.title}"

