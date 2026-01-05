"""
Integration tests for the add command in the CLI Todo application.
"""
import sys
import io
from contextlib import redirect_stdout, redirect_stderr
import pytest
from src.services.todo_service import TodoService
from src.ui.cli import TodoCLI


def test_add_command_integration():
    """Test that the add command works through the CLI interface."""
    service = TodoService()
    cli = TodoCLI(service)
    
    # Capture stdout
    captured_output = io.StringIO()
    
    # Add a task
    with redirect_stdout(captured_output):
        cli.add_task("Test task for integration")
    
    # Check that the output is correct
    output = captured_output.getvalue().strip()
    assert output == "Task 1 added."
    
    # Verify the task was actually added to the service
    tasks = service.get_all_tasks()
    assert len(tasks) == 1
    assert tasks[0].title == "Test task for integration"
    assert tasks[0].completed is False


def test_add_command_empty_title_error():
    """Test that the add command handles empty titles correctly."""
    service = TodoService()
    cli = TodoCLI(service)
    
    # Capture stderr
    captured_error = io.StringIO()
    
    # Try to add a task with an empty title
    with redirect_stderr(captured_error):
        cli.add_task("")
    
    # Check that the error message is correct
    error_output = captured_error.getvalue().strip()
    assert "Error:" in error_output