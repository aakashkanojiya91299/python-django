from django.db import connections

class EmployeeManager:
    def get_employees(self):
        with connections['default'].cursor() as cursor:
            cursor.execute('SELECT * FROM backend_employee' )
            rows = cursor.fetchall()
            response_data = []
        for employee in rows:
            response_data.append({
            'id': employee[0],
            'name': employee[1],
            'email': employee[2],
            'phone': employee[3],
            'address': employee[4],
            "department":employee[5],
        "designation":employee[6],
        "salary":employee[7],
        })
            
        return response_data

    def get_employees_tasks(self):
        with connections['default'].cursor() as cursor:
            cursor.execute('SELECT * FROM backend_employee_tasks' )
            rows = cursor.fetchall()
            response_data = []
        for employee in rows:
            response_data.append({
            'id': employee[0],
            'task_name':employee[1],
            'EmployeeId': employee[2],
            'progress': employee[3],
            'created': employee[4],
            'updated': employee[5],
            
        })
        return response_data

    def create_employee_task(self,id,data):
         with connections['default'].cursor() as cursor:
            cursor.execute('INSERT INTO backend_employee_tasks(task_name, EmployeeId, progress, created) VALUES (%s, %s, %s, %s)', [
                data['task_name'], id, data['progress'], data['created']])
            return True

    def update_employee_task(self, id, data):
        with connections['default'].cursor() as cursor:
            cursor.execute('UPDATE backend_employee_tasks SET task_name=%s, progress=%s, updated=%s WHERE id=%s' , [
                data['task_name'], data['progress'], data['updated'], id])
        return True

    def get_employee(self, id):
        with connections['default'].cursor() as cursor:
            cursor.execute('SELECT * FROM backend_employee WHERE id=%s', [id])
            row = cursor.fetchone()
            response_data = []
        for employee in row:
            response_data.append({
            'id': employee[0],
            'name': employee[1],
            'email': employee[2],
            'phone': employee[3],
            'address': employee[4],
            "department":employee[5],
        "designation":employee[6],
        "salary":employee[7]
        })
        return response_data

    def create_employee(self, data):
        with connections['default'].cursor() as cursor:
            cursor.execute('INSERT INTO backend_employee(name, email, phone, address, department, designation, salary) VALUES (%s, %s, %s, %s, %s, %s, %s)', [
                data['name'], data['email'], data['phone'], data['address'], data['department'], data['designation'], data['salary']])
        return True

    def update_employee(self, id, data):
        with connections['default'].cursor() as cursor:
            cursor.execute('UPDATE backend_employee SET name=%s, email=%s, phone=%s, address=%s, department=%s, designation=%s, salary=%s WHERE id=%s', [
                data['name'], data['email'], data['phone'], data['address'], data['department'], data['designation'], data['salary'], id])
        return True

    def delete_employee(self, id):
        with connections['default'].cursor() as cursor:
            cursor.execute('DELETE FROM backend_employee WHERE id=%s', [id])
        return True
