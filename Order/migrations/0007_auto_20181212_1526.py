# Generated by Django 2.1.1 on 2018-12-12 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0006_auto_20181212_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offerprice',
            name='SignNumber',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
