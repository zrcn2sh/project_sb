# Generated by Django 2.1.1 on 2018-09-14 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MST', '0005_auto_20180913_0728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codept',
            name='RegDate',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='codept',
            name='UpdateDate',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='coemp',
            name='RegDate',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='coemp',
            name='UpdateDate',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='couser',
            name='RegDate',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='couser',
            name='UpdateDate',
            field=models.DateField(auto_now=True),
        ),
    ]
