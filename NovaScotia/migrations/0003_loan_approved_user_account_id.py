# Generated by Django 3.1.4 on 2021-01-02 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NovaScotia', '0002_loan_approved_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan_approved_user',
            name='account_ID',
            field=models.BigIntegerField(default=0),
        ),
    ]