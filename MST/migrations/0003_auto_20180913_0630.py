# Generated by Django 2.1.1 on 2018-09-13 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MST', '0002_auto_20180913_0629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coemp',
            name='UpdateDate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='productlist',
            name='UpdateDate',
            field=models.DateField(),
        ),
    ]
