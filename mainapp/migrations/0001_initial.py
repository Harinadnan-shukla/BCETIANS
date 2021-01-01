# Generated by Django 3.0 on 2020-12-27 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignUpForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Batch', models.IntegerField(max_length=20)),
                ('Branch', models.CharField(max_length=20)),
                ('Address', models.CharField(max_length=100)),
                ('Mobile', models.IntegerField(max_length=12)),
                ('Email', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'SignUpRequest',
            },
        ),
    ]
