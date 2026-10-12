import os
from campusflow.tickets import create_ticket
from campusflow.queue import get_work_queue
from campusflow.reports import generate_reports
from campusflow.storage import save_tickets, load_tickets

DB_FILE = "data/tickets.json"

def assign_ticket(tickets: list, ticket_id: str, staff_name: str) -> dict:
    if not staff_name or not staff_name.strip():
        raise ValueError("Staff name cannot be empty.")
    for t in tickets:
        if t["id"] == ticket_id:
            t["assigned_to"] = staff_name.strip()
            return t
    raise KeyError(f"Ticket ID {ticket_id} not found.")

def update_status(tickets: list, ticket_id: str, new_status: str) -> dict:
    VALID_STATUSES = {"open", "in_progress", "resolved"}
    ns = new_status.strip().lower()
    if ns not in VALID_STATUSES:
        raise ValueError(f"Invalid status: {new_status}")
    
    target = next((t for t in tickets if t["id"] == ticket_id), None)
    if not target:
        raise KeyError(f"Ticket ID {ticket_id} not found.")
        
    current_status = target["status"]
    if ns == "in_progress" and not target["assigned_to"]:
        raise ValueError("Cannot move unassigned ticket to in_progress.")
    if current_status == "resolved" and ns != "open":
        raise ValueError("Resolved tickets can only be modified via explicit reopen to open.")
        
    target["status"] = ns
    return target

def main():
    try:
        tickets = load_tickets(DB_FILE)
    except Exception as e:
        print(f"Error loading database: {e}")
        tickets = []

    while True:
        print("\n=== CampusFlow Helpdesk Menu ===")
        print("1. Create Ticket")
        print("2. List All Tickets")
        print("3. View Ticket Details")
        print("4. Assign Ticket")
        print("5. Update Ticket Status (Workflow)")
        print("6. Show Work Queue")
        print("7. Show Reports")
        print("8. Exit")
        
        choice = input("Select an option (1-8): ").strip()
        
        if choice == "1":
            title = input("Enter ticket title: ")
            category = input("Enter category (Network, Hardware, Software, Other): ")
            urgency = input("Enter urgency (low, medium, high): ")
            try:
                affected_users = int(input("Enter affected users (positive integer): "))
                new_t = create_ticket(title, category, urgency, affected_users, tickets)
                tickets.append(new_t)
                save_tickets(DB_FILE, tickets)
                print(f"Success! Created ticket {new_t['id']} with priority '{new_t['priority']}'.")
            except Exception as err:
                print(f"Error creating ticket: {err}")

        elif choice == "2":
            if not tickets:
                print("No tickets found.")
            else:
                print("\n--- All Tickets ---")
                for t in tickets:
                    print(f"[{t['id']}] {t['title']} | Status: {t['status']} | Priority: {t['priority']} | Assigned: {t['assigned_to']}")

        elif choice == "3":
            tid = input("Enter ticket ID to view: ").strip()
            found = next((t for t in tickets if t["id"] == tid), None)
            if found:
                print("\n--- Ticket Details ---")
                for k, v in found.items():
                    print(f"  {k}: {v}")
            else:
                print(f"Ticket ID {tid} not found.")

        elif choice == "4":
            tid = input("Enter ticket ID to assign: ").strip()
            staff = input("Enter staff member name: ").strip()
            try:
                assign_ticket(tickets, tid, staff)
                save_tickets(DB_FILE, tickets)
                print(f"Ticket {tid} successfully assigned to {staff}.")
            except Exception as err:
                print(f"Assignment error: {err}")

        elif choice == "5":
            tid = input("Enter ticket ID: ").strip()
            new_s = input("Enter new status (open, in_progress, resolved): ").strip()
            try:
                update_status(tickets, tid, new_s)
                save_tickets(DB_FILE, tickets)
                print(f"Ticket {tid} status updated to {new_s}.")
            except Exception as err:
                print(f"Workflow error: {err}")

        elif choice == "6":
            queue = get_work_queue(tickets)
            print(f"\n--- Open Work Queue ({len(queue)} items) ---")
            for t in queue:
                print(f"[{t['id']}] Priority: {t['priority'].upper()} | Status: {t['status']} | Title: {t['title']}")

        elif choice == "7":
            report = generate_reports(tickets)
            print("\n--- Helpdesk Reports ---")
            print(f"Total Tickets: {report['total_tickets']}")
            print("By Status:", report['by_status'])
            print("By Priority:", report['by_priority'])

        elif choice == "8":
            print("Exiting CampusFlow. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose a number between 1 and 8.")

if __name__ == "__main__":
    main()