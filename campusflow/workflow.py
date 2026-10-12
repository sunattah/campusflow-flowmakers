"""
Engineer B Module: Assignment, Lifecycle, Work Queue, and Reports.
"""

VALID_STATUSES = {"open", "in_progress", "resolved"}
PRIORITY_ORDER = {"critical": 0, "high": 1, "medium": 2, "low": 3}

def assign_ticket(tickets: list, ticket_id: str, staff_name: str) -> dict:
    if not staff_name or not staff_name.strip():
        raise ValueError("Staff name cannot be empty.")
    
    for t in tickets:
        if t["id"] == ticket_id:
            t["assigned_to"] = staff_name.strip()
            return t
    raise KeyError(f"Ticket ID {ticket_id} not found.")

def update_status(tickets: list, ticket_id: str, new_status: str) -> dict:
    ns = new_status.strip().lower()
    if ns not in VALID_STATUSES:
        raise ValueError(f"Invalid status: {new_status}. Allowed: {VALID_STATUSES}")
    
    target = None
    for t in tickets:
        if t["id"] == ticket_id:
            target = t
            break
            
    if not target:
        raise KeyError(f"Ticket ID {ticket_id} not found.")
        
    current_status = target["status"]
    
    # Workflow constraints:
    # 1. Unassigned ticket cannot move to in_progress
    if ns == "in_progress" and not target["assigned_to"]:
        raise ValueError("Cannot move unassigned ticket to in_progress.")
        
    # 2. Resolved ticket can only be modified if explicitly reopened to open
    if current_status == "resolved" and ns != "open":
        raise ValueError("Resolved tickets can only be modified via explicit reopen to open.")
        
    target["status"] = ns
    return target

def get_work_queue(tickets: list) -> list:
    """Returns open, unresolved tickets sorted by priority then numeric ID."""
    unresolved = [t for t in tickets if t["status"] in ("open", "in_progress")]
    
    def sort_key(ticket):
        p_rank = PRIORITY_ORDER.get(ticket["priority"], 4)
        tid_num = int(ticket["id"][1:]) if ticket["id"].startswith("T") and ticket["id"][1:].isdigit() else 0
        return (p_rank, tid_num)
        
    return sorted(unresolved, key=sort_key)

def generate_reports(tickets: list) -> dict:
    total = len(tickets)
    by_status = {"open": 0, "in_progress": 0, "resolved": 0}
    by_priority = {"critical": 0, "high": 0, "medium": 0, "low": 0}
    
    for t in tickets:
        s = t.get("status", "open")
        p = t.get("priority", "low")
        if s in by_status:
            by_status[s] += 1
        if p in by_priority:
            by_priority[p] += 1
            
    return {
        "total_tickets": total,
        "by_status": by_status,
        "by_priority": by_priority
    }