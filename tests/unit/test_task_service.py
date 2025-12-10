"""Unit tests for the TaskService."""
import pytest
from src.services.task_service import TaskService
from src.models.task import Task


def test_task_service_initialization():
    """Test that TaskService initializes with empty task list."""
    service = TaskService()

    assert service.get_task_count() == 0
    assert service.get_all_tasks() == []


def test_add_task():
    """Test adding a task."""
    service = TaskService()

    task = service.add_task("Test task")

    assert service.get_task_count() == 1
    assert task.id == 1
    assert task.title == "Test task"
    assert task.completed is False


def test_add_task_with_description():
    """Test adding a task with description."""
    service = TaskService()

    task = service.add_task("Test task", "This is a description")

    assert service.get_task_count() == 1
    assert task.id == 1
    assert task.title == "Test task"
    assert task.description == "This is a description"


def test_get_all_tasks():
    """Test getting all tasks in creation order (newest first)."""
    service = TaskService()

    task1 = service.add_task("First task")
    task2 = service.add_task("Second task")
    task3 = service.add_task("Third task")

    tasks = service.get_all_tasks()

    # Should return tasks in reverse order (newest first)
    assert len(tasks) == 3
    assert tasks[0].id == task3.id  # Newest first
    assert tasks[1].id == task2.id
    assert tasks[2].id == task1.id  # Oldest last


def test_get_task_by_id():
    """Test getting a task by ID."""
    service = TaskService()

    task = service.add_task("Test task")

    found_task = service.get_task_by_id(task.id)
    assert found_task is not None
    assert found_task.id == task.id
    assert found_task.title == task.title

    # Test getting non-existent task
    not_found_task = service.get_task_by_id(999)
    assert not_found_task is None


def test_update_task():
    """Test updating a task."""
    service = TaskService()

    task = service.add_task("Original title", "Original description")

    # Update both title and description
    result = service.update_task(task.id, "Updated title", "Updated description")

    assert result is True
    assert task.title == "Updated title"
    assert task.description == "Updated description"

    # Test updating only title
    result = service.update_task(task.id, "Another title")
    assert result is True
    assert task.title == "Another title"
    assert task.description == "Updated description"  # Should remain unchanged

    # Test updating only description
    result = service.update_task(task.id, description="Another description")
    assert result is True
    assert task.title == "Another title"  # Should remain unchanged
    assert task.description == "Another description"


def test_update_nonexistent_task():
    """Test updating a non-existent task."""
    service = TaskService()

    result = service.update_task(999, "New title")
    assert result is False


def test_update_task_title_length_validation():
    """Test that updating task title validates length."""
    service = TaskService()
    task = service.add_task("Original title")

    long_title = "x" * 101  # 101 characters, exceeding the 100 character limit

    with pytest.raises(ValueError, match="Title exceeds maximum length of 100 characters"):
        service.update_task(task.id, long_title)


def test_update_task_description_length_validation():
    """Test that updating task description validates length."""
    service = TaskService()
    task = service.add_task("Original title")

    long_description = "x" * 501  # 501 characters, exceeding the 500 character limit

    with pytest.raises(ValueError, match="Description exceeds maximum length of 500 characters"):
        service.update_task(task.id, description=long_description)


def test_delete_task():
    """Test deleting a task."""
    service = TaskService()

    task = service.add_task("Test task")
    initial_count = service.get_task_count()

    result = service.delete_task(task.id)

    assert result is True
    assert service.get_task_count() == initial_count - 1
    assert service.get_task_by_id(task.id) is None


def test_delete_nonexistent_task():
    """Test deleting a non-existent task."""
    service = TaskService()

    result = service.delete_task(999)
    assert result is False


def test_toggle_task_completion():
    """Test toggling task completion status."""
    service = TaskService()

    task = service.add_task("Test task")
    assert task.completed is False

    # Toggle to complete
    result = service.toggle_task_completion(task.id)
    assert result is True
    assert task.completed is True

    # Toggle back to incomplete
    result = service.toggle_task_completion(task.id)
    assert result is True
    assert task.completed is False


def test_toggle_nonexistent_task():
    """Test toggling completion of a non-existent task."""
    service = TaskService()

    result = service.toggle_task_completion(999)
    assert result is False


def test_task_id_uniqueness():
    """Test that task IDs are unique."""
    service = TaskService()

    task1 = service.add_task("First task")
    task2 = service.add_task("Second task")
    task3 = service.add_task("Third task")

    ids = [task1.id, task2.id, task3.id]
    assert len(ids) == len(set(ids))  # All IDs should be unique
    assert task1.id == 1
    assert task2.id == 2
    assert task3.id == 3


def test_multiple_operations():
    """Test multiple operations in sequence."""
    service = TaskService()

    # Add multiple tasks
    task1 = service.add_task("Task 1")
    task2 = service.add_task("Task 2")
    task3 = service.add_task("Task 3")

    assert service.get_task_count() == 3

    # Update one task
    service.update_task(task2.id, "Updated Task 2")
    assert service.get_task_by_id(task2.id).title == "Updated Task 2"

    # Toggle completion
    service.toggle_task_completion(task1.id)
    assert service.get_task_by_id(task1.id).completed is True

    # Delete a task
    service.delete_task(task2.id)
    assert service.get_task_count() == 2
    assert service.get_task_by_id(task2.id) is None

    # Verify remaining tasks
    remaining_tasks = service.get_all_tasks()
    assert len(remaining_tasks) == 2


if __name__ == "__main__":
    pytest.main([__file__])