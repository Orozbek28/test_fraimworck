# Generated by Django 4.2 on 2023-04-19 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testfremvork', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='job_title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee', to='testfremvork.position'),
        ),
    ]
