# Generated by Django 3.0.5 on 2020-06-06 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0016_auto_20200606_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='colour_code',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='picture',
            field=models.ImageField(upload_to='images/'),
        ),
    ]