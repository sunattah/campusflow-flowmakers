# AI Learning Log

## Fellow: Engineer A
### Interaction #1 — Python Exception Raising and Validation
- **Problem:** Needed to ensure `affected_users` only accepts valid positive integers.
- **Initial understanding:** Thought basic `int()` casting was enough.
- **Prompt to AI:** "Explain how to validate function arguments for types and ranges in Python with a clean example."
- **AI guidance:** Suggested checking `isinstance(val, int)` and handling boolean edge cases where `isinstance(True, int)` evaluates to True.
- **Experiment/Test:** Tested passing floats, negative numbers, and booleans into the priority function.
- **Verification:** Unit tests confirmed `ValueError` and `TypeError` are raised correctly.
- **Decision:** Accepted and implemented in `tickets.py`.

---

## Fellow: Engineer B
### Interaction #1 — Safe File Persistence with JSON
- **Problem:** Needed to handle missing storage files gracefully on startup.
- **Initial understanding:** Thought `open()` would automatically create a file for reading.
- **Prompt to AI:** "Explain how to check if a file exists before loading JSON in Python."
- **AI guidance:** Suggested using `os.path.exists()` and catching `json.JSONDecodeError`.
- **Experiment/Test:** Wrote a test case passing a corrupted JSON string to verify error trapping.
- **Verification:** Test passed when a `ValueError` was successfully raised.
- **Decision:** Accepted and implemented in `storage.py`.