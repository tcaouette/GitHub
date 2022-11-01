# Generated by Django 2.1.14 on 2020-04-29 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stg1_dataentryperson_ihab_abid_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_code', models.CharField(blank=True, db_column='SiteCode', max_length=5, null=True)),
                ('sample_id', models.CharField(blank=True, db_column='SampleID', max_length=50, null=True)),
                ('analyte', models.SmallIntegerField(blank=True, db_column='Analyte', null=True)),
                ('test_date', models.DateTimeField(blank=True, db_column='TestDate', null=True)),
                ('method', models.SmallIntegerField(blank=True, db_column='Method', null=True)),
                ('rep', models.SmallIntegerField(blank=True, db_column='Rep', null=True)),
                ('lot', models.CharField(blank=True, db_column='Lot', max_length=50, null=True)),
                ('lot_exp', models.DateTimeField(blank=True, db_column='LotExpDate', null=True)),
                ('exc_comments', models.TextField(blank=True, db_column='ExclusionComments', null=True)),
                ('misc_comments', models.TextField(blank=True, db_column='MiscComments', null=True)),
                ('date_entry_datetime', models.DateTimeField(auto_now_add=True, db_column='DateEntryTime')),
                ('i_well_1', models.SmallIntegerField(blank=True, db_column='Init_WellResult_1', null=True)),
                ('i_well_2', models.SmallIntegerField(blank=True, db_column='Init_WellResult_2', null=True)),
                ('i_well_3', models.SmallIntegerField(blank=True, db_column='Init_WellResult_3', null=True)),
                ('i_well_4', models.SmallIntegerField(blank=True, db_column='Init_WellResult_4', null=True)),
                ('i_well_5', models.SmallIntegerField(blank=True, db_column='Init_WellResult_5', null=True)),
                ('i_well_6', models.SmallIntegerField(blank=True, db_column='Init_WellResult_6', null=True)),
                ('i_well_7', models.SmallIntegerField(blank=True, db_column='Init_WellResult_7', null=True)),
                ('i_well_8', models.SmallIntegerField(blank=True, db_column='Init_WellResult_8', null=True)),
                ('i_well_9', models.SmallIntegerField(blank=True, db_column='Init_WellResult_9', null=True)),
                ('i_well_10', models.SmallIntegerField(blank=True, db_column='Init_WellResult_10', null=True)),
                ('i_well_11', models.SmallIntegerField(blank=True, db_column='Init_WellResult_11', null=True)),
                ('e_well_1', models.SmallIntegerField(blank=True, db_column='Edit_WellResult_1', null=True)),
                ('e_well_2', models.SmallIntegerField(blank=True, db_column='Edit_WellResult_2', null=True)),
                ('e_well_3', models.SmallIntegerField(blank=True, db_column='Edit_WellResult_3', null=True)),
                ('e_well_4', models.SmallIntegerField(blank=True, db_column='Edit_WellResult_4', null=True)),
                ('e_well_5', models.SmallIntegerField(blank=True, db_column='Edit_WellResult_5', null=True)),
                ('e_well_6', models.SmallIntegerField(blank=True, db_column='Edit_WellResult_6', null=True)),
                ('e_well_7', models.SmallIntegerField(blank=True, db_column='Edit_WellResult_7', null=True)),
                ('e_well_8', models.SmallIntegerField(blank=True, db_column='Edit_WellResult_8', null=True)),
                ('e_well_9', models.SmallIntegerField(blank=True, db_column='Edit_WellResult_9', null=True)),
                ('e_well_10', models.SmallIntegerField(blank=True, db_column='Edit_WellResult_10', null=True)),
                ('e_well_11', models.SmallIntegerField(blank=True, db_column='Edit_WellResult_11', null=True)),
                ('card_result', models.SmallIntegerField(blank=True, db_column='CardResult', null=True)),
                ('abid_interp', models.CharField(blank=True, db_column='AbID_Result', max_length=50, null=True)),
                ('date_insert', models.CharField(blank=True, db_column='Date_Inserted', max_length=50, null=True)),
                ('user', models.CharField(blank=True, db_column='User', max_length=50, null=True)),
            ],
            options={
                'db_table': 'stg1_dataentryperson_abid_1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='stg1_dataentryperson_ihab_abid_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_code', models.CharField(blank=True, db_column='SiteCode', max_length=5, null=True)),
                ('sample_id', models.CharField(blank=True, db_column='SampleID', max_length=50, null=True)),
                ('analyte', models.SmallIntegerField(blank=True, db_column='Analyte', null=True)),
                ('test_date', models.DateTimeField(blank=True, db_column='TestDate', null=True)),
                ('method', models.SmallIntegerField(blank=True, db_column='Method', null=True)),
                ('rep', models.SmallIntegerField(blank=True, db_column='Rep', null=True)),
                ('lot', models.CharField(blank=True, db_column='Lot', max_length=50, null=True)),
                ('lot_exp', models.DateTimeField(blank=True, db_column='LotExpDate', null=True)),
                ('exc_comments', models.TextField(blank=True, db_column='ExclusionComments', null=True)),
                ('misc_comments', models.TextField(blank=True, db_column='MiscComments', null=True)),
                ('date_entry_datetime', models.DateTimeField(auto_now_add=True, db_column='DateEntryTime')),
                ('i_well_1', models.SmallIntegerField(blank=True, db_column='Init_WellResult_1', null=True)),
                ('i_well_2', models.SmallIntegerField(blank=True, db_column='Init_WellResult_2', null=True)),
                ('i_well_3', models.SmallIntegerField(blank=True, db_column='Init_WellResult_3', null=True)),
                ('i_well_4', models.SmallIntegerField(blank=True, db_column='Init_WellResult_4', null=True)),
                ('i_well_5', models.SmallIntegerField(blank=True, db_column='Init_WellResult_5', null=True)),
                ('i_well_6', models.SmallIntegerField(blank=True, db_column='Init_WellResult_6', null=True)),
                ('i_well_7', models.SmallIntegerField(blank=True, db_column='Init_WellResult_7', null=True)),
                ('i_well_8', models.SmallIntegerField(blank=True, db_column='Init_WellResult_8', null=True)),
                ('i_well_9', models.SmallIntegerField(blank=True, db_column='Init_WellResult_9', null=True)),
                ('i_well_10', models.SmallIntegerField(blank=True, db_column='Init_WellResult_10', null=True)),
                ('i_well_11', models.SmallIntegerField(blank=True, db_column='Init_WellResult_11', null=True)),
                ('e_well_1', models.SmallIntegerField(blank=True, db_column='Edit_WellResult_1', null=True)),
                ('e_well_2', models.SmallIntegerField(blank=True, db_column='Edit_WellResult_2', null=True)),
                ('e_well_3', models.SmallIntegerField(blank=True, db_column='Edit_WellResult_3', null=True)),
                ('e_well_4', models.SmallIntegerField(blank=True, db_column='Edit_WellResult_4', null=True)),
                ('e_well_5', models.SmallIntegerField(blank=True, db_column='Edit_WellResult_5', null=True)),
                ('e_well_6', models.SmallIntegerField(blank=True, db_column='Edit_WellResult_6', null=True)),
                ('e_well_7', models.SmallIntegerField(blank=True, db_column='Edit_WellResult_7', null=True)),
                ('e_well_8', models.SmallIntegerField(blank=True, db_column='Edit_WellResult_8', null=True)),
                ('e_well_9', models.SmallIntegerField(blank=True, db_column='Edit_WellResult_9', null=True)),
                ('e_well_10', models.SmallIntegerField(blank=True, db_column='Edit_WellResult_10', null=True)),
                ('e_well_11', models.SmallIntegerField(blank=True, db_column='Edit_WellResult_11', null=True)),
                ('card_result', models.SmallIntegerField(blank=True, db_column='CardResult', null=True)),
                ('abid_interp', models.CharField(blank=True, db_column='AbID_Result', max_length=50, null=True)),
                ('date_insert', models.CharField(blank=True, db_column='Date_Inserted', max_length=50, null=True)),
                ('user', models.CharField(blank=True, db_column='User', max_length=50, null=True)),
            ],
            options={
                'db_table': 'stg1_dataentryperson_abid_2',
                'managed': False,
            },
        ),
    ]