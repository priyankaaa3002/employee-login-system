# Employee Login System

A small SQLite-backed employee login system in Python, built to practice secure credential storage and parameterized SQL.

## Scripts

- **`employee_data.py`** — creates the `employees` table and seeds it with sample employee records. Passwords are hashed with `bcrypt` before being stored; nothing is ever saved in plain text.
- **`login_check.py`** — command-line login check. Looks up an employee by ID and verifies the entered password against the stored bcrypt hash.

## Security notes

- Passwords are hashed with `bcrypt` (salted, one-way) rather than stored or compared in plain text.
- All queries use parameterized SQL (`?` placeholders) to prevent SQL injection.

## Usage

```bash
pip install -r requirements.txt
python employee_data.py    # creates company_db and seeds sample employees
python login_check.py      # prompts for employee ID + password, checks against stored hash
```
