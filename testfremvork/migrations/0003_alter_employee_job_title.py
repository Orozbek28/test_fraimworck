# Generated by Django 4.2 on 2023-04-19 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testfremvork', '0002_alter_employee_job_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='job_title',
            field=models.CharField(max_length=20),
        ),
    ]
