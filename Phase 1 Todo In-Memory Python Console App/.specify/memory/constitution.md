<!--
Sync Impact Report:
- Version change: N/A → 1.0.0
- Modified principles: [PRINCIPLE_1_NAME] → Spec-driven development with no manual coding
- Modified principles: [PRINCIPLE_2_NAME] → In-memory task management with no persistence
- Modified principles: [PRINCIPLE_3_NAME] → Transparency of the full agentic development process
- Modified principles: [PRINCIPLE_4_NAME] → Clean, readable, and reviewable generated code
- Modified principles: [PRINCIPLE_5_NAME] → All functionality must be generated via Claude Code using Spec-Kit Plus
- Added sections: [SECTION_2_NAME] → Implementation Standards, [SECTION_3_NAME] → Development Workflow
- Templates requiring updates:
  - .specify/templates/plan-template.md ✅ updated
  - .specify/templates/spec-template.md ✅ updated
  - .specify/templates/tasks-template.md ✅ updated
  - .specify/commands/sp.*.md ✅ updated
- Follow-up TODOs: None
-->
# Todo In-Memory Python Console Application Constitution

## Core Principles

### Spec-driven development with no manual coding
All functionality must be generated through the spec-driven development workflow using Claude Code and Spec-Kit Plus. No manual coding, editing, or direct file modifications are allowed. All changes must flow through the spec → plan → tasks → implementation pipeline to ensure traceability and compliance.

### In-memory task management with no persistence
Application data exists only in memory during runtime. No persistence across application restarts is permitted. All tasks and state are volatile and will be lost when the application terminates. This ensures simplicity and prevents data corruption issues while maintaining the core functionality requirements.

### Transparency of the full agentic development process
All development activities, decisions, and changes must be fully traceable and transparent. The complete development process including specifications, plans, tasks, implementations, and architectural decisions must be preserved for review and audit purposes.

### Clean, readable, and reviewable generated code
Generated code must follow clean code principles, be easily readable, and suitable for code review processes. Code must be properly structured, documented where necessary, and maintainable while following Python best practices and conventions.

### All functionality must be generated via Claude Code using Spec-Kit Plus
Every piece of functionality, from basic features to complex business logic, must be created using Claude Code and the Spec-Kit Plus framework. This ensures consistency, compliance with project principles, and proper documentation of all development decisions.

### Five basic features implementation
The application must implement all five required features: Add, View, Update, Delete, and Mark Complete. These features form the core functionality of the todo application and must be fully functional and properly integrated.

## Implementation Standards

Application type: Command-line interface only
- Data storage: In-memory only (RAM)
- Programming language: Python 3.13+
- Package manager: UV
- Manual coding: 0% tolerance
- Persistence across application restarts: Not allowed
- Success criteria: All five required features function correctly in the console application, the application runs successfully from the command line, the full spec-driven workflow is clearly traceable, no manually written or edited code is present, all required deliverables are included and compliant

## Development Workflow

Development must follow the workflow: spec → plan → tasks → implementation. All specifications, plans, tasks, and iterations must be preserved for review. Code must follow clean code principles and proper Python project structure. All five basic features must be implemented (Add, View, Update, Delete, Mark Complete).

## Governance

This constitution supersedes all other development practices and guidelines for this project. All development activities must comply with these principles. Amendments to this constitution require explicit documentation, approval, and migration plan. All pull requests and code reviews must verify compliance with these principles. The full development process must maintain transparency and traceability.

**Version**: 1.0.0 | **Ratified**: 2025-12-31 | **Last Amended**: 2025-12-31