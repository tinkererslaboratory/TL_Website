# Generated by Django 3.0.5 on 2020-05-21 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0004_item_display'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='displaylevel1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='displaylevel2',
            field=models.BooleanField(default=False),
        ),
    ]