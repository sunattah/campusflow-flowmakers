"""Validation helpers for ticket fields."""

ALLOWED_PRIORITIES = {"low", "medium", "high", "urgent"}
ALLOWED_STATUSES = {"open", "in progress", "resolved", "closed"}
MIN_TITLE_LENGTH = 3
MAX_TITLE_LENGTH = 100
MIN_DESCRIPTION_LENGTH = 5
MAX_DESCRIPTION_LENGTH = 1000


def validate_title(title):
    """Return True when title is a non-empty string within the allowed length."""
    if not isinstance(title, str):
        return False
    cleaned = title.strip()
    return MIN_TITLE_LENGTH <= len(cleaned) <= MAX_TITLE_LENGTH


def validate_description(description):
    """Return True when description is a non-empty string within the allowed length."""
    if not isinstance(description, str):
        return False
    cleaned = description.strip()
    return MIN_DESCRIPTION_LENGTH <= len(cleaned) <= MAX_DESCRIPTION_LENGTH


def validate_priority(priority):
    """Accept allowed priorities without caring about letter case."""
    return isinstance(priority, str) and priority.strip().casefold() in ALLOWED_PRIORITIES


def validate_status(status):
    """Accept allowed statuses without caring about letter case."""
    return isinstance(status, str) and status.strip().casefold() in ALLOWED_STATUSES


def validate_ticket_data(ticket_data):
    """Return a list of readable validation errors; an empty list means valid."""
    errors = []
    if not isinstance(ticket_data, dict):
        return ["Ticket data must be a dictionary."]
    if not validate_title(ticket_data.get("title")):
        errors.append(f"Title must contain {MIN_TITLE_LENGTH}–{MAX_TITLE_LENGTH} characters.")
    if not validate_description(ticket_data.get("description")):
        errors.append(
            f"Description must contain {MIN_DESCRIPTION_LENGTH}–{MAX_DESCRIPTION_LENGTH} characters."
        )
    if not validate_priority(ticket_data.get("priority")):
        errors.append("Priority must be Low, Medium, High, or Urgent.")
    if not validate_status(ticket_data.get("status")):
        errors.append("Status must be Open, In Progress, Resolved, or Closed.")
    return errors
