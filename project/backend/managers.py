from django.db import connections
from django.utils import timezone

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

    def get_employees_tasks_by_id(self,id):
        with connections['default'].cursor() as cursor:
            cursor.execute('SELECT * FROM backend_employee_tasks WHERE employeeId=%s', [id] )
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
        print(data)
        with connections['default'].cursor() as cursor:
            cursor.execute('INSERT INTO backend_employee_tasks(task_name, EmployeeId, progress,created) VALUES (%s, %s, %s, %s)', [
                data['task_name'], id, data['progress'],timezone.now()])
            return True

    def update_employee_task(self, id, data,task_id):
        with connections['default'].cursor() as cursor:
            cursor.execute('UPDATE backend_employee_tasks SET task_name=%s, progress=%s, updated=%s WHERE id=%s and employeeId=%s' , [
                data['task_name'], data['progress'], timezone.now(),task_id, id])
        return True

    def get_employee(self, id):
        with connections['default'].cursor() as cursor:
            cursor.execute('SELECT * FROM backend_employee WHERE id=%s', [id])
            row = cursor.fetchone()
            response_data = {}
            if(row is not None):
                response_data.update({
                'id': row[0],
                'name': row[1],
                'email': row[2],
                'phone': row[3],
                'address': row[4],
                "department":row[5],
                "designation":row[6],
                "salary":row[7]
                })
            else:
                response_data = None
               
        return response_data

    def create_employee(self, data):
        with connections['default'].cursor() as cursor:
            cursor.execute('INSERT INTO backend_employee(name, email, phone, address, department, designation, salary,created) VALUES (%s, %s, %s, %s, %s, %s, %s, %s )', [
                data['name'], data['email'], data['phone'], data['address'], data['department'], data['designation'], data['salary'],timezone.now()])
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

    def save_employee_document(self,id,documentType,document):
        print(document)
        with connections['default'].cursor() as cursor:
            cursor.execute("INSERT INTO backend_employee_document (document_type,EmployeeId,document,uploaded_at) VALUES (%s, %s, %s, %s) RETURNING id", [documentType,id,document,timezone.now()])
            return cursor.fetchone()[0]

    def update_employee_document(self, id, data,documentId):
        with connections['default'].cursor() as cursor:
            cursor.execute('UPDATE backend_employee_document SET document_type=%s, document=%s WHERE EmployeeId=%s and id=%s', [
                 documentType,document,id,documentId])
        return True

    def get_employees_doc(self):
        with connections['default'].cursor() as cursor:
            cursor.execute('SELECT * FROM backend_employee_document' )
            rows = cursor.fetchall()
            response_data = []
        for employee in rows:
            response_data.append({
            'id': employee[0],
            'document_type': employee[1],
            'EmployeeId': employee[2],
            'uploaded_at': employee[5],
            "updated":employee[4]
        })
        return response_data

    def get_employee_doc(self,id):
        with connections['default'].cursor() as cursor:
            cursor.execute('SELECT * FROM backend_employee_document where EmployeeId=%s',[id])
            rows = cursor.fetchall()
            response_data = []
        for employee in rows:
            response_data.append({
            'id': employee[0],
            'document_type': employee[1],
            'EmployeeId': employee[2],
            'uploaded_at': employee[5],
            "updated":employee[4]
        })
        return response_data