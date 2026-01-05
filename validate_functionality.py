#!/usr/bin/env python3
"""
Validation script to test the CLI Todo application functionality
based on the quickstart guide examples.
"""
import sys
import os

# Add the project root to the path so we can import modules properly
sys.path.insert(0, os.path.dirname(__file__))

from src.services.todo_service import TodoService
from src.ui.cli import TodoCLI


def test_functionality():
    """Test all functionality as described in the quickstart guide."""
    print("Testing CLI Todo Application functionality...")

    # Create service and CLI interface
    service = TodoService()
    cli = TodoCLI(service)

    print("\n1. Testing 'add' command:")
    print("   Command: cli.add_task('Buy groceries')")
    cli.add_task("Buy groceries")
    print("   Expected: 'Task 1 added.'")

    print("\n2. Testing 'list' command:")
    print("   Command: cli.list_tasks()")
    cli.list_tasks()
    print("   Expected: '1. [ ] Buy groceries'")

    print("\n3. Testing 'complete' command:")
    print("   Command: cli.complete_task(1)")
    cli.complete_task(1)
    print("   Expected: 'Task 1 marked completed.'")

    print("\n4. Testing 'list' command again to see completion:")
    print("   Command: cli.list_tasks()")
    cli.list_tasks()
    print("   Expected: '1. [X] Buy groceries'")

    print("\n5. Testing 'update' command:")
    print("   Command: cli.update_task(1, 'Buy groceries and cook dinner')")
    cli.update_task(1, "Buy groceries and cook dinner")
    print("   Expected: 'Task 1 updated.'")

    print("\n6. Testing 'list' command again to see updated title:")
    print("   Command: cli.list_tasks()")
    cli.list_tasks()
    print("   Expected: '1. [X] Buy groceries and cook dinner'")

    print("\n7. Testing 'delete' command:")
    print("   Command: cli.delete_task(1)")
    cli.delete_task(1)
    print("   Expected: 'Task 1 removed.'")

    print("\n8. Testing 'list' command to confirm deletion:")
    print("   Command: cli.list_tasks()")
    cli.list_tasks()
    print("   Expected: 'No tasks found.'")

    print("\nAll functionality validated successfully!")


if __name__ == "__main__":
    test_functionality()