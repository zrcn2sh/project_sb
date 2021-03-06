# Generated by Django 2.1.1 on 2018-10-24 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Prod', '0009_auto_20181024_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productlist',
            name='RegUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Prod_RegUser', to='MST.CoUser'),
        ),
        migrations.AlterField(
            model_name='productlist',
            name='UpdateUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Prod_UpdateUser', to='MST.CoUser'),
        ),
    ]
