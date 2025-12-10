"""Entry point for the Evolution of Todo application.

This is the main CLI interface for the in-memory console todo application.
Phase I - In-Memory Console Application
"""
import sys
from src.services.task_service import TaskService
from src.ui.todo_cli import TodoCLI


def _handle_command(cli: TodoCLI, command: str, parts: list) -> bool:
    """Handle a single command and return True if the app should continue."""
    if command in ['quit', 'exit', 'q']:
        print("Goodbye!")
        return False
    if command in ['help', 'h']:
        print(cli.show_help())
        return True
    if command == 'add':
        if len(parts) < 2:
            print("Usage: add <title> [description]")
        else:
            title = parts[1]
            description = ' '.join(parts[2:]) if len(parts) > 2 else None
            print(cli.add_task(title, description))
        return True
    if command in ['list', 'ls']:
        print(cli.list_tasks())
        return True
    if command == 'update':
        if len(parts) < 2:
            print("Usage: update <id> [title] [description]")
        else:
            try:
                task_id = int(parts[1])
                title = parts[2] if len(parts) > 2 else None
                description = ' '.join(parts[3:]) if len(parts) > 3 else None
                print(cli.update_task(task_id, title, description))
            except ValueError:
                print("Task ID must be a number")
        return True
    if command == 'delete':
        if len(parts) < 2:
            print("Usage: delete <id>")
        else:
            try:
                task_id = int(parts[1])
                print(cli.delete_task(task_id))
            except ValueError:
                print("Task ID must be a number")
        return True
    if command == 'toggle':
        if len(parts) < 2:
            print("Usage: toggle <id>")
        else:
            try:
                task_id = int(parts[1])
                print(cli.toggle_task(task_id))
            except ValueError:
                print("Task ID must be a number")
        return True
    print(f"Unknown command: {command}. Type 'help' for available commands.")
    return True


def main() -> int:
    """Main entry point for the todo application."""
    print("Evolution of Todo - Phase I: In-Memory Console Application")

    # Initialize the task service and CLI
    task_service = TaskService()
    cli = TodoCLI(task_service)

    print("Type 'help' for available commands or 'quit' to exit.")

    while True:
        try:
            command_input = input("\n> ").strip()
            if not command_input:
                continue

            parts = command_input.split()
            command = parts[0].lower()

            # Handle the command and check if we should continue
            if not _handle_command(cli, command, parts):
                return 0

        except EOFError:
            # Handle Ctrl+D or when input is not available (e.g., in tests)
            print("\nGoodbye!")
            return 0
        except KeyboardInterrupt:
            # Handle Ctrl+C
            print("\nGoodbye!")
            return 0

    return 0


if __name__ == "__main__":
    sys.exit(main())

