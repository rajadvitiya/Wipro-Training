import pymysql

class EmployeeDB:
    def __init__(self):
        # Connect to MySQL using PyMySQL
        self.conn = pymysql.connect(
            host="localhost",
            user="root",
            password="pass@word1",
            database="employeedb",
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.conn.cursor()
        print("Connected to database")

    # CREATE
    def create_employee(self, eid, ename, salary, bonus):
        try:
            self.cursor.execute(
                "INSERT INTO employee (eid, ename, salary, bonus) VALUES (%s, %s, %s, %s)",
                (eid, ename, salary, bonus)
            )
            self.conn.commit()
            print("Employee created successfully")
        except Exception as e:
            print(f"Error creating employee: {e}")

    # READ
    def read_employees(self):
        try:
            self.cursor.execute("SELECT * FROM employee")
            rows = self.cursor.fetchall()
            if not rows:
                print("No employees found")
            for row in rows:
                print(row)
        except Exception as e:
            print(f"Error reading employees: {e}")

    # UPDATE salary and bonus
    def update_employee(self, eid, new_salary=None, new_bonus=None):
        try:
            if new_salary is not None:
                self.cursor.execute(
                    "UPDATE employee SET salary=%s WHERE eid=%s",
                    (new_salary, eid)
                )
            if new_bonus is not None:
                self.cursor.execute(
                    "UPDATE employee SET bonus=%s WHERE eid=%s",
                    (new_bonus, eid)
                )
            self.conn.commit()
            print("Employee updated successfully")
        except Exception as e:
            print(f"Error updating employee: {e}")

    # DELETE
    def delete_employee(self, eid):
        try:
            self.cursor.execute("DELETE FROM employee WHERE eid=%s", (eid,))
            self.conn.commit()
            print("Employee deleted successfully")
        except Exception as e:
            print(f"Error deleting employee: {e}")

    # Close connection
    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        print("Connection closed")


#============================================

if __name__ == "__main__":
    db = EmployeeDB()

    # CREATE
    db.create_employee(1, "Alice", 50000, 5000)

    # READ
    db.read_employees()

    # UPDATE
    db.update_employee(1, new_salary=60000, new_bonus=7000)
    db.read_employees()

    # DELETE
    db.delete_employee(1)
    db.read_employees()

    # Close connection
    db.close()

#============================================
