"""JSON file persistence for tickets."""
import json
from pathlib import Path


def load_tickets(filename):
    """Load a list of tickets; return an empty list if the file is missing/empty."""
    path = Path(filename)
    if not path.exists():
        return []
    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except (json.JSONDecodeError, OSError) as error:
        raise ValueError(f"Could not read ticket data from {path}: {error}") from error
    if not isinstance(data, list):
        raise ValueError(f"Ticket data in {path} must be a JSON list.")
    return data


def save_tickets(filename, tickets):
    """Save tickets as readable JSON, creating parent folders if needed."""
    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        json.dump(tickets, file, indent=2, ensure_ascii=False)
        file.write("\n")
