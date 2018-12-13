# Generated by Django 2.1.1 on 2018-10-24 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Prod', '0005_productlist_prodcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productlist',
            name='AXProdCode',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='productlist',
            name='AXProdName',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='productlist',
            name='AXRegDate',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='productlist',
            name='Basic_coprice',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='productlist',
            name='Basic_price',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='productlist',
            name='Inventory_YN',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='productlist',
            name='Margin',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='productlist',
            name='Mercury_YN',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='productlist',
            name='RegUser',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='Prod_RegUser', to='MST.CoUser'),
        ),
        migrations.AlterField(
            model_name='productlist',
            name='Remark',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='productlist',
            name='UpdateUser',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='Prod_UpdateUser', to='MST.CoUser'),
        ),
    ]
