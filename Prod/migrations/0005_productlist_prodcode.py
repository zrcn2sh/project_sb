# Generated by Django 2.1.1 on 2018-10-24 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Prod', '0004_auto_20181024_0535'),
    ]

    operations = [
        migrations.AddField(
            model_name='productlist',
            name='ProdCode',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
