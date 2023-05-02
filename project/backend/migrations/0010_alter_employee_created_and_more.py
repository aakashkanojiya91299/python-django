# Generated by Django 4.2 on 2023-04-26 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_alter_employee_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee_document',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee_tasks',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
