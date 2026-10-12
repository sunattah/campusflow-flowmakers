"""
Storage Module: JSON Load and Save operations.
"""
import json
import os

def save_tickets(filepath: str, tickets: list) -> None:
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(tickets, f, indent=4)

def load_tickets(filepath: str) -> list:
    if not os.path.exists(filepath):
        return []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            raise ValueError("JSON root must be a list of tickets.")
    except json.JSONDecodeError as e:
        raise ValueError(f"Malformed JSON in storage file: {e}")