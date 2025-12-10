"""Task management service.

Implements the business logic for task operations according to the constitution:
- Add Task (FR-001)
- View Tasks (FR-002)
- Update Task (FR-003)
- Delete Task (FR-004)
- Toggle Completion (FR-005)
"""
from typing import List, Optional
from src.models.task import Task


class TaskService:
    """Service class for managing tasks."""

    def __init__(self):
        """Initialize the task service with an empty task list."""
        self._tasks: List[Task] = []
        self._next_id = 1

    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        """Add a new task with the given title and optional description.

        Args:
            title: Required title (max 100 characters)
            description: Optional description (max 500 characters)

        Returns:
            The newly created Task object

        Raises:
            ValueError: If title or description exceed length limits
        """
        # Create a new task with auto-generated ID
        task = Task(
            id=self._next_id,
            title=title,
            description=description,
            completed=False  # Defaults to incomplete
        )

        # Add to our internal list
        self._tasks.append(task)

        # Increment the ID counter for the next task
        self._next_id += 1

        return task

    def get_all_tasks(self) -> List[Task]:
        """Get all tasks in creation order (newest first).

        Returns:
            List of all tasks, newest first
        """
        # Return tasks in reverse order (newest first)
        return self._tasks[::-1]

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """Get a task by its ID.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            The task if found, None otherwise
        """
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(
        self, task_id: int, title: Optional[str] = None, description: Optional[str] = None
    ) -> bool:
        """Update a task's title and/or description by ID.

        Args:
            task_id: The ID of the task to update
            title: New title (optional)
            description: New description (optional)

        Returns:
            True if task was found and updated, False otherwise
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        # Update title if provided
        if title is not None:
            # Validate the new title length
            if len(title) > 100:
                msg = f"Title exceeds maximum length of 100 characters: {len(title)}"
                raise ValueError(msg)
            task.title = title

        # Update description if provided
        if description is not None:
            # Validate the new description length
            if len(description) > 500:
                msg = f"Description exceeds maximum length of 500 characters: {len(description)}"
                raise ValueError(msg)
            task.description = description

        return True

    def delete_task(self, task_id: int) -> bool:
        """Delete a task by ID.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if task was found and deleted, False otherwise
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        self._tasks.remove(task)
        return True

    def toggle_task_completion(self, task_id: int) -> bool:
        """Toggle a task's completion status by ID.

        Args:
            task_id: The ID of the task to toggle

        Returns:
            True if task was found and toggled, False otherwise
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        task.completed = not task.completed
        return True

    def get_task_count(self) -> int:
        """Get the total number of tasks.

        Returns:
            The number of tasks
        """
        return len(self._tasks)