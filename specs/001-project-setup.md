# Spec 001: Project Setup

## Context
This specification defines the initial project setup for the Evolution of Todo application. This is the foundational phase that establishes the project structure, development workflow, and initial configuration required for spec-driven development. The goal is to create a clean, organized foundation that follows the constitution's requirements for Phase I - an in-memory console application.

## Requirements

### Functional
- Project must follow the directory structure specified in the constitution
- Project must use Python 3.13+ as required by the constitution
- Project must use UV for package management as specified
- Project must be structured with clear separation: Models → Services → UI/Interface
- Initial CLI entry point must be created to support future features

### Non-Functional
- Project setup must follow PEP 8 style guide
- All function signatures must include type hints
- Project must have no external dependencies beyond standard library for Phase I
- Setup must support the five core features to be implemented in subsequent specs
- Code must be maintainable and extensible for future phases

## Acceptance Criteria
- [ ] Directory structure matches constitution specification
- [ ] pyproject.toml created with proper configuration for UV
- [ ] Basic project files created (main.py, models/__init__.py, services/__init__.py, ui/__init__.py)
- [ ] Initial __init__.py files created for proper Python package structure
- [ ] .gitignore includes standard Python and development files
- [ ] README.md provides clear project overview and setup instructions
- [ ] Project can be initialized with UV package manager

## Technical Design
The project will follow the exact directory structure specified in the constitution:
- `/specs` - Contains specification files
- `/src` - Contains source code with subdirectories for models, services, and UI
- `/tests` - Contains unit and integration tests
- Root files include pyproject.toml, README.md, and .gitignore

The main.py file will serve as the entry point and will eventually implement the CLI interface. The models directory will contain data models for tasks, the services directory will contain business logic, and the UI directory will handle user interface concerns.

## Testing Strategy
- Verify directory structure exists as specified
- Confirm pyproject.toml has correct configuration
- Manual verification that project can be set up with UV
- Basic import tests to ensure package structure is correct

## Dependencies
- None - this is the foundational specification

## Open Questions
- None at this time