# Generated by Django 2.1.1 on 2018-11-13 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Prod', '0031_auto_20181113_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reqquotation',
            name='ReqVendor1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ReqVendor1', to='MST.CoVendor'),
        ),
    ]
