"""
Integration tests for the update command in the CLI Todo application.
"""
import sys
import io
from contextlib import redirect_stdout, redirect_stderr
import pytest
from src.services.todo_service import TodoService
from src.ui.cli import TodoCLI


def test_update_command_integration():
    """Test that the update command works through the CLI interface."""
    service = TodoService()
    cli = TodoCLI(service)
    
    # Add a task first
    task = service.add_task("Original task title")
    
    # Capture stdout
    captured_output = io.StringIO()
    
    # Update the task
    with redirect_stdout(captured_output):
        cli.update_task(task.id, "Updated task title")
    
    # Check that the output is correct
    output = captured_output.getvalue().strip()
    assert output == f"Task {task.id} updated."
    
    # Verify the task title has been updated
    updated_task = service.get_task_by_id(task.id)
    assert updated_task is not None
    assert updated_task.title == "Updated task title"


def test_update_command_invalid_id():
    """Test that the update command handles invalid IDs correctly."""
    service = TodoService()
    cli = TodoCLI(service)
    
    # Capture stderr
    captured_error = io.StringIO()
    
    # Try to update a task with an invalid ID
    with redirect_stderr(captured_error):
        cli.update_task(999, "New title")
    
    # Check that the error message is correct
    error_output = captured_error.getvalue().strip()
    assert "Error:" in error_output
    assert "not found" in error_output


def test_update_command_empty_title():
    """Test that the update command handles empty titles correctly."""
    service = TodoService()
    cli = TodoCLI(service)
    
    # Add a task first
    task = service.add_task("Original task title")
    
    # Capture stderr
    captured_error = io.StringIO()
    
    # Try to update with an empty title
    with redirect_stderr(captured_error):
        cli.update_task(task.id, "")
    
    # Check that the error message is correct
    error_output = captured_error.getvalue().strip()
    assert "Error:" in error_output