# Generated by Django 4.2.5 on 2023-09-29 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shms', '0002_days'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='time',
            field=models.IntegerField(default=2000),
        ),
    ]
