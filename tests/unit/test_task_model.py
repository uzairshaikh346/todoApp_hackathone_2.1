"""Unit tests for the Task model."""
import pytest
from src.models.task import Task


def test_task_creation():
    """Test basic task creation."""
    task = Task(id=1, title="Test task")

    assert task.id == 1
    assert task.title == "Test task"
    assert task.description is None
    assert task.completed is False
    assert task.created_at is not None


def test_task_with_description():
    """Test task creation with description."""
    task = Task(id=1, title="Test task", description="This is a test description")

    assert task.id == 1
    assert task.title == "Test task"
    assert task.description == "This is a test description"
    assert task.completed is False


def test_task_completion_toggle():
    """Test task completion status."""
    task = Task(id=1, title="Test task")

    assert task.completed is False

    task.completed = True
    assert task.completed is True

    task.completed = False
    assert task.completed is False


def test_task_string_representation():
    """Test string representation of task."""
    task = Task(id=1, title="Test task")

    # Initially incomplete
    assert str(task) == "[☐] 1: Test task"

    # When completed
    task.completed = True
    assert str(task) == "[✓] 1: Test task"


def test_task_title_length_validation():
    """Test that task title exceeds maximum length."""
    long_title = "x" * 101  # 101 characters, exceeding the 100 character limit

    with pytest.raises(ValueError, match="Title exceeds maximum length of 100 characters"):
        Task(id=1, title=long_title)


def test_task_description_length_validation():
    """Test that task description exceeds maximum length."""
    long_description = "x" * 501  # 501 characters, exceeding the 500 character limit

    with pytest.raises(ValueError, match="Description exceeds maximum length of 500 characters"):
        Task(id=1, title="Test", description=long_description)


def test_task_title_at_limit():
    """Test that task title at exactly 100 characters is valid."""
    title_at_limit = "x" * 100  # Exactly 100 characters

    task = Task(id=1, title=title_at_limit)
    assert task.title == title_at_limit


def test_task_description_at_limit():
    """Test that task description at exactly 500 characters is valid."""
    description_at_limit = "x" * 500  # Exactly 500 characters

    task = Task(id=1, title="Test", description=description_at_limit)
    assert task.description == description_at_limit


if __name__ == "__main__":
    pytest.main([__file__])