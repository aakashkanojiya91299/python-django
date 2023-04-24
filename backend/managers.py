from django.db import connections

class EmployeeManager:
    def get_employees(self):
        with connections['default'].cursor() as cursor:
            cursor.execute('SELECT * FROM employees')
            rows = cursor.fetchall()
        return rows

    def get_employee(self, id):
        with connections['default'].cursor() as cursor:
            cursor.execute('SELECT * FROM employees WHERE id=%s', [id])
            row = cursor.fetchone()
        return row

    def create_employee(self, data):
        with connections['default'].cursor() as cursor:
            cursor.execute('INSERT INTO employees(name, email, phone, address, department, designation, salary) VALUES (%s, %s, %s, %s, %s, %s, %s)', [
                data['name'], data['email'], data['phone'], data['address'], data['department'], data['designation'], data['salary']])
        return True

    def update_employee(self, id, data):
        with connections['default'].cursor() as cursor:
            cursor.execute('UPDATE employees SET name=%s, email=%s, phone=%s, address=%s, department=%s, designation=%s, salary=%s WHERE id=%s', [
                data['name'], data['email'], data['phone'], data['address'], data['department'], data['designation'], data['salary'], id])
        return True

    def delete_employee(self, id):
        with connections['default'].cursor() as cursor:
            cursor.execute('DELETE FROM employees WHERE id=%s', [id])
        return True
