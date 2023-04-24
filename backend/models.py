from django.db import connection

def create_employee_table():
    with connection.cursor() as cursor:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS employee (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(254) UNIQUE NOT NULL,
                phone VARCHAR(20) NOT NULL,
                address VARCHAR(500) NOT NULL,
                department VARCHAR(100) NOT NULL,
                designation VARCHAR(100) NOT NULL,
                salary DECIMAL(10, 2) NOT NULL
            );
        ''')

def insert_employee(name, email, phone, address, department, designation, salary):
    with connection.cursor() as cursor:
        cursor.execute('''
            INSERT INTO employee (name, email, phone, address, department, designation, salary)
            VALUES (%s, %s, %s, %s, %s, %s, %s);
        ''', [name, email, phone, address, department, designation, salary])

def select_all_employees():
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM employee;')
        return cursor.fetchall()

def select_employee_by_id(employee_id):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM employee WHERE id = %s;', [employee_id])
        return cursor.fetchone()

def update_employee(employee_id, name, email, phone, address, department, designation, salary):
    with connection.cursor() as cursor:
        cursor.execute('''
            UPDATE employee
            SET name = %s, email = %s, phone = %s, address = %s, department = %s, designation = %s, salary = %s
            WHERE id = %s;
        ''', [name, email, phone, address, department, designation, salary, employee_id])

def delete_employee(employee_id):
    with connection.cursor() as cursor:
        cursor.execute('DELETE FROM employee WHERE id = %s;', [employee_id])

