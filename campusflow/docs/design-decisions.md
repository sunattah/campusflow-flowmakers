# Design Decisions

## JSON storage
Tickets are stored in a JSON list so the project can run without installing a database or third-party package.

## Separation of responsibilities
The CLI, validation, ticket operations, persistence, workflow, and reporting are separated into modules. This makes the functions easier to understand and test.

## Validation return values
Single-field validators return `True` or `False`. `validate_ticket_data()` returns a list of error messages; an empty list means all fields are valid.

## Ticket IDs
New IDs are one greater than the largest existing ID, or 1 when there are no tickets.

## Known limitations
This learning version has no authentication, permissions, concurrency protection, or strict status-transition rules. JSON corruption is reported as an error rather than silently overwriting the file.
