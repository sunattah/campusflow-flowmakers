import unittest
from campusflow.tickets import calculate_priority, create_ticket, generate_ticket_id

class TestTickets(unittest.TestCase):
    
    def test_priority_rule_1_critical(self):
        self.assertEqual(calculate_priority("high", 12), "critical")
        self.assertEqual(calculate_priority("high", 10), "critical")

    def test_priority_rule_2_high(self):
        self.assertEqual(calculate_priority("high", 5), "high")
        self.assertEqual(calculate_priority("low", 15), "high")

    def test_priority_rule_3_medium(self):
        self.assertEqual(calculate_priority("medium", 1), "medium")
        self.assertEqual(calculate_priority("low", 3), "medium")

    def test_priority_rule_4_low(self):
        self.assertEqual(calculate_priority("low", 1), "low")
        self.assertEqual(calculate_priority("low", 2), "low")

    def test_invalid_affected_users_zero_or_negative(self):
        with self.assertRaises(ValueError):
            calculate_priority("high", 0)
        with self.assertRaises(ValueError):
            calculate_priority("medium", -3)

    def test_invalid_urgency(self):
        with self.assertRaises(ValueError):
            calculate_priority("urgent", 5)

    def test_create_ticket_success(self):
        existing = []
        ticket = create_ticket("Wi-Fi down", "Network", "high", 12, existing)
        self.assertEqual(ticket["id"], "T001")
        self.assertEqual(ticket["priority"], "critical")
        self.assertEqual(ticket["status"], "open")
        self.assertIsNone(ticket["assigned_to"])

    def test_blank_title_rejected(self):
        with self.assertRaises(ValueError):
            create_ticket("   ", "Hardware", "low", 2, [])

    def test_id_generation_sequence(self):
        existing = [{"id": "T005"}]
        new_id = generate_ticket_id(existing)
        self.assertEqual(new_id, "T006")

if __name__ == "__main__":
    unittest.main()