import json
import tempfile
import unittest
from pathlib import Path
from campusflow.storage import load_tickets, save_tickets


class StorageTests(unittest.TestCase):
    def test_missing_file_returns_empty_list(self):
        with tempfile.TemporaryDirectory() as directory:
            self.assertEqual(load_tickets(Path(directory) / "missing.json"), [])

    def test_save_and_load_round_trip(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "data" / "tickets.json"
            tickets = [{"id": 1, "title": "Wi-Fi problem"}]
            save_tickets(path, tickets)
            self.assertEqual(load_tickets(path), tickets)

    def test_invalid_json_raises_clear_error(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "tickets.json"
            path.write_text("{bad json", encoding="utf-8")
            with self.assertRaises(ValueError):
                load_tickets(path)


if __name__ == "__main__":
    unittest.main()
