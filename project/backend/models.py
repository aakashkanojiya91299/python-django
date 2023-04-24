from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=500)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Employee_tasks(models.Model):
    task_name = models.CharField(max_length=100)
    EmployeeId = models.IntegerField()
    progress = models.DecimalField(max_digits=3, decimal_places=2)
    created = models.DateTimeField()
    updated = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.task_name

class Employee_document(models.Model):
    document_type = models.CharField(max_length=100)
    EmployeeId = models.IntegerField()
    document = models.BinaryField()
    created = models.DateTimeField()
    updated = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.task_name
        
