"""
Integration tests for the delete command in the CLI Todo application.
"""
import sys
import io
from contextlib import redirect_stdout, redirect_stderr
import pytest
from src.services.todo_service import TodoService
from src.ui.cli import TodoCLI


def test_delete_command_integration():
    """Test that the delete command works through the CLI interface."""
    service = TodoService()
    cli = TodoCLI(service)
    
    # Add a task first
    task = service.add_task("Task to delete")
    
    # Verify the task exists
    assert service.get_task_by_id(task.id) is not None
    
    # Capture stdout
    captured_output = io.StringIO()
    
    # Delete the task
    with redirect_stdout(captured_output):
        cli.delete_task(task.id)
    
    # Check that the output is correct
    output = captured_output.getvalue().strip()
    assert output == f"Task {task.id} removed."
    
    # Verify the task is no longer in the service
    assert service.get_task_by_id(task.id) is None


def test_delete_command_invalid_id():
    """Test that the delete command handles invalid IDs correctly."""
    service = TodoService()
    cli = TodoCLI(service)
    
    # Capture stderr
    captured_error = io.StringIO()
    
    # Try to delete a task with an invalid ID
    with redirect_stderr(captured_error):
        cli.delete_task(999)
    
    # Check that the error message is correct
    error_output = captured_error.getvalue().strip()
    assert "Error:" in error_output
    assert "not found" in error_output