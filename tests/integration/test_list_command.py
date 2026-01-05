"""
Integration tests for the list command in the CLI Todo application.
"""
import sys
import io
from contextlib import redirect_stdout
import pytest
from src.services.todo_service import TodoService
from src.ui.cli import TodoCLI


def test_list_command_integration():
    """Test that the list command works through the CLI interface."""
    service = TodoService()
    cli = TodoCLI(service)
    
    # Add some tasks first
    service.add_task("First task")
    service.add_task("Second task")
    
    # Capture stdout
    captured_output = io.StringIO()
    
    # List tasks
    with redirect_stdout(captured_output):
        cli.list_tasks()
    
    # Check that the output is correct
    output = captured_output.getvalue().strip()
    lines = output.split('\n')
    
    # Should have 2 lines for the 2 tasks
    assert len(lines) == 2
    
    # Check the format of each line
    assert "1. [ ] First task" in lines
    assert "2. [ ] Second task" in lines


def test_list_command_empty():
    """Test that the list command handles empty lists correctly."""
    service = TodoService()
    cli = TodoCLI(service)
    
    # Capture stdout
    captured_output = io.StringIO()
    
    # List tasks when there are none
    with redirect_stdout(captured_output):
        cli.list_tasks()
    
    # Check that the output is correct
    output = captured_output.getvalue().strip()
    assert output == "No tasks found."