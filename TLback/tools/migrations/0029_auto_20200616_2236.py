# Generated by Django 3.0.5 on 2020-06-16 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0028_auto_20200616_2233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='id',
        ),
        migrations.AlterField(
            model_name='customer',
            name='roll_number',
            field=models.CharField(default='123456789', max_length=11, primary_key=True, serialize=False),
        ),
    ]