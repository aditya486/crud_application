# Generated by Django 2.1.7 on 2019-02-19 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0006_auto_20190219_0637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Date_of_Birth',
            field=models.DateField(),
        ),
    ]