import sqlite3
import bcrypt

#connecting to database 
conn = sqlite3.connect("company_db")
cur = conn.cursor()

#creating a table 
cur.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        employee_id TEXT PRIMARY KEY,
        employee_name TEXT NOT NULL,
        department TEXT,
        email TEXT,
        password_hash BLOB NOT NULL
    )
''')

def add_employee(emp_id, name, dep_name, email, password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    try:
        # This is to avoid SQL Injection
        cur.execute(
            "INSERT INTO employees(employee_id, employee_name, department, email, password_hash)"
            "VALUES (?, ?, ?, ?, ?)",
            (emp_id, name, dep_name, email, hashed)
        )
        conn.commit()
        print(f"Added {name} and ({emp_id})")
    except sqlite3.IntegrityError:
        print(f"ID {emp_id} Already Exists")

add_employee("E001", "Asha Rao", "Engineering", "asha@company.com", "secret123")
add_employee("E002", "Ravi Kumar", "HR", "ravi@company.com", "hunter2")
add_employee("E003", "Neha Sharma", "Finance", "neha@company.com", "finance123")
add_employee("E004", "Arjun Mehta", "Marketing", "arjun@company.com", "market456")
add_employee("E005", "Kavya Singh", "Sales", "kavya@company.com", "sales789")
add_employee("E006", "Rahul Verma", "Operations", "rahul@company.com", "ops321")
add_employee("E007", "Sneha Patel", "Engineering", "sneha@company.com", "eng123")
add_employee("E008", "Vikram Joshi", "Finance", "vikram@company.com", "fin456")


#verifying what's stored 
for row in cur.execute("SELECT employee_id, employee_name, department, email FROM employees"):
    print(row)

conn.close()