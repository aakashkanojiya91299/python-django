# Generated by Django 4.2 on 2023-04-26 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_rename_created_employee_document_uploaded_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_document',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
