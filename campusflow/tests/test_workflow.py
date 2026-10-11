import unittest
from campusflow.workflow import update_ticket_status


class WorkflowTests(unittest.TestCase):
    def test_valid_status_update(self):
        ticket = {"status": "Open"}
        self.assertIsNone(update_ticket_status(ticket, "in progress"))
        self.assertEqual(ticket["status"], "In Progress")

    def test_invalid_status_does_not_mutate_ticket(self):
        ticket = {"status": "Open"}
        self.assertIsNotNone(update_ticket_status(ticket, "Waiting"))
        self.assertEqual(ticket["status"], "Open")


if __name__ == "__main__":
    unittest.main()
