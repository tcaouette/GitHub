# Generated by Django 2.1.14 on 2020-01-08 00:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dtproperties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectid', models.IntegerField(blank=True, null=True)),
                ('property', models.CharField(max_length=64)),
                ('value', models.CharField(blank=True, max_length=255, null=True)),
                ('uvalue', models.CharField(blank=True, max_length=255, null=True)),
                ('lvalue', models.BinaryField(blank=True, null=True)),
                ('version', models.IntegerField()),
            ],
            options={
                'db_table': 'dtproperties',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sysdiagrams',
            fields=[
                ('name', models.CharField(max_length=128)),
                ('principal_id', models.IntegerField()),
                ('diagram_id', models.AutoField(primary_key=True, serialize=False)),
                ('version', models.IntegerField(blank=True, null=True)),
                ('definition', models.BinaryField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sysdiagrams',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tblaliquotbdm3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boxid_grid', models.CharField(blank=True, db_column='BoxID-Grid', max_length=255, null=True)),
                ('boxid', models.CharField(blank=True, db_column='BoxID', max_length=255, null=True)),
                ('boxcombo', models.CharField(blank=True, db_column='BoxCombo', max_length=255, null=True)),
                ('grid', models.CharField(blank=True, db_column='Grid', max_length=255, null=True)),
                ('invdate', models.DateTimeField(blank=True, db_column='InvDate', null=True)),
                ('invuser', models.CharField(blank=True, db_column='InvUser', max_length=255, null=True)),
            ],
            options={
                'db_table': 'tblAliquotBDM3',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tlkupcages',
            fields=[
                ('cagenumber', models.CharField(db_column='CageNumber', max_length=20, primary_key=True, serialize=False)),
                ('keynumber', models.CharField(blank=True, db_column='KeyNumber', max_length=10, null=True)),
            ],
            options={
                'db_table': 'tlkupCages',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tlkupcanes',
            fields=[
                ('canenum', models.CharField(db_column='CaneNum', max_length=10, primary_key=True, serialize=False)),
                ('canecapacity', models.IntegerField(blank=True, db_column='CaneCapacity', null=True)),
                ('caneinfo', models.CharField(blank=True, db_column='CaneInfo', max_length=50, null=True)),
            ],
            options={
                'db_table': 'tlkupCanes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tlkupfreezers',
            fields=[
                ('freezer', models.CharField(db_column='Freezer', max_length=10, primary_key=True, serialize=False)),
                ('freezertemp', models.CharField(db_column='FreezerTemp', max_length=10)),
                ('freezerloc', models.CharField(blank=True, db_column='FreezerLoc', max_length=50, null=True)),
            ],
            options={
                'db_table': 'tlkupFreezers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tdemogroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specid', models.CharField(db_column='SpecID', max_length=20)),
                ('age', models.SmallIntegerField(blank=True, db_column='Age', null=True)),
                ('gender', models.CharField(blank=True, db_column='Gender', max_length=5, null=True)),
                ('a', models.CharField(blank=True, db_column='A', max_length=50, null=True)),
                ('demogroup', models.CharField(db_column='DemoGroup', max_length=60)),
            ],
            options={
                'db_table': 'tDemoGroups',
            },
        ),
        migrations.CreateModel(
            name='TLinkAqlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aqid', models.CharField(db_column='AqID', max_length=50)),
                ('lotid', models.CharField(blank=True, db_column='LotID', max_length=10, null=True)),
                ('originalid', models.CharField(db_column='OriginalID', max_length=255)),
                ('verified', models.SmallIntegerField(blank=True, db_column='Verified', null=True)),
            ],
            options={
                'db_table': 't_link_AqLot',
            },
        ),
        migrations.CreateModel(
            name='TLinkLotkey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aqid', models.IntegerField(blank=True, db_column='AqID', null=True)),
                ('lotid', models.CharField(db_column='LotID', max_length=10)),
                ('originalid', models.CharField(db_column='OriginalID', max_length=30)),
                ('duplicate', models.CharField(blank=True, db_column='Duplicate', max_length=10, null=True)),
                ('verified', models.SmallIntegerField(blank=True, db_column='Verified', null=True)),
            ],
            options={
                'db_table': 't_link_LotKey',
            },
        ),
        migrations.CreateModel(
            name='TLinkPerpan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('originalid', models.CharField(blank=True, db_column='OriginalID', max_length=50, null=True)),
                ('panelname', models.CharField(db_column='PanelName', max_length=20)),
            ],
            options={
                'db_table': 't_link_PerPan',
            },
        ),
        migrations.CreateModel(
            name='TLinkRestrictions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resid', models.IntegerField(db_column='ResID')),
                ('aqid', models.CharField(db_column='AqID', max_length=50)),
                ('resvol', models.DecimalField(db_column='ResVol', decimal_places=3, max_digits=8)),
                ('resstatus', models.SmallIntegerField(db_column='ResStatus')),
            ],
            options={
                'db_table': 't_link_Restrictions',
            },
        ),
        migrations.CreateModel(
            name='TListInventorya',
            fields=[
                ('aqid', models.CharField(db_column='AqID', max_length=50, primary_key=True, serialize=False)),
                ('originalid', models.CharField(blank=True, db_column='OriginalID', max_length=255, null=True)),
                ('grid', models.CharField(db_column='Grid', max_length=50)),
                ('labelinfo', models.TextField(db_column='LabelInfo')),
                ('volume', models.DecimalField(blank=True, db_column='Volume', decimal_places=3, max_digits=8, null=True)),
                ('insertdate', models.DateTimeField(db_column='InsertDate')),
                ('invnum', models.IntegerField(db_column='InvNum')),
                ('invcomment', models.TextField(blank=True, db_column='InvComment', null=True)),
            ],
            options={
                'db_table': 't_list_InventoryA',
            },
        ),
        migrations.CreateModel(
            name='TListInventoryb',
            fields=[
                ('freezer', models.CharField(db_column='Freezer', max_length=100)),
                ('cage', models.CharField(db_column='Cage', max_length=50)),
                ('cane', models.CharField(blank=True, db_column='Cane', max_length=50, null=True)),
                ('stack', models.CharField(blank=True, db_column='Stack', max_length=50, null=True)),
                ('boxid', models.CharField(db_column='BoxID', max_length=200, primary_key=True, serialize=False)),
                ('invnum', models.IntegerField(db_column='InvNum')),
                ('insertdate', models.DateTimeField(db_column='InsertDate')),
                ('invcomment', models.TextField(blank=True, db_column='InvComment', null=True)),
            ],
            options={
                'db_table': 't_list_InventoryB',
            },
        ),
        migrations.CreateModel(
            name='TListInventorybBak24Sep',
            fields=[
                ('freezer', models.CharField(db_column='Freezer', max_length=100)),
                ('cage', models.CharField(db_column='Cage', max_length=50)),
                ('cane', models.CharField(blank=True, db_column='Cane', max_length=50, null=True)),
                ('stack', models.CharField(blank=True, db_column='Stack', max_length=50, null=True)),
                ('boxid', models.CharField(db_column='BoxID', max_length=200)),
                ('invdate', models.DateTimeField(db_column='InvDate')),
                ('invuser', models.CharField(db_column='InvUser', max_length=50)),
                ('invcomments', models.TextField(db_column='InvComments')),
                ('transnum', models.AutoField(db_column='TransNum', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 't_list_InventoryB_bak24SEP',
            },
        ),
        migrations.CreateModel(
            name='Tmphivsummary110',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plotid', models.CharField(blank=True, db_column='PLotID', max_length=20, null=True)),
                ('poriginalid', models.CharField(blank=True, db_column='POriginalID', max_length=20, null=True)),
                ('lotid', models.CharField(blank=True, db_column='LotID', max_length=20, null=True)),
                ('orignalid', models.CharField(blank=True, db_column='OrignalID', max_length=50, null=True)),
                ('pmatrix', models.CharField(blank=True, db_column='Pmatrix', max_length=50, null=True)),
                ('pdx', models.CharField(blank=True, db_column='PDx', max_length=50, null=True)),
                ('psource', models.CharField(blank=True, db_column='Psource', max_length=100, null=True)),
                ('pdrawdt', models.DateTimeField(blank=True, db_column='PDrawDt', null=True)),
                ('precdt', models.DateTimeField(blank=True, db_column='PRecDt', null=True)),
                ('manufacturer', models.CharField(blank=True, db_column='Manufacturer', max_length=50, null=True)),
                ('assaygrp', models.CharField(blank=True, db_column='AssayGrp', max_length=50, null=True)),
                ('assayname', models.CharField(blank=True, db_column='AssayName', max_length=50, null=True)),
                ('abag', models.CharField(blank=True, db_column='AbAg', max_length=10, null=True)),
                ('analyte', models.CharField(blank=True, db_column='Analyte', max_length=20, null=True)),
                ('pinter', models.CharField(blank=True, db_column='Pinter', max_length=20, null=True)),
                ('bands', models.TextField(blank=True, db_column='Bands', null=True)),
            ],
            options={
                'db_table': 'tmpHIVSummary_110',
            },
        ),
        migrations.CreateModel(
            name='Tmppediatrics110',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lotid', models.CharField(blank=True, db_column='LotID', max_length=10, null=True)),
                ('originalid', models.CharField(blank=True, db_column='OriginalID', max_length=30, null=True)),
                ('specid', models.CharField(blank=True, db_column='SpecID', max_length=20, null=True)),
                ('age', models.IntegerField(blank=True, db_column='Age', null=True)),
                ('gender', models.CharField(blank=True, db_column='Gender', max_length=50, null=True)),
                ('demogroup', models.CharField(blank=True, db_column='DemoGroup', max_length=50, null=True)),
                ('riskgroup', models.CharField(db_column='RiskGroup', max_length=50)),
                ('studydesc', models.CharField(blank=True, db_column='StudyDesc', max_length=255, null=True)),
                ('volume', models.DecimalField(blank=True, db_column='Volume', decimal_places=3, max_digits=8, null=True)),
            ],
            options={
                'db_table': 'tmpPediatrics_110',
            },
        ),
        migrations.CreateModel(
            name='TmpRefRiskgroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('riskcategory', models.CharField(db_column='RiskCategory', max_length=20)),
                ('riskgroupdesc', models.CharField(blank=True, db_column='RiskGroupDesc', max_length=200, null=True)),
                ('riskgroupid', models.IntegerField(db_column='RiskGroupID')),
            ],
            options={
                'db_table': 'tmp_ref_RiskGroups',
            },
        ),
        migrations.CreateModel(
            name='TmpUpInventorya',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aqid', models.CharField(blank=True, db_column='AqID', max_length=511, null=True)),
                ('specimenid', models.CharField(blank=True, db_column='SpecimenID', max_length=255, null=True)),
                ('boxid', models.CharField(blank=True, db_column='BoxID', max_length=255, null=True)),
                ('grid', models.CharField(blank=True, db_column='Grid', max_length=255, null=True)),
                ('labelinfo', models.TextField(blank=True, db_column='LabelInfo', null=True)),
                ('volume', models.FloatField(blank=True, db_column='Volume', null=True)),
                ('insertdate', models.DateTimeField(blank=True, db_column='InsertDate', null=True)),
                ('invnum', models.IntegerField(db_column='InvNum')),
                ('invcomment', models.TextField(blank=True, db_column='InvComment', null=True)),
            ],
            options={
                'db_table': 'tmp_up_InventoryA',
            },
        ),
        migrations.CreateModel(
            name='TRefDataidkey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sheet', models.TextField(blank=True, db_column='Sheet', null=True)),
                ('lotid', models.CharField(blank=True, db_column='LotID', max_length=10, null=True)),
                ('originalid', models.CharField(blank=True, db_column='OriginalID', max_length=30, null=True)),
                ('idstatus', models.CharField(blank=True, db_column='IDStatus', max_length=15, null=True)),
                ('idconfirmed', models.DateTimeField(blank=True, db_column='IDConfirmed', null=True)),
                ('pkid', models.IntegerField(db_column='PK')),
            ],
            options={
                'db_table': 't_ref_DataIDKEY',
            },
        ),
        migrations.CreateModel(
            name='TRefDepartments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deptcode', models.CharField(db_column='DeptCode', max_length=20)),
                ('deptname', models.CharField(db_column='DeptName', max_length=50)),
                ('divcode', models.CharField(db_column='DivCode', max_length=20)),
                ('divname', models.CharField(db_column='DivName', max_length=50)),
                ('groupcode', models.CharField(db_column='GroupCode', max_length=20)),
                ('groupname', models.CharField(db_column='GroupName', max_length=50)),
                ('oldcode', models.CharField(blank=True, db_column='OldCode', max_length=10, null=True)),
                ('oldname', models.CharField(blank=True, db_column='OldName', max_length=50, null=True)),
                ('link', models.TextField(blank=True, db_column='Link', null=True)),
            ],
            options={
                'db_table': 't_ref_Departments',
            },
        ),
        migrations.CreateModel(
            name='TRefInventories',
            fields=[
                ('invnum', models.AutoField(db_column='InvNum', primary_key=True, serialize=False)),
                ('invenddate', models.DateTimeField(db_column='InvEndDate')),
                ('invuser', models.CharField(db_column='InvUser', max_length=50)),
                ('invtype', models.CharField(db_column='InvType', max_length=50)),
            ],
            options={
                'db_table': 't_ref_Inventories',
            },
        ),
        migrations.CreateModel(
            name='TRefLocations',
            fields=[
                ('locgrid', models.CharField(db_column='LocGrid', max_length=50, primary_key=True, serialize=False)),
                ('freezernum', models.CharField(db_column='FreezerNum', max_length=10)),
                ('canenum', models.CharField(db_column='CaneNum', max_length=10)),
                ('cagenum', models.CharField(db_column='CageNum', max_length=20)),
                ('canegrid', models.CharField(db_column='CaneGrid', max_length=20)),
                ('keynumber', models.CharField(blank=True, db_column='KeyNumber', max_length=10, null=True)),
                ('freezertemp', models.CharField(blank=True, db_column='FreezerTemp', max_length=10, null=True)),
                ('room', models.TextField(blank=True, db_column='Room', null=True)),
            ],
            options={
                'db_table': 't_ref_Locations',
            },
        ),
        migrations.CreateModel(
            name='TRefLotsRisk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pkid', models.IntegerField(db_column='PK')),
                ('lotid', models.CharField(db_column='LotID', max_length=10)),
                ('originalid', models.CharField(blank=True, db_column='OriginalID', max_length=255, null=True)),
                ('risk_dx1', models.CharField(blank=True, db_column='Risk_Dx1', max_length=255, null=True)),
                ('risk_dx2', models.CharField(blank=True, db_column='Risk_Dx2', max_length=255, null=True)),
                ('risk_dx3', models.CharField(blank=True, db_column='Risk_Dx3', max_length=255, null=True)),
                ('dateverified', models.DateTimeField(blank=True, db_column='DateVerified', null=True)),
            ],
            options={
                'db_table': 't_ref_Lots_Risk',
            },
        ),
        migrations.CreateModel(
            name='TRefLotsSam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pkid', models.IntegerField(db_column='PK')),
                ('lotid', models.CharField(db_column='LotID', max_length=10)),
                ('originalid', models.CharField(blank=True, db_column='OriginalID', max_length=255, null=True)),
                ('samprepid', models.IntegerField(blank=True, db_column='SamPrepID', null=True)),
                ('samtypeid', models.IntegerField(blank=True, db_column='SamTypeID', null=True)),
                ('samapperance', models.CharField(blank=True, db_column='SamApperance', max_length=255, null=True)),
                ('vol_initial', models.DecimalField(blank=True, db_column='Vol_Initial', decimal_places=3, max_digits=8, null=True)),
                ('dateverified', models.DateTimeField(blank=True, db_column='DateVerified', null=True)),
            ],
            options={
                'db_table': 't_ref_Lots_Sam',
            },
        ),
        migrations.CreateModel(
            name='TRefLotsSource',
            fields=[
                ('pkid', models.AutoField(db_column='PK', primary_key=True, serialize=False)),
                ('lotid', models.CharField(db_column='LotID', max_length=10)),
                ('originalid', models.CharField(blank=True, db_column='OriginalID', max_length=255, null=True)),
                ('costperml', models.DecimalField(blank=True, db_column='CostPerMl', decimal_places=4, max_digits=19, null=True)),
                ('datepurchased', models.DateTimeField(blank=True, db_column='DatePurchased', null=True)),
                ('datecollected', models.DateTimeField(blank=True, db_column='DateCollected', null=True)),
                ('vendor', models.CharField(blank=True, db_column='Vendor', max_length=255, null=True)),
                ('country', models.CharField(blank=True, db_column='Country', max_length=255, null=True)),
                ('collectionloc', models.CharField(blank=True, db_column='CollectionLoc', max_length=255, null=True)),
                ('lotowner', models.CharField(blank=True, db_column='LotOwner', max_length=255, null=True)),
                ('lottrialsource', models.CharField(blank=True, db_column='LotTrialSource', max_length=255, null=True)),
                ('dateverified', models.DateTimeField(blank=True, db_column='DateVerified', null=True)),
            ],
            options={
                'db_table': 't_ref_Lots_Source',
            },
        ),
        migrations.CreateModel(
            name='TRefPanels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(db_column='Manufacturer', max_length=200)),
                ('panelname', models.CharField(db_column='PanelName', max_length=20)),
                ('paneltype', models.CharField(db_column='PanelType', max_length=255)),
                ('paneldesc', models.TextField(db_column='PanelDesc')),
                ('membernum', models.IntegerField(blank=True, db_column='MemberNum', null=True)),
            ],
            options={
                'db_table': 't_ref_Panels',
            },
        ),
        migrations.CreateModel(
            name='TRefRestrictions',
            fields=[
                ('resid', models.AutoField(db_column='ResID', primary_key=True, serialize=False)),
                ('resdept', models.CharField(blank=True, db_column='ResDept', max_length=20, null=True)),
                ('respersonnel', models.CharField(db_column='ResPersonnel', max_length=50)),
                ('resexpiration', models.DateTimeField(db_column='ResExpiration')),
                ('resdesc', models.TextField(blank=True, db_column='ResDesc', null=True)),
            ],
            options={
                'db_table': 't_ref_Restrictions',
            },
        ),
        migrations.CreateModel(
            name='TRefRiskgroups',
            fields=[
                ('riskcatid', models.AutoField(db_column='RiskCatID', primary_key=True, serialize=False)),
                ('riskcategory', models.CharField(db_column='RiskCategory', max_length=255)),
                ('riskcatdesc', models.TextField(blank=True, db_column='RiskCatDesc', null=True)),
            ],
            options={
                'db_table': 't_ref_RiskGroups',
            },
        ),
        migrations.CreateModel(
            name='TRefSamplepreparations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('samprepid', models.IntegerField(db_column='SamPrepID')),
                ('samprepdesc', models.CharField(blank=True, db_column='SamPrepDesc', max_length=255, null=True)),
            ],
            options={
                'db_table': 't_ref_SamplePreparations',
            },
        ),
        migrations.CreateModel(
            name='TRefSampletypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('samtypeid', models.IntegerField(db_column='SamTypeID')),
                ('samtypedesc', models.CharField(blank=True, db_column='SamTypeDesc', max_length=100, null=True)),
            ],
            options={
                'db_table': 't_ref_SampleTypes',
            },
        ),
        migrations.CreateModel(
            name='TRefTransactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transnum', models.CharField(db_column='TransNum', max_length=50)),
                ('issuedest', models.CharField(db_column='IssueDest', max_length=10)),
                ('issueuser', models.CharField(blank=True, db_column='IssueUser', max_length=100, null=True)),
                ('issuedate', models.DateTimeField(blank=True, db_column='IssueDate', null=True)),
                ('issuereason', models.TextField(blank=True, db_column='IssueReason', null=True)),
            ],
            options={
                'db_table': 't_ref_Transactions',
            },
        ),
        migrations.CreateModel(
            name='Triskgroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perid', models.CharField(blank=True, db_column='PerID', max_length=50, null=True)),
                ('lotid', models.CharField(blank=True, db_column='LotID', max_length=50, null=True)),
                ('trialkey', models.IntegerField(blank=True, db_column='TrialKey', null=True)),
                ('originalid', models.CharField(blank=True, db_column='OriginalID', max_length=30, null=True)),
                ('specid', models.CharField(db_column='SpecID', max_length=20)),
                ('studyid', models.CharField(blank=True, db_column='StudyID', max_length=10, null=True)),
                ('studydesc', models.CharField(blank=True, db_column='StudyDesc', max_length=200, null=True)),
                ('riskgroupid', models.SmallIntegerField(blank=True, db_column='RiskGroupID', null=True)),
                ('dup', models.IntegerField(blank=True, db_column='Dup', null=True)),
                ('comments', models.TextField(blank=True, db_column='Comments', null=True)),
            ],
            options={
                'db_table': 'tRiskGroups',
            },
        ),
        migrations.CreateModel(
            name='Ttrialids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trialkey', models.IntegerField(blank=True, db_column='TrialKey', null=True)),
                ('aqid', models.IntegerField(blank=True, db_column='AqID', null=True)),
                ('lotid', models.CharField(blank=True, db_column='LotID', max_length=10, null=True)),
                ('originalid', models.CharField(blank=True, db_column='OriginalID', max_length=100, null=True)),
                ('specid', models.CharField(blank=True, db_column='SpecID', max_length=20, null=True)),
                ('volreq', models.DecimalField(blank=True, db_column='Volreq', decimal_places=3, max_digits=8, null=True)),
                ('issued', models.SmallIntegerField(blank=True, db_column='Issued', null=True)),
            ],
            options={
                'db_table': 'tTrialIDs',
            },
        ),
        migrations.CreateModel(
            name='Ttrials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trialkey', models.IntegerField(blank=True, db_column='TrialKey', null=True)),
                ('division', models.CharField(blank=True, db_column='Division', max_length=5, null=True)),
                ('product', models.CharField(blank=True, db_column='Product', max_length=30, null=True)),
                ('initiationdate', models.DateTimeField(blank=True, db_column='InitiationDate', null=True)),
                ('approvaldate', models.DateTimeField(blank=True, db_column='ApprovalDate', null=True)),
                ('trialstatus', models.CharField(blank=True, db_column='TrialStatus', max_length=10, null=True)),
                ('inrepository', models.SmallIntegerField(blank=True, db_column='InRepository', null=True)),
            ],
            options={
                'db_table': 'tTrials',
            },
        ),
        migrations.CreateModel(
            name='TUpBoxissue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transnum', models.CharField(db_column='TransNum', max_length=50)),
                ('boxid', models.CharField(db_column='BoxID', max_length=50)),
                ('studyid', models.CharField(blank=True, db_column='StudyID', max_length=10, null=True)),
                ('specranges', models.TextField(blank=True, db_column='SpecRangeS', null=True)),
                ('specrangee', models.TextField(blank=True, db_column='SpecRangeE', null=True)),
            ],
            options={
                'db_table': 't_up_BoxIssue',
            },
        ),
        migrations.CreateModel(
            name='TUpInventorya',
            fields=[
                ('aqid', models.CharField(blank=True, db_column='AqID', max_length=50, primary_key=True, serialize=False)),
                ('originalid', models.CharField(blank=True, db_column='OriginalID', max_length=255, null=True)),
                ('grid', models.CharField(blank=True, db_column='Grid', max_length=50, null=True)),
                ('labelinfo', models.TextField(blank=True, db_column='LabelInfo', null=True)),
                ('volume', models.DecimalField(blank=True, db_column='Volume', decimal_places=3, max_digits=18, null=True)),
                ('insertdate', models.DateTimeField(blank=True, db_column='InsertDate', null=True)),
                ('invnum', models.IntegerField(db_column='InvNum')),
                ('invcomment', models.TextField(blank=True, db_column='InvComment', null=True)),
            ],
            options={
                'db_table': 't_up_InventoryA',
            },
        ),
        migrations.CreateModel(
            name='TUpInventoryaBak26Sep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aqid', models.CharField(blank=True, db_column='AqID', max_length=50, null=True)),
                ('originalid', models.CharField(blank=True, db_column='OriginalID', max_length=255, null=True)),
                ('boxid', models.CharField(blank=True, db_column='BoxID', max_length=255, null=True)),
                ('grid', models.CharField(blank=True, db_column='Grid', max_length=50, null=True)),
                ('labelinfo', models.TextField(blank=True, db_column='LabelInfo', null=True)),
                ('volume', models.DecimalField(blank=True, db_column='Volume', decimal_places=3, max_digits=18, null=True)),
                ('insertdate', models.DateTimeField(blank=True, db_column='InsertDate', null=True)),
                ('invnum', models.IntegerField(db_column='InvNum')),
                ('invcomment', models.TextField(blank=True, db_column='InvComment', null=True)),
            ],
            options={
                'db_table': 't_up_InventoryA_bak26SEP',
            },
        ),
        migrations.CreateModel(
            name='TUpInventoryb',
            fields=[
                ('freezer', models.CharField(blank=True, db_column='Freezer', max_length=100, null=True)),
                ('cage', models.CharField(blank=True, db_column='Cage', max_length=50, null=True)),
                ('cane', models.CharField(blank=True, db_column='Cane', max_length=50, null=True)),
                ('stack', models.CharField(blank=True, db_column='Stack', max_length=50, null=True)),
                ('boxid', models.CharField(blank=True, db_column='BoxID', max_length=200, primary_key=True, serialize=False)),
                ('invnum', models.IntegerField(db_column='InvNum')),
                ('insertdate', models.DateTimeField(blank=True, db_column='InsertDate', null=True)),
                ('invcomments', models.TextField(db_column='InvComments')),
            ],
            options={
                'db_table': 't_up_InventoryB',
            },
        ),
        migrations.CreateModel(
            name='TUpVialissue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transnum', models.CharField(db_column='TransNum', max_length=50)),
                ('originalid', models.CharField(blank=True, db_column='OriginalID', max_length=30, null=True)),
                ('aqid', models.CharField(db_column='AqID', max_length=50)),
                ('freezethaw', models.SmallIntegerField(db_column='FreezeThaw')),
                ('issuevol', models.DecimalField(db_column='IssueVol', decimal_places=3, max_digits=8)),
                ('issueall', models.SmallIntegerField(db_column='IssueAll')),
            ],
            options={
                'db_table': 't_up_VialIssue',
            },
        ),
        migrations.CreateModel(
            name='Tblboxinfo',
            fields=[
                ('boxid', models.OneToOneField(db_column='BoxID', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='search.TUpInventoryb')),
                ('boxtype', models.CharField(blank=True, db_column='BoxType', max_length=30, null=True)),
                ('contents', models.TextField(blank=True, db_column='Contents', null=True)),
                ('insertdate', models.DateTimeField(db_column='InsertDate')),
                ('invstatus', models.CharField(db_column='InvStatus', max_length=2)),
            ],
            options={
                'db_table': 'tblBoxInfo',
                'managed': False,
            },
        ),
        migrations.AddField(
            model_name='tupinventorya',
            name='boxid',
            field=models.ForeignKey(db_column='BoxID', max_length=255, on_delete=django.db.models.deletion.CASCADE, to='search.TUpInventoryb'),
        ),
        migrations.AddField(
            model_name='tlistinventorya',
            name='boxid',
            field=models.ForeignKey(db_column='BoxID', on_delete=django.db.models.deletion.CASCADE, to='search.TListInventoryb'),
        ),
    ]
