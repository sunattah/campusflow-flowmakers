import unittest
from campusflow.validation import (
    validate_title, validate_description, validate_priority,
    validate_status, validate_ticket_data,
)


class ValidationTests(unittest.TestCase):
    def test_title_valid_and_invalid(self):
        self.assertTrue(validate_title("Broken projector"))
        self.assertFalse(validate_title("  "))
        self.assertFalse(validate_title("Hi"))
        self.assertFalse(validate_title(None))

    def test_description_valid_and_invalid(self):
        self.assertTrue(validate_description("Projector will not turn on."))
        self.assertFalse(validate_description("no"))
        self.assertFalse(validate_description("   "))

    def test_priority_is_case_insensitive(self):
        for priority in ("Low", "Medium", "High", "Urgent", "high"):
            with self.subTest(priority=priority):
                self.assertTrue(validate_priority(priority))
        self.assertFalse(validate_priority("Critical"))
        self.assertFalse(validate_priority(None))

    def test_status_is_case_insensitive(self):
        for status in ("Open", "In Progress", "Resolved", "Closed", "in progress"):
            with self.subTest(status=status):
                self.assertTrue(validate_status(status))
        self.assertFalse(validate_status("Pending"))

    def test_ticket_data_valid(self):
        ticket = {
            "title": "Wi-Fi problem",
            "description": "Cannot connect to campus Wi-Fi.",
            "priority": "High",
            "status": "Open",
        }
        self.assertEqual(validate_ticket_data(ticket), [])

    def test_ticket_data_reports_all_errors(self):
        errors = validate_ticket_data({
            "title": "",
            "description": "",
            "priority": "Critical",
            "status": "Pending",
        })
        self.assertEqual(len(errors), 4)

    def test_ticket_data_rejects_non_dictionary(self):
        self.assertTrue(validate_ticket_data(None))


if __name__ == "__main__":
    unittest.main()
