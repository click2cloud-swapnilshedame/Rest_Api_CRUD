# Generated by Django 3.2.3 on 2021-05-30 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empmodels',
            fields=[
                ('EmpID', models.IntegerField(primary_key=True, serialize=False)),
                ('EmpName', models.CharField(max_length=70)),
                ('Email', models.CharField(max_length=70)),
                ('salary', models.IntegerField()),
            ],
            options={
                'db_table': 'Empmodels',
            },
        ),
    ]
