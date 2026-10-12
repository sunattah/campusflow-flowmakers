"""
Engineer A Module: Ticket Creation, Validation, and Priority Calculation.
"""

VALID_CATEGORIES = {"Network", "Hardware", "Software", "Other"}
VALID_URGENCIES = {"low", "medium", "high"}

def calculate_priority(urgency: str, affected_users: int) -> str:
    """
    Applies priority rules strictly in order:
    RULE 1: high urgency AND >= 10 affected users -> critical
    RULE 2: high urgency OR >= 10 affected users  -> high
    RULE 3: medium urgency OR >= 3 affected users -> medium
    RULE 4: all remaining valid tickets           -> low
    """
    u_lower = urgency.strip().lower()
    if u_lower not in VALID_URGENCIES:
        raise ValueError(f"Invalid urgency: {urgency}. Must be low, medium, or high.")
    
    if not isinstance(affected_users, int) or isinstance(affected_users, bool):
        raise TypeError("affected_users must be an integer.")
    if affected_users <= 0:
        raise ValueError("affected_users must be a positive integer greater than zero.")

    # Rule 1
    if u_lower == "high" and affected_users >= 10:
        return "critical"
    # Rule 2
    if u_lower == "high" or affected_users >= 10:
        return "high"
    # Rule 3
    if u_lower == "medium" or affected_users >= 3:
        return "medium"
    # Rule 4
    return "low"

def generate_ticket_id(existing_tickets: list) -> str:
    """Generates sequential unique IDs like T001, T002, etc."""
    if not existing_tickets:
        return "T001"
    
    max_num = 0
    for t in existing_tickets:
        tid = t.get("id", "")
        if tid.startswith("T") and tid[1:].isdigit():
            num = int(tid[1:])
            if num > max_num:
                max_num = num
    return f"T{max_num + 1:03d}"

def create_ticket(title: str, category: str, urgency: str, affected_users: int, existing_tickets: list) -> dict:
    """Validates inputs and creates a new ticket dictionary."""
    if not title or not title.strip():
        raise ValueError("Ticket title must not be blank.")
    
    cat_cleaned = category.strip().capitalize()
    if cat_cleaned not in VALID_CATEGORIES:
        raise ValueError(f"Invalid category. Choose from {list(VALID_CATEGORIES)}.")
    
    u_cleaned = urgency.strip().lower()
    priority = calculate_priority(u_cleaned, affected_users)
    ticket_id = generate_ticket_id(existing_tickets)

    return {
        "id": ticket_id,
        "title": title.strip(),
        "category": cat_cleaned,
        "urgency": u_cleaned,
        "affected_users": affected_users,
        "priority": priority,
        "status": "open",
        "assigned_to": None
    }