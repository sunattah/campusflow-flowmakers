"""Ticket creation and lookup operations."""
from .validation import validate_ticket_data


def create_ticket(tickets, title, description, priority):
    """Create, append, and return a ticket. Raises ValueError for invalid data."""
    next_id = max((ticket.get("id", 0) for ticket in tickets), default=0) + 1
    ticket = {
        "id": next_id,
        "title": title.strip() if isinstance(title, str) else title,
        "description": description.strip() if isinstance(description, str) else description,
        "priority": priority.strip().title() if isinstance(priority, str) else priority,
        "status": "Open",
    }
    errors = validate_ticket_data(ticket)
    if errors:
        raise ValueError(" ".join(errors))
    tickets.append(ticket)
    return ticket


def list_tickets(tickets):
    """Return tickets ordered by ID."""
    return sorted(tickets, key=lambda ticket: ticket.get("id", 0))


def find_ticket(tickets, ticket_id):
    """Return the ticket matching an ID, or None."""
    for ticket in tickets:
        if ticket.get("id") == ticket_id:
            return ticket
    return None
