# Generated by Django 3.0.5 on 2020-06-18 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0036_auto_20200618_1419'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='roll',
        ),
        migrations.AddField(
            model_name='request',
            name='roll_number',
            field=models.ForeignKey(default='123456789', on_delete=django.db.models.deletion.CASCADE, to='tools.Customer'),
        ),
    ]
