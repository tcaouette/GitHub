# Generated by Django 2.1.15 on 2021-03-01 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rvpsyndromic', '0008_auto_20210219_1454'),
    ]

    operations = [
        migrations.CreateModel(
            name='TStg2Ad',
            fields=[
                ('sampleid', models.CharField(blank=True, db_column='SampleID', max_length=25, primary_key=True, serialize=False)),
                ('inv_site', models.CharField(blank=True, db_column='Inv_Site', max_length=255, null=True)),
                ('inv_equipment', models.CharField(blank=True, db_column='Inv_Equipment', max_length=255, null=True)),
                ('inv_test_name', models.CharField(blank=True, db_column='Inv_Test_Name', max_length=255, null=True)),
                ('inv_test_date', models.CharField(blank=True, db_column='Inv_Test_Date', max_length=25, null=True)),
                ('inv_operator', models.CharField(blank=True, db_column='Inv_Operator', max_length=25, null=True)),
                ('inv_well_id', models.CharField(blank=True, db_column='Inv_Well_ID', max_length=25, null=True)),
                ('inv_sarscov2_concentration', models.CharField(blank=True, db_column='Inv_Sarscov2_Concentration', max_length=255, null=True)),
                ('inv_infa_concentration', models.CharField(blank=True, db_column='Inv_InfA_Concentration', max_length=255, null=True)),
                ('inv_infb_concentration', models.CharField(blank=True, db_column='Inv_InfB_Concentration', max_length=255, null=True)),
                ('inv_rp_concentration', models.CharField(blank=True, db_column='Inv_RP_Concentration', max_length=255, null=True)),
                ('inv_sarscov2_interpretation', models.CharField(blank=True, db_column='Inv_Sarscov2_Interpretation', max_length=255, null=True)),
                ('inv_infa_interpretation', models.CharField(blank=True, db_column='Inv_InfA_Interpretation', max_length=255, null=True)),
                ('inv_infb_interpretation', models.CharField(blank=True, db_column='Inv_InfB_Interpretation', max_length=255, null=True)),
                ('inv_rp_interpretation', models.CharField(blank=True, db_column='Inv_RP_Interpretation', max_length=255, null=True)),
                ('reffluoperator', models.CharField(blank=True, db_column='RefFluOperator', max_length=255, null=True)),
                ('refflukitname', models.CharField(blank=True, db_column='RefFluKitName', max_length=255, null=True)),
                ('refflu_date', models.CharField(blank=True, db_column='RefFlu_Date', max_length=25, null=True)),
                ('refflua_well', models.CharField(blank=True, db_column='RefFluA_Well', max_length=5, null=True)),
                ('refflub_well', models.CharField(blank=True, db_column='RefFluB_Well', max_length=5, null=True)),
                ('refrsv_well', models.CharField(blank=True, db_column='RefRSV_Well', max_length=5, null=True)),
                ('refflua_cqvalue', models.CharField(blank=True, db_column='RefFluA_CqValue', max_length=25, null=True)),
                ('refflub_cqvalue', models.CharField(blank=True, db_column='RefFluB_CqValue', max_length=25, null=True)),
                ('refrsv_cqvalue', models.CharField(blank=True, db_column='RefRSV_CqValue', max_length=25, null=True)),
                ('refflua_interp', models.CharField(blank=True, db_column='RefFluA_Interp', max_length=25, null=True)),
                ('refflub_interp', models.CharField(blank=True, db_column='RefFluB_Interp', max_length=25, null=True)),
                ('refrsv_interp', models.CharField(blank=True, db_column='RefRSV_Interp', max_length=25, null=True)),
                ('refcov2_test_name', models.CharField(blank=True, db_column='RefCov2_Test_Name', max_length=255, null=True)),
                ('refcov2_test_date', models.CharField(blank=True, db_column='RefCov2_Test_Date', max_length=25, null=True)),
                ('refcov2_kit_name', models.CharField(blank=True, db_column='RefCov2_Kit_Name', max_length=255, null=True)),
                ('refcov2_operator', models.CharField(blank=True, db_column='RefCov2_Operator', max_length=255, null=True)),
                ('refcov2_well_id', models.CharField(blank=True, db_column='RefCov2_Well_ID', max_length=255, null=True)),
                ('refcov2_n1_concentration', models.CharField(blank=True, db_column='RefCov2_N1_Concentration', max_length=25, null=True)),
                ('refcov2_n2_concentration', models.CharField(blank=True, db_column='RefCov2_N2_Concentration', max_length=25, null=True)),
                ('refcov2_rp_concentration', models.CharField(blank=True, db_column='RefCov2_RP_Concentration', max_length=25, null=True)),
                ('refcov2_n1_droplet_count', models.CharField(blank=True, db_column='RefCov2_N1_Droplet_Count', max_length=25, null=True)),
                ('refcov2_n2_droplet_count', models.CharField(blank=True, db_column='RefCov2_N2_Droplet_Count', max_length=25, null=True)),
                ('refcov2_rp_droplet_count', models.CharField(blank=True, db_column='RefCov2_RP_Droplet_Count', max_length=25, null=True)),
                ('refcov2_result_interpretation', models.CharField(blank=True, db_column='RefCov2_Result_Interpretation', max_length=255, null=True)),
                ('inv_notes', models.TextField(blank=True, db_column='Inv_Notes', null=True)),
                ('ref_notes', models.TextField(blank=True, db_column='Ref_Notes', null=True)),
            ],
            options={
                'db_table': 't_stg2_AD',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TStg2Demo',
            fields=[
                ('subjectid', models.CharField(blank=True, db_column='SubjectID', max_length=25, primary_key=True, serialize=False)),
                ('specimenid', models.CharField(blank=True, db_column='SpecimenID', max_length=25, null=True)),
                ('subject_age', models.CharField(blank=True, db_column='Subject_Age', max_length=25, null=True)),
                ('subject_sex', models.CharField(blank=True, db_column='Subject_Sex', max_length=3, null=True)),
                ('subject_race', models.CharField(blank=True, db_column='Subject_Race', max_length=50, null=True)),
                ('subject_ethnicity', models.CharField(blank=True, db_column='Subject_Ethnicity', max_length=50, null=True)),
                ('collection_date', models.CharField(blank=True, db_column='Collection_Date', max_length=25, null=True)),
                ('symptom_date', models.CharField(blank=True, db_column='Symptom_Date', max_length=25, null=True)),
                ('symptom_desc', models.TextField(blank=True, db_column='Symptom_Desc', null=True)),
                ('symptom_cough', models.CharField(blank=True, db_column='Symptom_Cough', max_length=3, null=True)),
                ('symptom_conges', models.CharField(blank=True, db_column='Symptom_Conges', max_length=3, null=True)),
                ('symptom_rhinorrhea', models.CharField(blank=True, db_column='Symptom_Rhinorrhea', max_length=3, null=True)),
                ('symptom_sore_throat', models.CharField(blank=True, db_column='Symptom_Sore_Throat', max_length=3, null=True)),
                ('symptom_fever', models.CharField(blank=True, db_column='Symptom_Fever', max_length=3, null=True)),
                ('symptom_headache', models.CharField(blank=True, db_column='Symptom_Headache', max_length=3, null=True)),
                ('symptom_myalgia', models.CharField(blank=True, db_column='Symptom_Myalgia', max_length=3, null=True)),
                ('symptom_other', models.TextField(blank=True, db_column='Symptom_Other', null=True)),
                ('symptom_hospitalized', models.CharField(blank=True, db_column='Symptom_Hospitalized', max_length=25, null=True)),
                ('influzab_kitname', models.CharField(blank=True, db_column='InfluzAB_KitName', max_length=255, null=True)),
                ('influza_testresult', models.CharField(blank=True, db_column='InfluzA_TestResult', max_length=25, null=True)),
                ('influza_ctvalue', models.CharField(blank=True, db_column='InfluzA_CTvalue', max_length=25, null=True)),
                ('influzb_testresult', models.CharField(blank=True, db_column='InfluzB_TestResult', max_length=25, null=True)),
                ('influzb_ctvalue', models.CharField(blank=True, db_column='InfluzB_CTvalue', max_length=25, null=True)),
                ('rsv_kitname', models.CharField(blank=True, db_column='RSV_KitName', max_length=255, null=True)),
                ('rsv_testvalue', models.CharField(blank=True, db_column='RSV_TestValue', max_length=25, null=True)),
                ('rsv_ctvalues', models.CharField(blank=True, db_column='RSV_CTvalues', max_length=25, null=True)),
                ('cov2_kitname', models.CharField(blank=True, db_column='COV2_KitName', max_length=255, null=True)),
                ('cov2_testresult', models.CharField(blank=True, db_column='COV2_TestResult', max_length=25, null=True)),
                ('cov2_ctvalue', models.CharField(blank=True, db_column='COV2_CTvalue', max_length=25, null=True)),
                ('excl_flag', models.IntegerField(blank=True, db_column='Excl_Flag', null=True)),
                ('userid', models.CharField(blank=True, max_length=255, null=True)),
                ('post_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 't_stg2_DEMO',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TStg2Subjexcl',
            fields=[
                ('subjectid', models.CharField(blank=True, db_column='SubjectID', max_length=25, primary_key=True, serialize=False)),
                ('specimenid', models.CharField(blank=True, db_column='SpecimenID', max_length=25, null=True)),
                ('subject_age', models.CharField(blank=True, db_column='Subject_Age', max_length=25, null=True)),
                ('subject_sex', models.CharField(blank=True, db_column='Subject_Sex', max_length=3, null=True)),
                ('subject_race', models.CharField(blank=True, db_column='Subject_Race', max_length=50, null=True)),
                ('subject_ethnicity', models.CharField(blank=True, db_column='Subject_Ethnicity', max_length=50, null=True)),
                ('collection_date', models.CharField(blank=True, db_column='Collection_Date', max_length=25, null=True)),
                ('symptom_date', models.CharField(blank=True, db_column='Symptom_Date', max_length=25, null=True)),
                ('symptom_desc', models.TextField(blank=True, db_column='Symptom_Desc', null=True)),
                ('symptom_cough', models.CharField(blank=True, db_column='Symptom_Cough', max_length=3, null=True)),
                ('symptom_conges', models.CharField(blank=True, db_column='Symptom_Conges', max_length=3, null=True)),
                ('symptom_rhinorrhea', models.CharField(blank=True, db_column='Symptom_Rhinorrhea', max_length=3, null=True)),
                ('symptom_sore_throat', models.CharField(blank=True, db_column='Symptom_Sore_Throat', max_length=3, null=True)),
                ('symptom_fever', models.CharField(blank=True, db_column='Symptom_Fever', max_length=3, null=True)),
                ('symptom_headache', models.CharField(blank=True, db_column='Symptom_Headache', max_length=3, null=True)),
                ('symptom_myalgia', models.CharField(blank=True, db_column='Symptom_Myalgia', max_length=3, null=True)),
                ('symptom_other', models.TextField(blank=True, db_column='Symptom_Other', null=True)),
                ('symptom_hospitalized', models.CharField(blank=True, db_column='Symptom_Hospitalized', max_length=25, null=True)),
                ('influzab_kitname', models.CharField(blank=True, db_column='InfluzAB_KitName', max_length=255, null=True)),
                ('influza_testresult', models.CharField(blank=True, db_column='InfluzA_TestResult', max_length=25, null=True)),
                ('influza_ctvalue', models.CharField(blank=True, db_column='InfluzA_CTvalue', max_length=25, null=True)),
                ('influzb_testresult', models.CharField(blank=True, db_column='InfluzB_TestResult', max_length=25, null=True)),
                ('influzb_ctvalue', models.CharField(blank=True, db_column='InfluzB_CTvalue', max_length=25, null=True)),
                ('rsv_kitname', models.CharField(blank=True, db_column='RSV_KitName', max_length=255, null=True)),
                ('rsv_testvalue', models.CharField(blank=True, db_column='RSV_TestValue', max_length=25, null=True)),
                ('rsv_ctvalues', models.CharField(blank=True, db_column='RSV_CTvalues', max_length=25, null=True)),
                ('cov2_kitname', models.CharField(blank=True, db_column='COV2_KitName', max_length=255, null=True)),
                ('cov2_testresult', models.CharField(blank=True, db_column='COV2_TestResult', max_length=25, null=True)),
                ('cov2_ctvalue', models.CharField(blank=True, db_column='COV2_CTvalue', max_length=25, null=True)),
                ('excl_flag', models.IntegerField(blank=True, db_column='Excl_Flag', null=True)),
                ('userid', models.CharField(blank=True, max_length=255, null=True)),
                ('post_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 't_stg2_SUBJEXCL',
                'managed': False,
            },
        ),
    ]