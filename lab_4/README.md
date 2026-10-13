# Lab 4: Fixtures and Test Data Management

This lab practices using pytest fixtures to prepare and manage test data.

## Topics
- Basic fixtures with `@pytest.fixture`
- Setup and teardown with `yield`
- Function, module, and session scopes
- Shared fixtures in `conftest.py`
- Factory fixtures for custom test data

## Setup (Windows Git Bash)
```bash
python -m venv venv
source venv/Scripts/activate
python -m pip install pytest
```

## Run Tests
```bash
python -m pytest -v -s
```

## Expected Result
All 23 tests pass. Fixture messages show setup, teardown, and scope behavior.
