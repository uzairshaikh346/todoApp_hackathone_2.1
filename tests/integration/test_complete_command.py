"""
Integration tests for the complete command in the CLI Todo application.
"""
import sys
import io
from contextlib import redirect_stdout, redirect_stderr
import pytest
from src.services.todo_service import TodoService
from src.ui.cli import TodoCLI


def test_complete_command_integration():
    """Test that the complete command works through the CLI interface."""
    service = TodoService()
    cli = TodoCLI(service)
    
    # Add a task first
    task = service.add_task("Task to complete")
    
    # Capture stdout
    captured_output = io.StringIO()
    
    # Complete the task
    with redirect_stdout(captured_output):
        cli.complete_task(task.id)
    
    # Check that the output is correct
    output = captured_output.getvalue().strip()
    assert output == f"Task {task.id} marked completed."
    
    # Verify the task is now complete
    updated_task = service.get_task_by_id(task.id)
    assert updated_task is not None
    assert updated_task.completed is True


def test_complete_command_invalid_id():
    """Test that the complete command handles invalid IDs correctly."""
    service = TodoService()
    cli = TodoCLI(service)
    
    # Capture stderr
    captured_error = io.StringIO()
    
    # Try to complete a task with an invalid ID
    with redirect_stderr(captured_error):
        cli.complete_task(999)
    
    # Check that the error message is correct
    error_output = captured_error.getvalue().strip()
    assert "Error:" in error_output
    assert "not found" in error_output