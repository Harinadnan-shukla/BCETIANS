# Generated by Django 3.0 on 2020-12-27 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signupform',
            name='Batch',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='signupform',
            name='Mobile',
            field=models.IntegerField(),
        ),
    ]