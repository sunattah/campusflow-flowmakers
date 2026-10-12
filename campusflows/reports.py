"""
Reports Module: Generates summary statistics and breakdowns of tickets by status and priority.
"""

def generate_reports(tickets: list) -> dict:
    """
    Analyzes the ticket collection and returns a dictionary containing:
    - total_tickets: Total count of tickets
    - by_status: Breakdown count for open, in_progress, and resolved
    - by_priority: Breakdown count for critical, high, medium, and low
    """
    total = len(tickets)
    
    by_status = {
        "open": 0,
        "in_progress": 0,
        "resolved": 0
    }
    
    by_priority = {
        "critical": 0,
        "high": 0,
        "medium": 0,
        "low": 0
    }
    
    for t in tickets:
        status = t.get("status", "open").strip().lower()
        priority = t.get("priority", "low").strip().lower()
        
        if status in by_status:
            by_status[status] += 1
        else:
            # Handle any unexpected status gracefully
            by_status[status] = by_status.get(status, 0) + 1
            
        if priority in by_priority:
            by_priority[priority] += 1
        else:
            by_priority[priority] = by_priority.get(priority, 0) + 1
            
    return {
        "total_tickets": total,
        "by_status": by_status,
        "by_priority": by_priority
    }