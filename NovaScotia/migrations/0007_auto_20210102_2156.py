# Generated by Django 3.1.4 on 2021-01-03 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NovaScotia', '0006_auto_20210102_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offeres',
            name='offerend',
            field=models.DateTimeField(blank=True),
        ),
    ]
