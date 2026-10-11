import unittest
from campusflow.tickets import create_ticket, list_tickets, find_ticket


class TicketTests(unittest.TestCase):
    def test_create_ticket_assigns_id_and_open_status(self):
        tickets = []
        ticket = create_ticket(tickets, "Broken projector", "It will not turn on.", "High")
        self.assertEqual(ticket["id"], 1)
        self.assertEqual(ticket["status"], "Open")
        self.assertEqual(len(tickets), 1)

    def test_ids_increment_from_existing_tickets(self):
        tickets = [{"id": 4, "title": "Existing"}]
        ticket = create_ticket(tickets, "Wi-Fi problem", "Wi-Fi is unavailable.", "Medium")
        self.assertEqual(ticket["id"], 5)

    def test_invalid_ticket_is_not_added(self):
        tickets = []
        with self.assertRaises(ValueError):
            create_ticket(tickets, "", "Too short", "Critical")
        self.assertEqual(tickets, [])

    def test_find_ticket(self):
        tickets = [{"id": 1}, {"id": 2}]
        self.assertEqual(find_ticket(tickets, 2), {"id": 2})
        self.assertIsNone(find_ticket(tickets, 99))

    def test_list_tickets_orders_by_id(self):
        tickets = [{"id": 3}, {"id": 1}]
        self.assertEqual([t["id"] for t in list_tickets(tickets)], [1, 3])


if __name__ == "__main__":
    unittest.main()
