# Generated by Django 2.1.1 on 2018-10-24 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Prod', '0008_auto_20181024_0658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productlist',
            name='Basic_coprice',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='productlist',
            name='Basic_price',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
