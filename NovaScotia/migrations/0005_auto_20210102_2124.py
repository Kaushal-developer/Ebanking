# Generated by Django 3.1.4 on 2021-01-03 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NovaScotia', '0004_loan_approved_user_pin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offeres',
            name='offerend',
            field=models.DateField(),
        ),
    ]
