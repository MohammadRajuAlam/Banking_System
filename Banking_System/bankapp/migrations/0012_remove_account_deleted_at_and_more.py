# Generated by Django 5.0 on 2024-06-13 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0011_alter_bank_bank_id_alter_branch_branch_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='accountholder',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='bank',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='branch',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='deleted_at',
        ),
    ]