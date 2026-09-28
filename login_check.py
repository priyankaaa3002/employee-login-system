import sqlite3
import bcrypt

def check_login(emp_id, password):
    conn = sqlite3.connect("company_db")
    cur = conn.cursor()

    cur.execute("SELECT password_hash FROM employees WHERE employee_id = ?", (emp_id,))
    row = cur.fetchone()
    conn.close()

    if row is None:
        return "ID doesn't exist"

    stored_hash = row[0]
    if bcrypt.checkpw(password.encode(), stored_hash):
        return "Access successful"
    return "Password incorrect"


#login_check(user)
if __name__ == "__main__":
    emp_id = input("Employee ID: ").strip()
    password = input("Password: ")
    print(check_login(emp_id, password))
