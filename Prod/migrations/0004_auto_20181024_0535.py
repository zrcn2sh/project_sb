# Generated by Django 2.1.1 on 2018-10-24 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Prod', '0003_auto_20181024_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reqquotation',
            name='Status',
            field=models.CharField(blank=True, choices=[('A', '접수'), ('R', '요청'), ('S', '제안'), ('O', '발주'), ('C', '변경'), ('F', '실패')], default='A', max_length=2),
        ),
    ]
