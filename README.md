# Evolution of Todo

## Phase I: In-Memory Console Application

This is the initial phase of the Evolution of Todo project - a command-line todo application built using Python 3.13+ with in-memory storage.

## Setup

1. Ensure you have Python 3.13+ installed
2. Install UV package manager: `pip install uv`
3. Install dependencies: `uv sync` (or `uv pip install -e .`)

## Project Structure

```
evolution-of-todo/
├── README.md              # Project overview and setup
├── CLAUDE.md              # AI development guide
├── pyproject.toml         # UV dependencies
├── .gitignore
├── specs/                 # Specification history
│   ├── 001-setup.md
│   ├── 002-add-task.md
│   └── ...
├── src/                   # Source code
│   ├── __init__.py
│   ├── main.py           # Entry point
│   ├── models/           # Data models
│   ├── services/         # Business logic
│   └── ui/               # User interface
└── tests/                # Test files
    ├── unit/
    └── integration/
```

## Features

This application will implement the following core features:

- **FR-001: Add Task** - Add new tasks with title and optional description
- **FR-002: View Tasks** - List all tasks with status indicators
- **FR-003: Update Task** - Update task title and/or description
- **FR-004: Delete Task** - Remove tasks by ID
- **FR-005: Toggle Completion** - Mark tasks as complete/incomplete

## Development Methodology

This project follows a spec-driven development approach where every feature begins as a specification file in the `/specs` folder. No code generation occurs without an approved specification.

## Next Steps

1. Create your first specification file: `specs/001-project-setup.md`
2. Review with Claude Code
3. Approve specification
4. Implement according to the specification