"""Basic ticket summary reports."""


def build_report(tickets):
    """Return aggregate counts for all, available statuses, and priorities."""
    status_counts = {}
    priority_counts = {}
    for ticket in tickets:
        status = ticket.get("status", "Unknown")
        priority = ticket.get("priority", "Unknown")
        status_counts[status] = status_counts.get(status, 0) + 1
        priority_counts[priority] = priority_counts.get(priority, 0) + 1
    return {
        "total": len(tickets),
        "statuses": status_counts,
        "priorities": priority_counts,
    }


def print_report(tickets):
    report = build_report(tickets)
    print(f"Total tickets: {report['total']}")
    print("By status:")
    if report["statuses"]:
        for status, count in sorted(report["statuses"].items()):
            print(f"  {status}: {count}")
    else:
        print("  No tickets yet.")
    print("By priority:")
    if report["priorities"]:
        for priority, count in sorted(report["priorities"].items()):
            print(f"  {priority}: {count}")
    else:
        print("  No tickets yet.")
