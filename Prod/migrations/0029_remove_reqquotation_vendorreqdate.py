# Generated by Django 2.1.1 on 2018-11-08 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Prod', '0028_auto_20181108_1435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reqquotation',
            name='VendorReqDate',
        ),
    ]
