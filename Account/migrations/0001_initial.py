# Generated by Django 3.1.4 on 2021-01-01 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='account_detail',
            fields=[
                ('Aname', models.CharField(max_length=200)),
                ('Fname', models.CharField(max_length=200)),
                ('Mname', models.CharField(max_length=200)),
                ('Address', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('pincode', models.IntegerField()),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('dob', models.CharField(max_length=200)),
                ('mob', models.IntegerField()),
                ('aadhar', models.IntegerField(unique=True)),
                ('pancard', models.CharField(max_length=200, unique=True)),
                ('account_type', models.CharField(max_length=200)),
                ('Applicants_image', models.ImageField(upload_to='files/')),
                ('aadhar_image', models.ImageField(upload_to='files/')),
                ('pan_image', models.ImageField(upload_to='files/')),
                ('Sign', models.ImageField(upload_to='files/')),
                ('account_approve', models.CharField(default='pending', max_length=20)),
            ],
        ),
    ]
