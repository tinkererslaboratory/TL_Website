# Generated by Django 3.0.5 on 2020-07-26 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0047_fblink'),
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('status', models.BooleanField(default=False)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools.Item')),
            ],
        ),
    ]
