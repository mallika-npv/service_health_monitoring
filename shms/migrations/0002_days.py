# Generated by Django 4.2.5 on 2023-09-28 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='days',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('webs', models.TextField(max_length=255)),
                ('dt', models.FloatField()),
                ('high_dt', models.BooleanField()),
            ],
        ),
    ]
