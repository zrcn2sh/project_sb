# Generated by Django 2.1.1 on 2018-10-26 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Prod', '0022_productinventory_invenqty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinventory',
            name='Remark',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='productinventory',
            name='UpdateUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Inven_UpdateUser', to='MST.CoUser'),
        ),
    ]
