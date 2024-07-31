# Generated by Django 5.0 on 2024-07-20 07:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0022_alter_branch_bank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account', to='bankapp.branch'),
        ),
        migrations.AlterField(
            model_name='accountholder',
            name='account_number',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='accountholder', to='bankapp.account'),
        ),
    ]