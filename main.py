"""
Entry point for the CLI Todo application.

This module provides the main command-line interface for the todo application.
It handles argument parsing and routes commands to the appropriate handlers.
"""
import argparse
import sys
from src.services.todo_service import TodoService
from src.ui.cli import TodoCLI


def interactive_mode():
    """
    Run the CLI in interactive mode with a numbered menu.
    """
    service = TodoService()
    cli = TodoCLI(service)

    while True:
        print("\n=== TODO APP MENU ===")
        print("1. Add task")
        print("2. List tasks")
        print("3. Complete task")
        print("4. Update task")
        print("5. Delete task")
        print("6. Exit")
        print("=====================")

        try:
            choice = input("Enter your choice (1-6): ").strip()

            if choice == '1':
                title = input("Enter task title: ").strip()
                if title:
                    cli.add_task(title)
                else:
                    print("Task title cannot be empty.")
            elif choice == '2':
                cli.list_tasks()
            elif choice == '3':
                try:
                    task_id = int(input("Enter task ID to complete: "))
                    cli.complete_task(task_id)
                except ValueError:
                    print("Please enter a valid task ID (number).")
            elif choice == '4':
                try:
                    task_id = int(input("Enter task ID to update: "))
                    new_title = input("Enter new title: ").strip()
                    if new_title:
                        cli.update_task(task_id, new_title)
                    else:
                        print("Task title cannot be empty.")
                except ValueError:
                    print("Please enter a valid task ID (number).")
            elif choice == '5':
                try:
                    task_id = int(input("Enter task ID to delete: "))
                    cli.delete_task(task_id)
                except ValueError:
                    print("Please enter a valid task ID (number).")
            elif choice == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)


def main():
    """
    Main entry point for the CLI Todo application.

    Parses command-line arguments and executes the appropriate command
    using the TodoService and CLI interface. If no arguments are provided,
    runs in interactive mode.
    """
    parser = argparse.ArgumentParser(
        description="CLI Todo Application - Manage your tasks from the command line"
    )

    # Define subcommands
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Add command
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('title', nargs='+', help='Task title')

    # List command
    list_parser = subparsers.add_parser('list', help='List all tasks')

    # Complete command
    complete_parser = subparsers.add_parser('complete', help='Mark a task as complete')
    complete_parser.add_argument('id', type=int, help='Task ID')

    # Update command
    update_parser = subparsers.add_parser('update', help='Update a task title')
    update_parser.add_argument('id', type=int, help='Task ID')
    update_parser.add_argument('new_title', nargs='+', help='New task title')

    # Delete command
    delete_parser = subparsers.add_parser('delete', help='Delete a task')
    delete_parser.add_argument('id', type=int, help='Task ID')

    # Parse arguments
    args = parser.parse_args()

    # If no command is provided, run interactive mode
    if args.command is None:
        interactive_mode()
    else:
        # Create service and CLI interface
        service = TodoService()
        cli = TodoCLI(service)

        # Execute the appropriate command
        try:
            if args.command == 'add':
                title = ' '.join(args.title)
                cli.add_task(title)
            elif args.command == 'list':
                cli.list_tasks()
            elif args.command == 'complete':
                cli.complete_task(args.id)
            elif args.command == 'update':
                new_title = ' '.join(args.new_title)
                cli.update_task(args.id, new_title)
            elif args.command == 'delete':
                cli.delete_task(args.id)
            else:
                # Invalid command
                print(f"Error: Unknown command '{args.command}'", file=sys.stderr)
                parser.print_help()
                sys.exit(1)
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()