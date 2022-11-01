# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TUpSearchTest(models.Model):
    lotid = models.CharField(db_column='LotID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    trialkey = models.CharField(db_column='TrialKey', max_length=50, blank=True, null=True)  # Field name made lowercase.
    studyid = models.CharField(db_column='StudyID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    studydesc = models.CharField(db_column='StudyDesc', max_length=200, blank=True, null=True)  # Field name made lowercase.
    aqid = models.CharField(db_column='AqID', max_length=50)  # Field name made lowercase.
    originalid = models.CharField(db_column='OriginalID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    grid = models.CharField(db_column='Grid', max_length=50, blank=True, null=True)  # Field name made lowercase.
    labelinfo = models.TextField(db_column='LabelInfo', blank=True, null=True)  # Field name made lowercase.
    volume = models.DecimalField(db_column='Volume', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    insertdate = models.DateTimeField(db_column='InsertDate', blank=True, null=True)  # Field name made lowercase.
    invnum = models.CharField(db_column='InvNum', max_length=50, blank=True, null=True)  # Field name made lowercase.
    invcomment = models.TextField(db_column='InvComment', blank=True, null=True)  # Field name made lowercase.
    boxid = models.CharField(db_column='BoxID', max_length=200)  # Field name made lowercase.
    checkout = models.IntegerField(db_column='CheckOut')  # Field name made lowercase.
    date_changed = models.DateTimeField(db_column='Date_Changed', blank=True, null=True)  # Field name made lowercase.
    user = models.CharField(db_column='User', max_length=50, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(db_column='Age', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=50, blank=True, null=True)  # Field name made lowercase.
    demogroup = models.CharField(db_column='DemoGroup', max_length=50, blank=True, null=True)  # Field name made lowercase.
    riskcategory = models.CharField(db_column='RiskCategory', max_length=50, blank=True, null=True)  # Field name made lowercase.
    riskgroupdesc = models.CharField(db_column='RiskGroupDesc', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bloodtype = models.CharField(db_column='BloodType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hiv1 = models.CharField(db_column='HIV1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hiv2 = models.CharField(db_column='HIV2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hivo = models.CharField(db_column='HIVO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hbs = models.CharField(db_column='HBs', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hbc = models.CharField(db_column='HBc', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hav = models.CharField(db_column='HAV', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hcv = models.CharField(db_column='HCV', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mmrv = models.CharField(db_column='MMRV', max_length=50, blank=True, null=True)  # Field name made lowercase.
    influenza = models.CharField(db_column='Influenza', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sars_cov2 = models.CharField(db_column='SARS_COV2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    other = models.CharField(db_column='Other', max_length=50, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    panelname = models.CharField(db_column='PanelName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    paneldesc = models.CharField(db_column='PanelDesc', max_length=50, blank=True, null=True)  # Field name made lowercase.
    membernum = models.CharField(db_column='MemberNum', max_length=50, blank=True, null=True)  # Field name made lowercase.
    samtypedesc = models.CharField(db_column='SamTypeDesc', max_length=50, blank=True, null=True)  # Field name made lowercase.
    samprepdesc = models.CharField(db_column='SamPrepDesc', max_length=50, blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.
    dup = models.CharField(db_column='Dup', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isconfirmed = models.CharField(db_column='IsConfirmed', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_up_search_test'
