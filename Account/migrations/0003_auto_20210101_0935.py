# Generated by Django 3.1.4 on 2021-01-01 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_auto_20210101_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan_detail',
            name='user_exists',
            field=models.CharField(default='No', max_length=5),
        ),
    ]
