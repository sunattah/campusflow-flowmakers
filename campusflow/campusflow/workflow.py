"""Ticket status updates."""
from .validation import validate_status

# Deliberately simple workflow: users can select any allowed status.
def update_ticket_status(ticket, new_status):
    """Update status, returning an error message or None on success."""
    if not isinstance(ticket, dict):
        return "Invalid ticket."
    if not validate_status(new_status):
        return "Status must be Open, In Progress, Resolved, or Closed."
    normalized = new_status.strip().casefold()
    display_names = {
        "open": "Open",
        "in progress": "In Progress",
        "resolved": "Resolved",
        "closed": "Closed",
    }
    ticket["status"] = display_names[normalized]
    return None
