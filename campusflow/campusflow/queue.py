"""
Queue Module: Manages open work queues sorted by priority and ticket ID.
"""

# Priority weighting for sorting (lower number = higher priority)
PRIORITY_ORDER = {
    "critical": 0,
    "high": 1,
    "medium": 2,
    "low": 3
}

def get_work_queue(tickets: list) -> list:
    """
    Returns open and unresolved tickets sorted by priority 
    (critical -> high -> medium -> low), breaking ties 
    using the numeric ticket ID (e.g., T001 before T005).
    """
    # Filter for unresolved tickets (open or in_progress)
    unresolved = [t for t in tickets if t.get("status") in ("open", "in_progress")]
    
    def sort_key(ticket):
        # Determine priority rank, default to lowest if unknown
        p_rank = PRIORITY_ORDER.get(ticket.get("priority", "low"), 4)
        
        # Extract numeric part of ticket ID for tie-breaking (e.g., "T003" -> 3)
        tid = ticket.get("id", "T0")
        if tid.startswith("T") and tid[1:].isdigit():
            tid_num = int(tid[1:])
        else:
            tid_num = 0
            
        return (p_rank, tid_num)
        
    # Sort and return the queue
    return sorted(unresolved, key=sort_key)