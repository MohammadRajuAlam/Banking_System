# Generated by Django 5.0 on 2024-06-23 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0018_alter_account_options_alter_accountholder_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('Deposit', 'Deposit'), ('Withdraw', 'Withdraw')], max_length=20),
        ),
    ]