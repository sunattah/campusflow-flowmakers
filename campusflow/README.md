# CampusFlow

CampusFlow is a small Python command-line application for creating and tracking campus support tickets. It stores tickets locally in JSON.

## Features

- Create tickets with a title, description, priority, and initial `Open` status.
- List all tickets and view one ticket by ID.
- Update a ticket's status.
- View simple totals grouped by status and priority.
- Validate input before changing ticket data.
- Save tickets to `data/tickets.json`.

## Requirements

- Python 3.10 or newer
- No third-party packages required

## Run

From the project root:

```bash
python main.py
```

Use the menu to create and manage tickets. Valid priorities are `Low`, `Medium`, `High`, and `Urgent`. Valid statuses are `Open`, `In Progress`, `Resolved`, and `Closed`.

## Run tests

```bash
python -m unittest discover -v
```

The tests use Python's built-in `unittest` library and temporary files, so they do not need to modify your real ticket data.

## Project structure

- `main.py` — command-line menu and user interaction
- `campusflow/validation.py` — validates ticket fields
- `campusflow/tickets.py` — creates, lists, and finds tickets
- `campusflow/workflow.py` — updates ticket statuses
- `campusflow/storage.py` — reads and writes JSON
- `campusflow/reports.py` — summarizes ticket data
- `tests/` — automated tests
- `data/tickets.json` — local ticket data file

## Design notes

This is a learning/demo CLI, not a multi-user production service. It does not include login, role permissions, concurrent editing, or a database. Status updates currently accept any allowed status rather than enforcing a strict transition sequence. The `.gitignore` excludes `data/tickets.json` because it may contain local data; the empty starter file is included in this archive, but Git will ignore it once the ignore rule applies.
