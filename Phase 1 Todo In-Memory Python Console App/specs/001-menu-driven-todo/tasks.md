# Tasks: Menu-Driven Todo CLI Application

**Input**: Design documents from `/specs/001-menu-driven-todo/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

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
- [X] T002 Initialize Python 3.13+ project with standard library dependencies
- [X] T003 [P] Create src directory structure: src/, src/models/, src/services/, src/cli/

---
## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 Create Task model with zero-padded ID, title, description, and completion status in src/models/task.py
- [X] T005 Create TaskManager service for in-memory storage in src/services/task_manager.py
- [X] T006 Create menu interface handler in src/cli/menu_interface.py
- [X] T007 Create main application entry point in src/todo_app.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Menu-Driven Task Display (Priority: P1) 🎯 MVP

**Goal**: Display a menu-driven interface with numbered options that shows the application title centered between separator lines

**Independent Test**: Can start the application and see the main menu with numbered options (1-6) displayed correctly

### Implementation for User Story 1

- [X] T008 [P] [US1] Implement main menu display with centered title and separator lines in src/todo_app.py
- [X] T009 [P] [US1] Implement menu option display (1-6) in src/cli/menu_interface.py
- [X] T010 [US1] Create menu loop to continuously display options until exit in src/todo_app.py
- [X] T011 [US1] Implement option selection handling in src/cli/menu_interface.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Add Task Functionality (Priority: P2)

**Goal**: Allow users to add tasks by selecting option 1, prompting for title first, then description, and assigning a zero-padded numeric ID

**Independent Test**: Can select option 1, enter a title and description, and see the task added with a zero-padded ID

### Implementation for User Story 2

- [X] T012 [P] [US2] Implement add task command in src/cli/menu_interface.py
- [X] T013 [P] [US2] Implement title and description prompts for task creation in src/cli/menu_interface.py
- [X] T014 [US2] Update TaskManager to support adding tasks with zero-padded IDs in src/services/task_manager.py
- [X] T015 [US2] Ensure new tasks are assigned zero-padded numeric IDs (001, 002, etc.) in src/services/task_manager.py
- [X] T016 [US2] Set completion status to false by default when creating tasks in src/services/task_manager.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - View Tasks Functionality (Priority: P3)

**Goal**: Allow users to view all tasks by selecting option 2, displaying them in tabular format with zero-padded ID, title, description, and completion status

**Independent Test**: Can select option 2 and see all tasks displayed in a tabular format with visual separators

### Implementation for User Story 3

- [X] T017 [P] [US3] Implement view tasks command in src/cli/menu_interface.py
- [X] T018 [P] [US3] Create tabular display format for tasks with visual separators in src/cli/menu_interface.py
- [X] T019 [US3] Update TaskManager to support retrieving all tasks in src/services/task_manager.py
- [X] T020 [US3] Format output to show zero-padded ID, title, description, and status in tabular format in src/cli/menu_interface.py

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Update Task Functionality (Priority: P4)

**Goal**: Allow users to update tasks by selecting option 3, prompting for zero-padded task ID, and allowing updates to title and/or description

**Independent Test**: Can select option 3, enter a zero-padded task ID, and update the title and/or description

### Implementation for User Story 4

- [X] T021 [P] [US4] Implement update task command in src/cli/menu_interface.py
- [X] T022 [P] [US4] Implement zero-padded task ID prompt in src/cli/menu_interface.py
- [X] T023 [P] [US4] Implement title and description update prompts in src/cli/menu_interface.py
- [X] T024 [US4] Update TaskManager to support updating task title and description in src/services/task_manager.py
- [X] T025 [US4] Validate that updates work with zero-padded task IDs in src/services/task_manager.py

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---

## Phase 7: User Story 5 - Delete Task Functionality (Priority: P5)

**Goal**: Allow users to delete tasks by selecting option 4 and entering a zero-padded task ID

**Independent Test**: Can select option 4, enter a zero-padded task ID, and successfully delete the task

### Implementation for User Story 5

- [X] T026 [P] [US5] Implement delete task command in src/cli/menu_interface.py
- [X] T027 [P] [US5] Implement zero-padded task ID prompt for deletion in src/cli/menu_interface.py
- [X] T028 [US5] Update TaskManager to support deleting tasks by ID in src/services/task_manager.py
- [X] T029 [US5] Add confirmation message for successful deletion in src/cli/menu_interface.py

**Checkpoint**: At this point, User Stories 1-5 should all work independently

---

## Phase 8: User Story 6 - Mark Complete/Incomplete Functionality (Priority: P6)

**Goal**: Allow users to toggle task completion status by selecting option 5 and entering a zero-padded task ID

**Independent Test**: Can select option 5, enter a zero-padded task ID, and successfully toggle the completion status

### Implementation for User Story 6

- [X] T030 [P] [US6] Implement mark complete/incomplete command in src/cli/menu_interface.py
- [X] T031 [US6] Implement zero-padded task ID prompt for status toggle in src/cli/menu_interface.py
- [X] T032 [US6] Update TaskManager to support toggling completion status in src/services/task_manager.py
- [X] T033 [US6] Add confirmation message for status change in src/cli/menu_interface.py

**Checkpoint**: At this point, User Stories 1-6 should all work independently

---

## Phase 9: User Story 7 - Exit Functionality (Priority: P7)

**Goal**: Allow users to exit the application by selecting option 6

**Independent Test**: Can select option 6 and the application exits gracefully

### Implementation for User Story 7

- [X] T034 [P] [US7] Implement exit command in src/cli/menu_interface.py
- [X] T035 [US7] Ensure clean application shutdown when option 6 is selected in src/todo_app.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 10: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T036 [P] Add proper error handling for invalid menu selections in src/cli/menu_interface.py
- [X] T037 [P] Add proper error handling for invalid task IDs in src/cli/menu_interface.py
- [X] T038 Add input validation for task titles and descriptions in src/services/task_manager.py
- [X] T039 [P] Improve visual formatting with consistent separator lines in src/cli/menu_interface.py
- [X] T040 [P] Ensure in-memory behavior (tasks lost on restart) is consistent across all operations
- [X] T041 Run quickstart validation to ensure all menu options work as described

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - Depends on having tasks to update
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - Depends on having tasks to delete
- **User Story 6 (P6)**: Can start after Foundational (Phase 2) - Depends on having tasks to toggle
- **User Story 7 (P7)**: Can start after Foundational (Phase 2) - No dependencies

### Within Each User Story

- Models before services
- Services before CLI interface
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all components for User Story 1 together:
Task: "Implement main menu display with centered title and separator lines in src/todo_app.py"
Task: "Implement menu option display (1-6) in src/cli/menu_interface.py"
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
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
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