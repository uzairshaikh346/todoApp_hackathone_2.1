"""Integration tests for the complete todo application."""
import sys
from io import StringIO
from unittest.mock import patch
from src.services.task_service import TaskService
from src.ui.todo_cli import TodoCLI


def test_complete_workflow():
    """Test the complete workflow of adding, listing, updating, toggling, and deleting tasks."""
    # Initialize service and CLI
    task_service = TaskService()
    cli = TodoCLI(task_service)

    # 1. Add tasks
    result1 = cli.add_task("First task", "This is the first task")
    assert "Task added successfully!" in result1
    assert "ID: 1" in result1

    result2 = cli.add_task("Second task", "This is the second task")
    assert "Task added successfully!" in result2
    assert "ID: 2" in result2

    # 2. List tasks (should show newest first)
    list_result = cli.list_tasks()
    assert "No tasks found." not in list_result
    assert "First task" in list_result
    assert "Second task" in list_result
    # Second task should appear first (newest first)
    second_pos = list_result.find("Second task")
    first_pos = list_result.find("First task")
    assert second_pos < first_pos, "Newer tasks should appear first"

    # 3. Update a task
    update_result = cli.update_task(1, "Updated first task")
    assert "Task 1 updated successfully!" in update_result

    # Verify the update worked
    updated_list = cli.list_tasks()
    assert "Updated first task" in updated_list

    # 4. Toggle task completion
    toggle_result = cli.toggle_task(1)
    assert "Task 1 marked as completed!" in toggle_result

    # Verify the toggle worked
    toggled_list = cli.list_tasks()
    assert "[✓] ID: 1" in toggled_list

    # 5. Delete a task
    delete_result = cli.delete_task(2)
    assert "Task 2 deleted successfully!" in delete_result

    # Verify the deletion worked
    final_list = cli.list_tasks()
    assert "Second task" not in final_list
    assert "Updated first task" in final_list

    print("✓ Complete workflow test passed!")


def test_error_handling():
    """Test error handling for invalid operations."""
    task_service = TaskService()
    cli = TodoCLI(task_service)

    # Try to update a non-existent task
    update_result = cli.update_task(999, "New title")
    assert "Task 999 not found!" in update_result

    # Try to delete a non-existent task
    delete_result = cli.delete_task(999)
    assert "Task 999 not found!" in delete_result

    # Try to toggle a non-existent task
    toggle_result = cli.toggle_task(999)
    assert "Task 999 not found!" in toggle_result

    # Try to add a task with too long title
    long_title = "x" * 101
    error_result = cli.add_task(long_title)
    assert "Error adding task:" in error_result

    print("✓ Error handling test passed!")


def test_command_parsing_simulation():
    """Simulate command parsing to verify CLI functionality."""
    task_service = TaskService()
    cli = TodoCLI(task_service)

    # Simulate adding tasks
    add_result = cli.add_task("Sample task", "Sample description")
    assert "Task added successfully!" in add_result

    # Test various commands
    help_result = cli.show_help()
    assert "Available commands:" in help_result
    assert "add" in help_result
    assert "list" in help_result
    assert "update" in help_result
    assert "delete" in help_result
    assert "toggle" in help_result

    print("✓ Command parsing simulation test passed!")


if __name__ == "__main__":
    test_complete_workflow()
    test_error_handling()
    test_command_parsing_simulation()
    print("\n✓ All integration tests passed!")
    sys.exit(0)