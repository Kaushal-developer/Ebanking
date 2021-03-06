# Generated by Django 3.1.4 on 2021-01-01 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='loan_detail',
            fields=[
                ('date', models.DateField(auto_now=True)),
                ('Aname', models.CharField(max_length=200)),
                ('Address', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('pincode', models.IntegerField()),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('mob', models.IntegerField()),
                ('Applicants_image', models.ImageField(upload_to='files/')),
                ('user_exists', models.BooleanField(default='No')),
                ('emp_type', models.CharField(max_length=20)),
                ('sal_range', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='account_detail',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
