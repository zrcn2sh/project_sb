# Generated by Django 2.1.1 on 2018-12-11 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0002_auto_20181210_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='offerprice',
            name='OrderDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
