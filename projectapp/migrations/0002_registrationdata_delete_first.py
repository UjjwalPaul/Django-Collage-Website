# Generated by Django 4.1.2 on 2022-11-13 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='registrationData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('fname', models.CharField(max_length=50)),
                ('mail', models.CharField(max_length=40)),
                ('mob', models.CharField(max_length=10)),
                ('branch', models.CharField(max_length=10)),
                ('dob', models.DateField()),
                ('pass1', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='first',
        ),
    ]
