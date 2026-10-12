# CampusFlow Design Decisions

## 1. Data Structures & Storage Contract
- **Decision:** Tickets are stored as a list of dictionaries in-memory and serialized into JSON via `storage.py`.
- **Rationale:** Keeps data handling transparent, simple, and native to Python without requiring external databases.

## 2. Function Ownership & Responsibilities
- **Engineer A:** Owns `campusflow/tickets.py` (ticket creation, field validation, and priority rules engine).
- **Engineer B:** Owns workflow assignment, status lifecycle, queue sorting, reports, and JSON persistence.

## 3. Error Handling Strategy
- **Decision:** Functions raise descriptive `ValueError` or `KeyError` exceptions when inputs or state transitions are invalid.
- **Rationale:** Allows the CLI and unit tests to catch errors cleanly and display meaningful messages to users.