# Generated by Django 2.1.1 on 2018-11-07 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Prod', '0023_auto_20181026_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productlist',
            name='SSD',
            field=models.CharField(blank=True, choices=[('0', 'None'), ('1', '64GB'), ('2', '120GB'), ('3', '128GB'), ('4', '250GB'), ('5', '256GB'), ('6', '500GB'), ('7', '512GB'), ('8', '1TB'), ('9', '2TB'), ('10', '2TB초과')], max_length=2),
        ),
    ]
