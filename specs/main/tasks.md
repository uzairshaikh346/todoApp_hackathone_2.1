---

description: "Task list for Simple CLI Todo App implementation"
---

# Tasks: Simple CLI Todo App

**Input**: Design documents from `/specs/main/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The feature specification includes a testing strategy, so test tasks will be included.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan
- [X] T002 Initialize Python 3.13+ project with pyproject.toml
- [X] T003 [P] Configure linting and formatting tools (ruff, black)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 [P] Create Task model in src/models/task.py based on data model
- [X] T005 [P] Create TodoService in src/services/todo_service.py with in-memory storage
- [X] T006 Create main.py entry point with CLI argument parsing using argparse
- [X] T007 Configure error handling and CLI output formatting
- [X] T008 Setup basic testing framework with pytest

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Task (Priority: P1) 🎯 MVP

**Goal**: Allow users to add new tasks with a title to the todo list

**Independent Test**: User can run `python main.py add "Task title"` and see "Task [ID] added." message, and the task appears in the list

### Tests for User Story 1 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T009 [P] [US1] Unit test for TodoService.add_task() in tests/unit/test_todo_service.py
- [X] T010 [P] [US1] Integration test for add command in tests/integration/test_add_command.py

### Implementation for User Story 1

- [X] T011 [US1] Implement add_task method in src/services/todo_service.py
- [X] T012 [US1] Implement add command in src/ui/cli.py
- [X] T013 [US1] Connect add command to main.py CLI interface
- [X] T014 [US1] Add validation for task title (non-empty string)

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Task List (Priority: P1)

**Goal**: Display all tasks with their completion status in a readable format

**Independent Test**: User can run `python main.py list` and see all tasks with their IDs and completion status

### Tests for User Story 2 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T015 [P] [US2] Unit test for TodoService.get_all_tasks() in tests/unit/test_todo_service.py
- [X] T016 [P] [US2] Integration test for list command in tests/integration/test_list_command.py

### Implementation for User Story 2

- [X] T017 [US2] Implement get_all_tasks method in src/services/todo_service.py
- [X] T018 [US2] Implement list command in src/ui/cli.py
- [X] T019 [US2] Connect list command to main.py CLI interface
- [X] T020 [US2] Format output to match specification: "1. [ ] Task title" or "1. [X] Task title"

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Task Complete (Priority: P2)

**Goal**: Allow users to mark a specific task as completed using its ID

**Independent Test**: User can run `python main.py complete 1` and see "Task 1 marked completed." message, and the task shows as completed when listed

### Tests for User Story 3 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T021 [P] [US3] Unit test for TodoService.mark_task_complete() in tests/unit/test_todo_service.py
- [X] T022 [P] [US3] Integration test for complete command in tests/integration/test_complete_command.py

### Implementation for User Story 3

- [X] T023 [US3] Implement mark_task_complete method in src/services/todo_service.py
- [X] T024 [US3] Implement complete command in src/ui/cli.py
- [X] T025 [US3] Connect complete command to main.py CLI interface
- [X] T026 [US3] Add validation for task ID (positive integer)

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Delete Task (Priority: P3)

**Goal**: Allow users to remove a specific task from the list using its ID

**Independent Test**: User can run `python main.py delete 1` and see "Task 1 removed." message, and the task no longer appears in the list

### Tests for User Story 4 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T027 [P] [US4] Unit test for TodoService.delete_task() in tests/unit/test_todo_service.py
- [X] T028 [P] [US4] Integration test for delete command in tests/integration/test_delete_command.py

### Implementation for User Story 4

- [X] T029 [US4] Implement delete_task method in src/services/todo_service.py
- [X] T030 [US4] Implement delete command in src/ui/cli.py
- [X] T031 [US4] Connect delete command to main.py CLI interface
- [X] T032 [US4] Add validation for task ID (positive integer)

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---

## Phase 7: User Story 5 - Update Task (Priority: P4)

**Goal**: Allow users to modify the title of an existing task using its ID

**Independent Test**: User can run `python main.py update 1 "New title"` and see "Task 1 updated." message, and the task shows the new title when listed

### Tests for User Story 5 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T033 [P] [US5] Unit test for TodoService.update_task() in tests/unit/test_todo_service.py
- [X] T034 [P] [US5] Integration test for update command in tests/integration/test_update_command.py

### Implementation for User Story 5

- [X] T035 [US5] Implement update_task method in src/services/todo_service.py
- [X] T036 [US5] Implement update command in src/ui/cli.py
- [X] T037 [US5] Connect update command to main.py CLI interface
- [X] T038 [US5] Add validation for task ID (positive integer) and new title (non-empty string)

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T039 [P] Documentation updates in README.md
- [X] T040 Code cleanup and refactoring
- [X] T041 [P] Additional unit tests in tests/unit/
- [X] T042 Error handling for invalid commands or IDs
- [X] T043 Run quickstart.md validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3 → P4)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 4 (P3)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 5 (P4)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together:
- [ ] T009 [P] [US1] Unit test for TodoService.add_task() in tests/unit/test_todo_service.py
- [ ] T010 [P] [US1] Integration test for add command in tests/integration/test_add_command.py

# Launch implementation tasks for User Story 1:
- [ ] T011 [US1] Implement add_task method in src/services/todo_service.py
- [ ] T012 [US1] Implement add command in src/ui/cli.py
- [ ] T013 [US1] Connect add command to main.py CLI interface
- [ ] T014 [US1] Add validation for task title (non-empty string)
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence