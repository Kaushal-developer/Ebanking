# Generated by Django 3.1.4 on 2021-01-01 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0004_auto_20210101_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan_detail',
            name='loan_approve',
            field=models.CharField(default='pending', max_length=20),
        ),
    ]
