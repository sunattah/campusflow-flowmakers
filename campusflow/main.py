"""Command-line entry point for CampusFlow."""
from campusflow.tickets import create_ticket, list_tickets, find_ticket
from campusflow.validation import validate_ticket_data
from campusflow.storage import load_tickets, save_tickets
from campusflow.workflow import update_ticket_status
from campusflow.reports import print_report

DATA_FILE = "data/tickets.json"


def ask(prompt):
    return input(prompt).strip()


def show_menu():
    print("\n=== CampusFlow ===")
    print("1. Create ticket")
    print("2. List tickets")
    print("3. View ticket")
    print("4. Update ticket status")
    print("5. Reports")
    print("0. Exit")


def main():
    tickets = load_tickets(DATA_FILE)
    while True:
        show_menu()
        choice = ask("Choose an option: ")

        if choice == "1":
            title = input("Title: ")
            description = input("Description: ")
            priority = input("Priority (Low, Medium, High, Urgent): ")
            ticket_data = {
                "title": title,
                "description": description,
                "priority": priority,
                "status": "Open",
            }
            errors = validate_ticket_data(ticket_data)
            if errors:
                print("Ticket was not created:")
                for error in errors:
                    print(f"- {error}")
                continue
            ticket = create_ticket(tickets, title, description, priority)
            save_tickets(DATA_FILE, tickets)
            print(f"Created ticket #{ticket['id']}.")

        elif choice == "2":
            if not tickets:
                print("No tickets found.")
            for ticket in list_tickets(tickets):
                print(f"#{ticket['id']} | {ticket['status']} | {ticket['priority']} | {ticket['title']}")

        elif choice == "3":
            try:
                ticket_id = int(ask("Ticket ID: "))
            except ValueError:
                print("Please enter a whole-number ticket ID.")
                continue
            ticket = find_ticket(tickets, ticket_id)
            if ticket:
                for key, value in ticket.items():
                    print(f"{key.title()}: {value}")
            else:
                print("Ticket not found.")

        elif choice == "4":
            try:
                ticket_id = int(ask("Ticket ID: "))
            except ValueError:
                print("Please enter a whole-number ticket ID.")
                continue
            status = input("New status (Open, In Progress, Resolved, Closed): ")
            ticket = find_ticket(tickets, ticket_id)
            if not ticket:
                print("Ticket not found.")
                continue
            error = update_ticket_status(ticket, status)
            if error:
                print(error)
            else:
                save_tickets(DATA_FILE, tickets)
                print("Ticket status updated.")

        elif choice == "5":
            print_report(tickets)

        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid menu option. Choose 0–5.")


if __name__ == "__main__":
    main()
