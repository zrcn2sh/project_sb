# Generated by Django 2.1.1 on 2018-11-29 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Prod', '0036_auto_20181128_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reqquotation',
            name='VendorReqUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ReqUser', to='MST.CoUser'),
        ),
    ]
