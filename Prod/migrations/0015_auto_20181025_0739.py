# Generated by Django 2.1.1 on 2018-10-25 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Prod', '0014_auto_20181025_0654'),
    ]

    operations = [
        migrations.AddField(
            model_name='productlist',
            name='BWRatio',
            field=models.CharField(blank=True, choices=[('1', '800:1 이하'), ('2', '801-1,000:1'), ('3', '1,001:1-3,000:1'), ('4', '3,001:1-4,999:1'), ('5', '5000:1이상')], max_length=2),
        ),
        migrations.AddField(
            model_name='productlist',
            name='ETCRemark1',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='productlist',
            name='ETCRemark2',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='productlist',
            name='ETCRemark3',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='productlist',
            name='Panel',
            field=models.CharField(blank=True, choices=[('1', 'IPS'), ('3', 'VA'), ('5', 'TN'), ('7', 'PLS'), ('9', 'AHVA'), ('11', 'AD-PLS')], max_length=2),
        ),
        migrations.AddField(
            model_name='productlist',
            name='ReqSpeed',
            field=models.CharField(blank=True, choices=[('1', '1-4'), ('2', '5-8'), ('3', '9-12'), ('4', '13-16'), ('5', '17-20'), ('6', '21-')], max_length=2),
        ),
        migrations.AddField(
            model_name='productlist',
            name='Resolution',
            field=models.CharField(blank=True, choices=[('1', 'HD이하'), ('3', 'FHD(1920x1080'), ('5', 'WFHD(2560x1080)'), ('7', 'WQHD(2560x1440)'), ('9', 'UWQHD(3440x1440)'), ('11', '4KUHD(3840x2160)'), ('13', '4KUHD초과')], max_length=2),
        ),
        migrations.AddField(
            model_name='productlist',
            name='SRCapacity',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='productlist',
            name='SRCuttingSize',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='productlist',
            name='SRInputWidth',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='productlist',
            name='SRPowerCon',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='productlist',
            name='Size',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
