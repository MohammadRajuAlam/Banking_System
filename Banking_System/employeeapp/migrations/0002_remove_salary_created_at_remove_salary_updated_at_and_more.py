# Generated by Django 5.0 on 2024-07-07 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salary',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='salary',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='salary',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]