# Generated by Django 2.1.15 on 2021-02-17 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rvpsyndromic', '0006_auto_20210216_0614'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tstg1brpcr',
            options={'managed': False},
        ),
        migrations.RemoveField(
            model_name='tstg1brpcrupdate',
            name='cov2_cq',
        ),
        migrations.RemoveField(
            model_name='tstg1brpcrupdate',
            name='cov2_interp',
        ),
        migrations.RemoveField(
            model_name='tstg1brpcrupdate',
            name='infa_cq',
        ),
        migrations.RemoveField(
            model_name='tstg1brpcrupdate',
            name='infa_interp',
        ),
        migrations.RemoveField(
            model_name='tstg1brpcrupdate',
            name='infb_cq',
        ),
        migrations.RemoveField(
            model_name='tstg1brpcrupdate',
            name='infb_interp',
        ),
        migrations.RemoveField(
            model_name='tstg1brpcrupdate',
            name='kitexp',
        ),
        migrations.RemoveField(
            model_name='tstg1brpcrupdate',
            name='kitlot',
        ),
        migrations.RemoveField(
            model_name='tstg1brpcrupdate',
            name='kitname',
        ),
        migrations.RemoveField(
            model_name='tstg1brpcrupdate',
            name='operator',
        ),
        migrations.RemoveField(
            model_name='tstg1brpcrupdate',
            name='rp_cq',
        ),
        migrations.RemoveField(
            model_name='tstg1brpcrupdate',
            name='rp_interp',
        ),
        migrations.RemoveField(
            model_name='tstg1brpcrupdate',
            name='sample',
        ),
        migrations.RemoveField(
            model_name='tstg1brpcrupdate',
            name='siteabbr',
        ),
        migrations.RemoveField(
            model_name='tstg1brpcrupdate',
            name='well',
        ),
        migrations.AddField(
            model_name='tstg1brpcrupdate',
            name='inv_equipment',
            field=models.CharField(blank=True, db_column='Inv_Equipment', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tstg1brpcrupdate',
            name='inv_infa_concentration',
            field=models.CharField(blank=True, db_column='Inv_InfA_Concentration', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tstg1brpcrupdate',
            name='inv_infa_interpretation',
            field=models.CharField(blank=True, db_column='Inv_InfA_Interpretation', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tstg1brpcrupdate',
            name='inv_infb_concentration',
            field=models.CharField(blank=True, db_column='Inv_InfB_Concentration', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tstg1brpcrupdate',
            name='inv_infb_interpretation',
            field=models.CharField(blank=True, db_column='Inv_InfB_Interpretation', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tstg1brpcrupdate',
            name='inv_kit_expiration_date',
            field=models.DateTimeField(blank=True, db_column='Inv_Kit_Expiration_Date', null=True),
        ),
        migrations.AddField(
            model_name='tstg1brpcrupdate',
            name='inv_kit_lotid',
            field=models.CharField(blank=True, db_column='Inv_Kit_LotID', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tstg1brpcrupdate',
            name='inv_kit_name',
            field=models.CharField(blank=True, db_column='Inv_Kit_Name', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tstg1brpcrupdate',
            name='inv_notes',
            field=models.TextField(blank=True, db_column='Inv_Notes', null=True),
        ),
        migrations.AddField(
            model_name='tstg1brpcrupdate',
            name='inv_operator',
            field=models.CharField(blank=True, db_column='Inv_Operator', max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='tstg1brpcrupdate',
            name='inv_rp_concentration',
            field=models.CharField(blank=True, db_column='Inv_RP_Concentration', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tstg1brpcrupdate',
            name='inv_rp_interpretation',
            field=models.CharField(blank=True, db_column='Inv_RP_Interpretation', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tstg1brpcrupdate',
            name='inv_sarscov2_concentration',
            field=models.CharField(blank=True, db_column='Inv_Sarscov2_Concentration', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tstg1brpcrupdate',
            name='inv_sarscov2_interpretation',
            field=models.CharField(blank=True, db_column='Inv_Sarscov2_Interpretation', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tstg1brpcrupdate',
            name='inv_site',
            field=models.CharField(blank=True, db_column='Inv_Site', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tstg1brpcrupdate',
            name='inv_test_date',
            field=models.DateTimeField(blank=True, db_column='Inv_Test_Date', null=True),
        ),
        migrations.AddField(
            model_name='tstg1brpcrupdate',
            name='inv_test_name',
            field=models.CharField(blank=True, db_column='Inv_Test_Name', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tstg1brpcrupdate',
            name='inv_well_id',
            field=models.CharField(blank=True, db_column='Inv_Well_ID', max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='tstg1brpcrupdate',
            name='sampleid',
            field=models.CharField(blank=True, db_column='SampleID', max_length=25, null=True),
        ),
    ]
