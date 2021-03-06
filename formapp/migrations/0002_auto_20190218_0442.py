# Generated by Django 2.1.7 on 2019-02-18 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='Address',
            field=models.CharField(default=1, max_length=1024),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='Mobile_No',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default=1, max_length=2),
            preserve_default=False,
        ),
    ]
