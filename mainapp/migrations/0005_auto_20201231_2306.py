# Generated by Django 3.0 on 2020-12-31 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_eventalumnimeet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventalumnimeet',
            name='Email',
            field=models.EmailField(max_length=254),
        ),
    ]