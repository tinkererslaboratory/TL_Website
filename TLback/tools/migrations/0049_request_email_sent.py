# Generated by Django 3.0.7 on 2020-07-29 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0048_machine'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='email_sent',
            field=models.BooleanField(default=False),
        ),
    ]
