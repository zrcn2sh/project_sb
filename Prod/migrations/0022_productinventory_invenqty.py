# Generated by Django 2.1.1 on 2018-10-26 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Prod', '0021_auto_20181026_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinventory',
            name='InvenQty',
            field=models.IntegerField(default=0),
        ),
    ]
