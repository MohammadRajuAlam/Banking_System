# Generated by Django 5.0 on 2024-06-13 12:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0008_alter_bank_bank_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='bank_id',
            field=models.CharField(error_messages={'unique': 'Given bank_id is already used.'}, max_length=10, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_bank_id', message='Bank ID must contain both characters and numbers.', regex='^(?=.*[a-zA-Z])(?=.*\\d)[a-zA-Z\\d]*$')]),
        ),
        migrations.AlterField(
            model_name='bank',
            name='bank_name',
            field=models.CharField(error_messages={'null': 'Bank Name should not be blank'}, max_length=100),
        ),
    ]