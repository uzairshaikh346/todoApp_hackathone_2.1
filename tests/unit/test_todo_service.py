"""
Unit tests for the TodoService to verify all functionality.
"""
import pytest
from src.models.task import Task
from src.services.todo_service import TodoService


def test_create_task():
    """Test that a task can be created with the correct attributes."""
    task = Task(id=1, title="Test task", completed=False)
    assert task.id == 1
    assert task.title == "Test task"
    assert task.completed is False


def test_create_task_with_invalid_id():
    """Test that creating a task with an invalid ID raises an error."""
    with pytest.raises(ValueError):
        Task(id=0, title="Test task", completed=False)

    with pytest.raises(ValueError):
        Task(id=-1, title="Test task", completed=False)


def test_create_task_with_invalid_title():
    """Test that creating a task with an invalid title raises an error."""
    with pytest.raises(ValueError):
        Task(id=1, title="", completed=False)

    with pytest.raises(ValueError):
        Task(id=1, title="   ", completed=False)


def test_create_task_with_invalid_completed():
    """Test that creating a task with an invalid completed status raises an error."""
    with pytest.raises(ValueError):
        Task(id=1, title="Test task", completed="invalid")


def test_add_task():
    """Test that a task can be added to the service."""
    service = TodoService()
    task = service.add_task("Test task")

    assert task.id == 1
    assert task.title == "Test task"
    assert task.completed is False

    tasks = service.get_all_tasks()
    assert len(tasks) == 1
    assert tasks[0].id == 1


def test_add_task_with_empty_title():
    """Test that adding a task with an empty title raises an error."""
    service = TodoService()

    with pytest.raises(ValueError):
        service.add_task("")

    with pytest.raises(ValueError):
        service.add_task("   ")


def test_get_all_tasks():
    """Test that all tasks can be retrieved."""
    service = TodoService()
    service.add_task("First task")
    service.add_task("Second task")

    tasks = service.get_all_tasks()
    assert len(tasks) == 2
    assert tasks[0].title == "First task"
    assert tasks[1].title == "Second task"


def test_get_task_by_id():
    """Test that a specific task can be retrieved by ID."""
    service = TodoService()
    task = service.add_task("Test task")

    retrieved_task = service.get_task_by_id(task.id)
    assert retrieved_task is not None
    assert retrieved_task.id == task.id
    assert retrieved_task.title == task.title
    assert retrieved_task.completed == task.completed

    # Test with non-existent ID
    assert service.get_task_by_id(999) is None


def test_mark_task_complete():
    """Test that a task can be marked as complete."""
    service = TodoService()
    task = service.add_task("Test task")

    # Initially task should be incomplete
    assert task.completed is False

    # Mark as complete
    success = service.mark_task_complete(task.id)
    assert success is True

    # Verify task is now complete
    updated_task = service.get_task_by_id(task.id)
    assert updated_task is not None
    assert updated_task.completed is True


def test_mark_task_incomplete():
    """Test that a task can be marked as incomplete."""
    service = TodoService()
    task = service.add_task("Test task")

    # Mark as complete first
    service.mark_task_complete(task.id)
    assert service.get_task_by_id(task.id).completed is True

    # Mark as incomplete
    success = service.mark_task_incomplete(task.id)
    assert success is True

    # Verify task is now incomplete
    updated_task = service.get_task_by_id(task.id)
    assert updated_task is not None
    assert updated_task.completed is False


def test_update_task():
    """Test that a task can be updated."""
    service = TodoService()
    task = service.add_task("Original task")

    # Update the task
    success = service.update_task(task.id, "Updated task")
    assert success is True

    # Verify the task was updated
    updated_task = service.get_task_by_id(task.id)
    assert updated_task is not None
    assert updated_task.title == "Updated task"


def test_update_task_with_empty_title():
    """Test that updating a task with an empty title raises an error."""
    service = TodoService()
    task = service.add_task("Original task")

    with pytest.raises(ValueError):
        service.update_task(task.id, "")

    with pytest.raises(ValueError):
        service.update_task(task.id, "   ")


def test_update_nonexistent_task():
    """Test that updating a non-existent task returns False."""
    service = TodoService()

    success = service.update_task(999, "New title")
    assert success is False


def test_delete_task():
    """Test that a task can be deleted."""
    service = TodoService()
    task = service.add_task("Test task")

    # Verify task exists
    assert service.get_task_by_id(task.id) is not None

    # Delete task
    success = service.delete_task(task.id)
    assert success is True

    # Verify task no longer exists
    assert service.get_task_by_id(task.id) is None


def test_delete_nonexistent_task():
    """Test that deleting a non-existent task returns False."""
    service = TodoService()

    success = service.delete_task(999)
    assert success is False