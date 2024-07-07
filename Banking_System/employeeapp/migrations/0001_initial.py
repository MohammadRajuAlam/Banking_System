# Generated by Django 5.0 on 2024-07-01 12:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('department_name', models.CharField(error_messages={'unique': 'Given name already exists.'}, max_length=50, unique=True)),
                ('department_id', models.CharField(error_messages={'unique': 'Given ID is already used.'}, max_length=10, unique=True)),
                ('phone', models.PositiveBigIntegerField(error_messages={'unique': 'Given number is already used.'}, unique=True)),
                ('email', models.EmailField(error_messages={'unique': 'Given Email ID is already used.'}, max_length=30, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=10)),
                ('middle_name', models.CharField(blank=True, max_length=10, null=True)),
                ('last_name', models.CharField(max_length=10)),
                ('employee_id', models.CharField(error_messages={'unique': 'Given ID is already used.'}, max_length=10, unique=True)),
                ('designation', models.CharField(max_length=50)),
                ('total_experience', models.FloatField(default=0)),
                ('date_of_join', models.DateField()),
                ('highest_degree', models.CharField(max_length=50)),
                ('phone', models.PositiveBigIntegerField(error_messages={'unique': 'Given number is already used.'}, unique=True)),
                ('email', models.EmailField(error_messages={'unique': 'Given email ID is already used.'}, max_length=30, unique=True)),
                ('is_working_here', models.BooleanField(default=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employeeapp.department')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('date', models.DateField()),
                ('attendance_status', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent'), ('Leave', 'Leave')], max_length=20)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employeeapp.employee')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('bank_name', models.CharField(max_length=50)),
                ('account_number', models.PositiveBigIntegerField(error_messages={'unique': 'Given account number is already used.'}, unique=True)),
                ('account_type', models.CharField(choices=[('Current', 'Current'), ('Saving', 'Saving'), ('Joint', 'Joint')], max_length=20)),
                ('balance', models.FloatField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='employeeapp.employee')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EmployeeDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('employee_aadhaar', models.PositiveBigIntegerField(error_messages={'unique': 'Given Aadhaar number already exists.'}, unique=True)),
                ('father_name', models.CharField(max_length=20)),
                ('house_phone_number', models.PositiveBigIntegerField(blank=True, error_messages={'unique': 'Given phone number already exists.'}, null=True, unique=True)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('pincode', models.IntegerField()),
                ('country', models.CharField(default='India', max_length=50)),
                ('date_of_birth', models.DateField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employeeapp.employee')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('project_name', models.CharField(max_length=100)),
                ('project_id', models.CharField(error_messages={'unique': 'Given project ID already exists.'}, max_length=10, unique=True)),
                ('technologies_used', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('description', models.CharField(max_length=255)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employeeapp.department')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employeeapp.employee')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('amount', models.FloatField(default=0)),
                ('date', models.DateField()),
                ('remark', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('account_number', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employeeapp.account')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employeeapp.employee')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('task_name', models.CharField(max_length=100)),
                ('task_id', models.CharField(error_messages={'unique': 'Task ID already exists.'}, max_length=10, unique=True)),
                ('task_status', models.CharField(choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], max_length=20)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('task_description', models.CharField(max_length=255)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employeeapp.employee')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employeeapp.project')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]