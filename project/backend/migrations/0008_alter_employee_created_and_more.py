# Generated by Django 4.2 on 2023-04-26 19:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_alter_employee_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='employee_document',
            name='uploaded_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='employee_tasks',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]