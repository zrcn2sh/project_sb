# Generated by Django 2.1.1 on 2018-10-24 01:50

import Prod.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('MST', '0016_remove_covendor_vendorcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDetail_DT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DTType', models.CharField(max_length=10, null=True)),
                ('DTCpu', models.CharField(max_length=20, null=True)),
                ('DTCpuDetail', models.CharField(max_length=20, null=True)),
                ('DTRAM', models.IntegerField(null=True)),
                ('DTHDD', models.CharField(max_length=10, null=True)),
                ('DTSSD', models.CharField(max_length=10, null=True)),
                ('DTGraphicCard', models.CharField(max_length=20, null=True)),
                ('DTPower', models.CharField(max_length=10, null=True)),
                ('DTKeyboard_YN', models.BooleanField(null=True)),
                ('DTMouse_YN', models.BooleanField(null=True)),
                ('DTIORemark', models.CharField(max_length=100, null=True)),
                ('DTRemark', models.CharField(max_length=100, null=True)),
                ('RegDate', models.DateField(auto_now_add=True, null=True)),
                ('UpdateDate', models.DateField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetail_ETC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Remark1', models.CharField(max_length=500)),
                ('Remark2', models.CharField(max_length=500)),
                ('Remark3', models.CharField(max_length=500)),
                ('RegDate', models.DateField(auto_now_add=True)),
                ('UpdateDate', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetail_MT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MTScreenSize', models.CharField(max_length=10)),
                ('MTScreenType', models.CharField(max_length=10)),
                ('MTScreenRatio', models.CharField(max_length=10)),
                ('MTResolution', models.CharField(max_length=10)),
                ('MTPanel', models.CharField(max_length=10)),
                ('MTReqSpeed', models.CharField(max_length=10)),
                ('MTBWRatio', models.CharField(max_length=10)),
                ('MTIORemark', models.CharField(max_length=100)),
                ('MTRemark', models.CharField(max_length=100)),
                ('RegDate', models.DateField(auto_now_add=True)),
                ('UpdateDate', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetail_NT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NTType', models.CharField(max_length=10)),
                ('NTCpu', models.CharField(max_length=20)),
                ('NTCpuDetail', models.CharField(max_length=20)),
                ('NTRAM', models.IntegerField()),
                ('NTHDD', models.CharField(max_length=10)),
                ('NTSSD', models.CharField(max_length=10)),
                ('NTGraphicCard', models.CharField(max_length=20)),
                ('NTScreenSize', models.CharField(max_length=10)),
                ('NTWeight', models.CharField(max_length=10)),
                ('NTMouse_YN', models.BooleanField()),
                ('NTPouch_YN', models.BooleanField()),
                ('NTBag_YN', models.BooleanField()),
                ('NTIORemark', models.CharField(max_length=100)),
                ('NTRemark', models.CharField(max_length=100)),
                ('RegDate', models.DateField(auto_now_add=True)),
                ('UpdateDate', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetail_SR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SRInputWidth', models.CharField(max_length=10, null=True)),
                ('SRCuttingSize', models.CharField(max_length=10, null=True)),
                ('SRCapacity', models.CharField(max_length=10, null=True)),
                ('SRPowerCon', models.CharField(max_length=10, null=True)),
                ('SRSize', models.CharField(max_length=30, null=True)),
                ('SRWeight', models.CharField(max_length=10, null=True)),
                ('SRRemark', models.CharField(max_length=100, null=True)),
                ('RegDate', models.DateField(auto_now_add=True, null=True)),
                ('UpdateDate', models.DateField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductInventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('InvenDate', models.DateField()),
                ('Remark', models.CharField(max_length=100)),
                ('RegDate', models.DateField(auto_now_add=True)),
                ('UpdateDate', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProdDiv', models.CharField(max_length=2)),
                ('ProdName', models.CharField(max_length=50)),
                ('ProdBrand', models.CharField(max_length=20)),
                ('Mercury_YN', models.BooleanField()),
                ('AXProdCode', models.CharField(max_length=10)),
                ('AXProdName', models.CharField(max_length=50)),
                ('AXRegDate', models.DateField()),
                ('ProdStatus', models.CharField(max_length=1)),
                ('Basic_coprice', models.IntegerField()),
                ('Basic_price', models.IntegerField()),
                ('Margin', models.FloatField()),
                ('Inventory_YN', models.BooleanField()),
                ('Remark', models.TextField()),
                ('RegDate', models.DateField(auto_now_add=True)),
                ('UpdateDate', models.DateField(auto_now=True)),
                ('RegUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Prod_RegUser', to='MST.CoUser')),
                ('UpdateUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Prod_UpdateUser', to='MST.CoUser')),
                ('VendorCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Prod_Vendor', to='MST.CoVendor')),
            ],
        ),
        migrations.CreateModel(
            name='ReqQuotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ReqNo', models.CharField(default=Prod.models.ReqQuotation.ReqNO_default, max_length=30)),
                ('OriginReqNo', models.CharField(blank=True, max_length=20)),
                ('Custname', models.CharField(max_length=100)),
                ('RPCustname', models.CharField(blank=True, max_length=100)),
                ('Rental_YN', models.BooleanField()),
                ('Bid_YN', models.BooleanField()),
                ('ReqProd', models.TextField()),
                ('Remark', models.CharField(blank=True, max_length=500)),
                ('CanonETC', models.TextField(blank=True)),
                ('ShipDT', models.CharField(blank=True, max_length=8)),
                ('Status', models.CharField(blank=True, max_length=2)),
                ('VendorReq_YN', models.BooleanField()),
                ('FailReason', models.CharField(blank=True, max_length=500)),
                ('RegDate', models.DateField(auto_now_add=True)),
                ('UpdateDate', models.DateField(auto_now=True)),
                ('DeptCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ReqQ_Dept', to='MST.CoDept')),
                ('EmpNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ReqQ_Emp', to='MST.CoEmp')),
                ('RegUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Req_RegUser', to='MST.CoUser')),
                ('ReqVendor1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ReqVendor1', to='MST.CoVendor')),
                ('ReqVendor2', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='ReqVendor2', to='MST.CoVendor')),
                ('ReqVendor3', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='ReqVendor3', to='MST.CoVendor')),
                ('UpdateUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Req_UpdateUser', to='MST.CoUser')),
                ('VendorReqUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ReqUser', to='MST.CoUser')),
            ],
        ),
        migrations.AddField(
            model_name='productinventory',
            name='Prodcode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Prod.ProductList'),
        ),
        migrations.AddField(
            model_name='productinventory',
            name='RegUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Inven_RegUser', to='MST.CoUser'),
        ),
        migrations.AddField(
            model_name='productinventory',
            name='UpdateUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Inven_UpdateUser', to='MST.CoUser'),
        ),
        migrations.AddField(
            model_name='productdetail_sr',
            name='ProdCode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Prod.ProductList'),
        ),
        migrations.AddField(
            model_name='productdetail_sr',
            name='RegUser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SR_RegUser', to='MST.CoUser'),
        ),
        migrations.AddField(
            model_name='productdetail_sr',
            name='UpdateUser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SR_UpdateUser', to='MST.CoUser'),
        ),
        migrations.AddField(
            model_name='productdetail_nt',
            name='ProdCode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Prod.ProductList'),
        ),
        migrations.AddField(
            model_name='productdetail_nt',
            name='RegUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='NT_RegUser', to='MST.CoUser'),
        ),
        migrations.AddField(
            model_name='productdetail_nt',
            name='UpdateUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='NT_UpdateUser', to='MST.CoUser'),
        ),
        migrations.AddField(
            model_name='productdetail_mt',
            name='ProdCode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Prod.ProductList'),
        ),
        migrations.AddField(
            model_name='productdetail_mt',
            name='RegUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='MT_RegUser', to='MST.CoUser'),
        ),
        migrations.AddField(
            model_name='productdetail_mt',
            name='UpdateUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='MT_UpdateUser', to='MST.CoUser'),
        ),
        migrations.AddField(
            model_name='productdetail_etc',
            name='ProdCode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Prod.ProductList'),
        ),
        migrations.AddField(
            model_name='productdetail_etc',
            name='RegUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ETC_RegUser', to='MST.CoUser'),
        ),
        migrations.AddField(
            model_name='productdetail_etc',
            name='UpdateUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ETC_UpdateUser', to='MST.CoUser'),
        ),
        migrations.AddField(
            model_name='productdetail_dt',
            name='ProdCode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Prod.ProductList'),
        ),
        migrations.AddField(
            model_name='productdetail_dt',
            name='RegUser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='DT_RegUser', to='MST.CoUser'),
        ),
        migrations.AddField(
            model_name='productdetail_dt',
            name='UpdateUser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='DT_UpdateUser', to='MST.CoUser'),
        ),
    ]
