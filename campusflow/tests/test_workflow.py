import unittest
import os
import tempfile
from campusflow.workflow import assign_ticket, update_status, get_work_queue, generate_reports
from campusflow.storage import save_tickets, load_tickets

class TestWorkflowAndStorage(unittest.TestCase):
    
    def setUp(self):
        self.sample_tickets = [
            {"id": "T001", "title": "A", "category": "Network", "urgency": "low", "affected_users": 1, "priority": "low", "status": "open", "assigned_to": None},
            {"id": "T002", "title": "B", "category": "Hardware", "urgency": "high", "affected_users": 15, "priority": "critical", "status": "open", "assigned_to": "Alice"},
            {"id": "T003", "title": "C", "category": "Software", "urgency": "high", "affected_users": 5, "priority": "high", "status": "in_progress", "assigned_to": "Bob"}
        ]
        self.test_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.test_dir.name, "tickets.json")

    def tearDown(self):
        self.test_dir.cleanup()

    def test_assign_ticket_success(self):
        t = assign_ticket(self.sample_tickets, "T001", "Charlie")
        self.assertEqual(t["assigned_to"], "Charlie")

    def test_assign_ticket_unknown_id(self):
        with self.assertRaises(KeyError):
            assign_ticket(self.sample_tickets, "T999", "Charlie")

    def test_unassigned_cannot_start_in_progress(self):
        with self.assertRaises(ValueError):
            update_status(self.sample_tickets, "T001", "in_progress")

    def test_assigned_ticket_lifecycle(self):
        update_status(self.sample_tickets, "T002", "in_progress")
        self.assertEqual(self.sample_tickets[1]["status"], "in_progress")
        
        update_status(self.sample_tickets, "T002", "resolved")
        self.assertEqual(self.sample_tickets[1]["status"], "resolved")
        
        # Resolved ticket cannot change to in_progress directly
        with self.assertRaises(ValueError):
            update_status(self.sample_tickets, "T002", "in_progress")
            
        # Reopen to open is allowed
        update_status(self.sample_tickets, "T002", "open")
        self.assertEqual(self.sample_tickets[1]["status"], "open")

    def test_work_queue_sorting(self):
        queue = get_work_queue(self.sample_tickets)
        # Critical (T002) should come before High (T003), which comes before Low (T001)
        self.assertEqual(queue[0]["id"], "T002")
        self.assertEqual(queue[1]["id"], "T003")
        self.assertEqual(queue[2]["id"], "T001")

    def test_reports(self):
        report = generate_reports(self.sample_tickets)
        self.assertEqual(report["total_tickets"], 3)
        self.assertEqual(report["by_priority"]["critical"], 1)

    def test_json_persistence(self):
        save_tickets(self.db_path, self.sample_tickets)
        loaded = load_tickets(self.db_path)
        self.assertEqual(len(loaded), 3)
        self.assertEqual(loaded[1]["id"], "T002")

if __name__ == "__main__":
    unittest.main()