# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime
#class AuthGroup(models.Model):
#    name = models.CharField(unique=True, max_length=80)
#
#    class Meta:
        #managed = False
#        db_table = 'auth_group'
#
#
#class AuthGroupPermissions(models.Model):
#    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)
#
#    class Meta:
#        managed = False
#        db_table = 'auth_group_permissions'
#        unique_together = (('group', 'permission'),)
#
#
#class AuthPermission(models.Model):
#    name = models.CharField(max_length=255)
#    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#    codename = models.CharField(max_length=100)
#
#    class Meta:
#        #managed = False
#        db_table = 'auth_permission'
#        unique_together = (('content_type', 'codename'),)
#
#
#class AuthUser(models.Model):
#    password = models.CharField(max_length=128)
#    last_login = models.DateTimeField(blank=True, null=True)
#    is_superuser = models.BooleanField()
#    username = models.CharField(unique=True, max_length=150)
#    first_name = models.CharField(max_length=30)
#    last_name = models.CharField(max_length=150)
#    email = models.CharField(max_length=254)
#    is_staff = models.BooleanField()
#    is_active = models.BooleanField()
#    date_joined = models.DateTimeField()
#
#    class Meta:
#        #managed = False
#        db_table = 'auth_user'
#
#
#class AuthUserGroups(models.Model):
#    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#
#    class Meta:
#        managed = False
#        db_table = 'auth_user_groups'
#        unique_together = (('user', 'group'),)
#
#
#class AuthUserUserPermissions(models.Model):
#    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)
#
#    class Meta:
#        managed = False
#        db_table = 'auth_user_user_permissions'
#        unique_together = (('user', 'permission'),)
#
#
#
#class DjangoAdminLog(models.Model):
#    action_time = models.DateTimeField()
#    object_id = models.TextField(blank=True, null=True)
#    object_repr = models.CharField(max_length=200)
#    action_flag = models.SmallIntegerField()
#    change_message = models.TextField()
#    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#
#   class Meta:
        #managed = False
#        db_table = 'django_admin_log'
#
#
#class DjangoContentType(models.Model):
#    app_label = models.CharField(max_length=100)
#    model = models.CharField(max_length=100)
#
#    class Meta:
#        #managed = False
#        db_table = 'django_content_type'
#        unique_together = (('app_label', 'model'),)
#
#
#class DjangoMigrations(models.Model):
#    app = models.CharField(max_length=255)
#    name = models.CharField(max_length=255)
#    applied = models.DateTimeField()
#
#    class Meta:
#        #managed = False
#        db_table = 'django_migrations'
#
#
#class DjangoSession(models.Model):
#    session_key = models.CharField(primary_key=True, max_length=40)
#    session_data = models.TextField()
#    expire_date = models.DateTimeField()
#
#    class Meta:
#        #managed = False
#        db_table = 'django_session'


class Dtproperties(models.Model):
    objectid = models.IntegerField(blank=True, null=True)
    property = models.CharField(max_length=64)
    value = models.CharField(max_length=255, blank=True, null=True)
    uvalue = models.CharField(max_length=255, blank=True, null=True)
    lvalue = models.BinaryField(blank=True, null=True)
    version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dtproperties'
        unique_together = (('id', 'property'),)


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)


class Tdemogroups(models.Model):
    specid = models.CharField(db_column='SpecID', max_length=20)  # Field name made lowercase.
    age = models.SmallIntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=5, blank=True, null=True)  # Field name made lowercase.
    a = models.CharField(db_column='A', max_length=50, blank=True, null=True)  # Field name made lowercase.
    demogroup = models.CharField(db_column='DemoGroup', max_length=60)  # Field name made lowercase.

    class Meta:
#        managed = False
        db_table = 'tDemoGroups'


class Triskgroups(models.Model):
    perid = models.CharField(db_column='PerID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lotid = models.CharField(db_column='LotID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    trialkey = models.IntegerField(db_column='TrialKey', blank=True, null=True)  # Field name made lowercase.
    originalid = models.CharField(db_column='OriginalID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    specid = models.CharField(db_column='SpecID', max_length=20)  # Field name made lowercase.
    studyid = models.CharField(db_column='StudyID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    studydesc = models.CharField(db_column='StudyDesc', max_length=200, blank=True, null=True)  # Field name made lowercase.
    riskgroupid = models.SmallIntegerField(db_column='RiskGroupID', blank=True, null=True)  # Field name made lowercase.
    dup = models.IntegerField(db_column='Dup', blank=True, null=True)  # Field name made lowercase.
    comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tRiskGroups'


class Ttrialids(models.Model):
    trialkey = models.IntegerField(db_column='TrialKey', blank=True, null=True)  # Field name made lowercase.
    aqid = models.IntegerField(db_column='AqID', blank=True, null=True)  # Field name made lowercase.
    lotid = models.CharField(db_column='LotID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    originalid = models.CharField(db_column='OriginalID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    specid = models.CharField(db_column='SpecID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    volreq = models.DecimalField(db_column='Volreq', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    issued = models.SmallIntegerField(db_column='Issued', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tTrialIDs'


class Ttrials(models.Model):
    trialkey = models.IntegerField(db_column='TrialKey', blank=True, null=True)  # Field name made lowercase.
    division = models.CharField(db_column='Division', max_length=5, blank=True, null=True)  # Field name made lowercase.
    product = models.CharField(db_column='Product', max_length=30, blank=True, null=True)  # Field name made lowercase.
    initiationdate = models.DateTimeField(db_column='InitiationDate', blank=True, null=True)  # Field name made lowercase.
    approvaldate = models.DateTimeField(db_column='ApprovalDate', blank=True, null=True)  # Field name made lowercase.
    trialstatus = models.CharField(db_column='TrialStatus', max_length=10, blank=True, null=True)  # Field name made lowercase.
    inrepository = models.SmallIntegerField(db_column='InRepository', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tTrials'

class TLinkAqlot(models.Model):
    aqid = models.CharField(db_column='AqID', max_length=50)  # Field name made lowercase.
    lotid = models.CharField(db_column='LotID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    originalid = models.CharField(db_column='OriginalID', max_length=255)  # Field name made lowercase.
    verified = models.SmallIntegerField(db_column='Verified', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 't_link_AqLot'


class TLinkLotkey(models.Model):
    aqid = models.IntegerField(db_column='AqID', blank=True, null=True)  # Field name made lowercase.
    lotid = models.CharField(db_column='LotID', max_length=10)  # Field name made lowercase.
    originalid = models.CharField(db_column='OriginalID', max_length=30)  # Field name made lowercase.
    duplicate = models.CharField(db_column='Duplicate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    verified = models.SmallIntegerField(db_column='Verified', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 't_link_LotKey'


class TLinkPerpan(models.Model):
    originalid = models.CharField(db_column='OriginalID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    panelname = models.CharField(db_column='PanelName', max_length=20)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 't_link_PerPan'


class TLinkRestrictions(models.Model):
    resid = models.IntegerField(db_column='ResID')  # Field name made lowercase.
    aqid = models.CharField(db_column='AqID', max_length=50)  # Field name made lowercase.
    resvol = models.DecimalField(db_column='ResVol', max_digits=8, decimal_places=3)  # Field name made lowercase.
    resstatus = models.SmallIntegerField(db_column='ResStatus')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 't_link_Restrictions'

class TListInventoryb(models.Model):
   
    freezer = models.CharField(db_column='Freezer', max_length=100)  # Field name made lowercase.
    cage = models.CharField(db_column='Cage', max_length=50)  # Field name made lowercase.
    cane = models.CharField(db_column='Cane', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stack = models.CharField(db_column='Stack', max_length=50, blank=True, null=True)  # Field name made lowercase.
    boxid = models.CharField(db_column='BoxID', max_length=200,primary_key =True)  # Field name made lowercase.
    invnum = models.IntegerField(db_column='InvNum')  # Field name made lowercase.
    insertdate = models.DateTimeField(db_column='InsertDate')  # Field name made lowercase.
    invcomment = models.TextField(db_column='InvComment', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 't_list_InventoryB'

    def __str__(self):
        return self.boxid

    def get_absolute_url(self):
        return reverse('search:aliquot_add')

class TListInventorya(models.Model):
    
    aqid = models.CharField(db_column='AqID',  max_length=50,primary_key=True)  # Field name made lowercase.
    originalid = models.CharField(db_column='OriginalID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    boxid = models.ForeignKey(TListInventoryb,db_column='BoxID', on_delete=models.CASCADE)  # Field name made lowercase. ## DK 11/21/2019 I Do not think boxname is correct related_name shouldn't it be BoxID?
    grid = models.CharField(db_column='Grid', max_length=50)  # Field name made lowercase.
    labelinfo = models.TextField(db_column='LabelInfo')  # Field name made lowercase.
    volume = models.DecimalField(db_column='Volume', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    insertdate = models.DateTimeField(db_column='InsertDate')  # Field name made lowercase.
      
    invnum = models.IntegerField(db_column='InvNum')  # Field name made lowercase.
    invcomment = models.TextField(db_column='InvComment', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 't_list_InventoryA'

    def __str__(self):
        return self.aqid

    def get_absolute_url(self):
        return reverse('aliquot_add')


class AliquotList(models.Model):
    aqid = models.CharField(db_column='AqID',  max_length=50, primary_key=True)  # Field name made lowercase.
    originalid = models.CharField(db_column='OriginalID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    boxid = models.ForeignKey(TListInventoryb, on_delete=models.CASCADE)  # Field name made lowercase. ## DK 11/21/2019 I Do not think boxname is correct related_name shouldn't it be BoxID?
    grid = models.CharField(db_column='Grid', max_length=50)  # Field name made lowercase.
    labelinfo = models.TextField(db_column='LabelInfo')  # Field name made lowercase.
    volume = models.DecimalField(db_column='Volume', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    insertdate = models.DateTimeField(db_column='InsertDate')  # Field name made lowercase.
      
    invnum = models.IntegerField(db_column='InvNum')  # Field name made lowercase.
    invcomment = models.TextField(db_column='InvComment', blank=True, null=True)  # Field name made lowercase.

    class Meta:
#        managed = False
        db_table = 't_list_InventoryA'

    def __str__(self):
        return self.aqid, self.originalid, self.boxid, self.grid, self.labelinfo, self.volume, self.insertdate, self.invnum, self.invcomment


class TListInventorybBak24Sep(models.Model):
    freezer = models.CharField(db_column='Freezer', max_length=100)  # Field name made lowercase.
    cage = models.CharField(db_column='Cage', max_length=50)  # Field name made lowercase.
    cane = models.CharField(db_column='Cane', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stack = models.CharField(db_column='Stack', max_length=50, blank=True, null=True)  # Field name made lowercase.
    boxid = models.CharField(db_column='BoxID', max_length=200)  # Field name made lowercase.
    invdate = models.DateTimeField(db_column='InvDate')  # Field name made lowercase.
    invuser = models.CharField(db_column='InvUser', max_length=50)  # Field name made lowercase.
    invcomments = models.TextField(db_column='InvComments')  # Field name made lowercase. This field type is a guess.
    transnum = models.AutoField(db_column='TransNum',primary_key=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 't_list_InventoryB_bak24SEP'


class TRefDataidkey(models.Model):
    sheet = models.TextField(db_column='Sheet', blank=True, null=True)  # Field name made lowercase.
    lotid = models.CharField(db_column='LotID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    originalid = models.CharField(db_column='OriginalID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    idstatus = models.CharField(db_column='IDStatus', max_length=15, blank=True, null=True)  # Field name made lowercase.
    idconfirmed = models.DateTimeField(db_column='IDConfirmed', blank=True, null=True)  # Field name made lowercase.
    pkid = models.IntegerField(db_column='PK')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 't_ref_DataIDKEY'


class TRefDepartments(models.Model):
    deptcode = models.CharField(db_column='DeptCode', max_length=20)  # Field name made lowercase.
    deptname = models.CharField(db_column='DeptName', max_length=50)  # Field name made lowercase.
    divcode = models.CharField(db_column='DivCode', max_length=20)  # Field name made lowercase.
    divname = models.CharField(db_column='DivName', max_length=50)  # Field name made lowercase.
    groupcode = models.CharField(db_column='GroupCode', max_length=20)  # Field name made lowercase.
    groupname = models.CharField(db_column='GroupName', max_length=50)  # Field name made lowercase.
    oldcode = models.CharField(db_column='OldCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    oldname = models.CharField(db_column='OldName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    link = models.TextField(db_column='Link', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        #managed = False
        db_table = 't_ref_Departments'


class TRefInventories(models.Model):
    invnum = models.AutoField(db_column='InvNum', primary_key=True)  # Field name made lowercase.
    invenddate = models.DateTimeField(db_column='InvEndDate')  # Field name made lowercase.
    invuser = models.CharField(db_column='InvUser', max_length=50)  # Field name made lowercase.
    invtype = models.CharField(db_column='InvType', max_length=50)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 't_ref_Inventories'


class TRefLocations(models.Model):
    locgrid = models.CharField(db_column='LocGrid', primary_key=True, max_length=50)  # Field name made lowercase.
    freezernum = models.CharField(db_column='FreezerNum', max_length=10)  # Field name made lowercase.
    canenum = models.CharField(db_column='CaneNum', max_length=10)  # Field name made lowercase.
    cagenum = models.CharField(db_column='CageNum', max_length=20)  # Field name made lowercase.
    canegrid = models.CharField(db_column='CaneGrid', max_length=20)  # Field name made lowercase.
    keynumber = models.CharField(db_column='KeyNumber', max_length=10, blank=True, null=True)  # Field name made lowercase.
    freezertemp = models.CharField(db_column='FreezerTemp', max_length=10, blank=True, null=True)  # Field name made lowercase.
    room = models.TextField(db_column='Room', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 't_ref_Locations'


class TRefLotsRisk(models.Model):
    pkid = models.IntegerField(db_column='PK')  # Field name made lowercase.
    lotid = models.CharField(db_column='LotID', max_length=10)  # Field name made lowercase.
    originalid = models.CharField(db_column='OriginalID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    risk_dx1 = models.CharField(db_column='Risk_Dx1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    risk_dx2 = models.CharField(db_column='Risk_Dx2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    risk_dx3 = models.CharField(db_column='Risk_Dx3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dateverified = models.DateTimeField(db_column='DateVerified', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 't_ref_Lots_Risk'


class TRefLotsSam(models.Model):
    pkid = models.IntegerField(db_column='PK')  # Field name made lowercase.
    lotid = models.CharField(db_column='LotID', max_length=10)  # Field name made lowercase.
    originalid = models.CharField(db_column='OriginalID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    samprepid = models.IntegerField(db_column='SamPrepID', blank=True, null=True)  # Field name made lowercase.
    samtypeid = models.IntegerField(db_column='SamTypeID', blank=True, null=True)  # Field name made lowercase.
    samapperance = models.CharField(db_column='SamApperance', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vol_initial = models.DecimalField(db_column='Vol_Initial', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    dateverified = models.DateTimeField(db_column='DateVerified', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 't_ref_Lots_Sam'


class TRefLotsSource(models.Model):
    pkid = models.AutoField(db_column='PK', primary_key=True)  # Field name made lowercase.
    lotid = models.CharField(db_column='LotID', max_length=10)  # Field name made lowercase.
    originalid = models.CharField(db_column='OriginalID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    costperml = models.DecimalField(db_column='CostPerMl', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    datepurchased = models.DateTimeField(db_column='DatePurchased', blank=True, null=True)  # Field name made lowercase.
    datecollected = models.DateTimeField(db_column='DateCollected', blank=True, null=True)  # Field name made lowercase.
    vendor = models.CharField(db_column='Vendor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=255, blank=True, null=True)  # Field name made lowercase.
    collectionloc = models.CharField(db_column='CollectionLoc', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lotowner = models.CharField(db_column='LotOwner', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lottrialsource = models.CharField(db_column='LotTrialSource', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dateverified = models.DateTimeField(db_column='DateVerified', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 't_ref_Lots_Source'


class TRefPanels(models.Model):
    manufacturer = models.CharField(db_column='Manufacturer', max_length=200)  # Field name made lowercase.
    panelname = models.CharField(db_column='PanelName', max_length=20)  # Field name made lowercase.
    paneltype = models.CharField(db_column='PanelType', max_length=255)  # Field name made lowercase.
    paneldesc = models.TextField(db_column='PanelDesc')  # Field name made lowercase.
    membernum = models.IntegerField(db_column='MemberNum', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 't_ref_Panels'


class TRefRestrictions(models.Model):
    resid = models.AutoField(db_column='ResID',primary_key=True)  # Field name made lowercase.
    resdept = models.CharField(db_column='ResDept', max_length=20, blank=True, null=True)  # Field name made lowercase.
    respersonnel = models.CharField(db_column='ResPersonnel', max_length=50)  # Field name made lowercase.
    resexpiration = models.DateTimeField(db_column='ResExpiration')  # Field name made lowercase.
    resdesc = models.TextField(db_column='ResDesc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 't_ref_Restrictions'


class TRefRiskgroups(models.Model):
    riskcatid = models.AutoField(db_column='RiskCatID',primary_key=True )  # Field name made lowercase.
    riskcategory = models.CharField(db_column='RiskCategory', max_length=255)  # Field name made lowercase.
    riskcatdesc = models.TextField(db_column='RiskCatDesc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 't_ref_RiskGroups'


class TRefSamplepreparations(models.Model):
    samprepid = models.IntegerField(db_column='SamPrepID')  # Field name made lowercase.
    samprepdesc = models.CharField(db_column='SamPrepDesc', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 't_ref_SamplePreparations'


class TRefSampletypes(models.Model):
    samtypeid = models.IntegerField(db_column='SamTypeID')  # Field name made lowercase.
    samtypedesc = models.CharField(db_column='SamTypeDesc', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 't_ref_SampleTypes'


class TRefTransactions(models.Model):
    transnum = models.CharField(db_column='TransNum', max_length=50)  # Field name made lowercase.
    issuedest = models.CharField(db_column='IssueDest', max_length=10)  # Field name made lowercase.
    issueuser = models.CharField(db_column='IssueUser', max_length=100, blank=True, null=True)  # Field name made lowercase.
    issuedate = models.DateTimeField(db_column='IssueDate', blank=True, null=True)  # Field name made lowercase.
    issuereason = models.TextField(db_column='IssueReason', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 't_ref_Transactions'


class TUpBoxissue(models.Model):
    transnum = models.CharField(db_column='TransNum', max_length=50)  # Field name made lowercase.
    boxid = models.CharField(db_column='BoxID', max_length=50)  # Field name made lowercase.
    studyid = models.CharField(db_column='StudyID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    specranges = models.TextField(db_column='SpecRangeS', blank=True, null=True)  # Field name made lowercase.
    specrangee = models.TextField(db_column='SpecRangeE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 't_up_BoxIssue'

class TUpCoa(models.Model):
    year = models.CharField(db_column='Year', max_length=5, blank=True, null=True)  # Field name made lowercase.
    lotid = models.CharField(db_column='LotID', max_length=20, blank=True, primary_key=True)  # Field name made lowercase.
    field_field = models.CharField(db_column='#', max_length=10, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    originalid = models.CharField(db_column='OriginalID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cofa = models.TextField(db_column='CofA', blank=True, null=True)  # Field name made lowercase.
    pdf_contents = models.TextField(db_column='PDF_Contents', blank=True, null=True)  # Field name made lowercase.
    comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_up_CoA'

    def __str__(self):
        return self.lotid



class TUpInventoryb(models.Model):
    freezer = models.CharField(db_column='Freezer', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cage = models.CharField(db_column='Cage', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cane = models.CharField(db_column='Cane', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stack = models.CharField(db_column='Stack', max_length=50, blank=True, null=True)  # Field name made lowercase.
    boxid = models.CharField(db_column='BoxID', max_length=200, blank=True, primary_key=True)  # Field name made lowercase.
    invnum = models.IntegerField(db_column='InvNum',blank=True, null=True)  # Field name made lowercase.
    insertdate = models.DateTimeField(db_column='InsertDate', blank=True, null=True)  # Field name made lowercase.
    invcomments = models.TextField(db_column='InvComments',blank=True,null=True) 

    class Meta:
#        managed = False
        db_table = 't_up_InventoryB'
#        db_table = 't_up_InventoryB_test'

    def __str__(self):
        return self.boxid

    def get_absolute_url(self):
       # return reverse('search:aliquot_add')
        return reverse("aliquot_detail",args=[str(self.boxid)])

class TUpSearch(models.Model):
    lotid = models.ForeignKey(TUpCoa,db_column='LotID',  max_length=50, on_delete=models.CASCADE)  # Field name made lowercase.
    trialkey = models.CharField(db_column='TrialKey', max_length=50, blank=True, null=True)  # Field name made lowercase.
    studyid = models.CharField(db_column='StudyID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    studydesc = models.CharField(db_column='StudyDesc', max_length=200, blank=True, null=True)  # Field name made lowercase.
    aqid = models.CharField(db_column='AqID', primary_key=True, max_length=50)  # Field name made lowercase.
    originalid = models.CharField(db_column='OriginalID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    grid = models.CharField(db_column='Grid', max_length=50, blank=True, null=True)  # Field name made lowercase.
    labelinfo = models.TextField(db_column='LabelInfo', blank=True, null=True)  # Field name made lowercase.
    volume = models.DecimalField(db_column='Volume', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    insertdate = models.DateTimeField(db_column='InsertDate', blank=True, null=True)  # Field name made lowercase.
    invnum = models.CharField(db_column='InvNum', max_length=50, blank=True, null=True)  # Field name made lowercase.
    invcomment = models.TextField(db_column='InvComment', blank=True, null=True)  # Field name made lowercase.
    boxid = models.ForeignKey(TUpInventoryb, db_column='BoxID', max_length=255, on_delete=models.CASCADE)  # Field name made lowercase.
    #boxid = models.CharField(db_column='BoxID', max_length=200)  # Field name made lowercase.
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
    freeze_thaw = models.IntegerField(db_column='Freeze_Thaw', blank=True, null=True)  # Field name made lowercase.
    ship_location = models.CharField(db_column='ship_location',max_length=50, blank=True,null=True)
    class Meta:
        managed = False
        db_table = 't_up_Search'

    def __str__(self):
        return self.aqid

    def get_absolute_url(self):
       # return reverse('aliquot_add')
        return reverse("aliquot_dispose", args=[str(self.aqid)])

def increment_site_id():
	last_id = TRefSite.objects.all().aggregate(largest=models.Max('siteid'))['largest']
	if last_id ==None:
		return 1
	else:
		return last_id + 1

class SearchCreateLocationTrans(models.Model):
    create_trans_id = models.IntegerField(primary_key=True,unique=True,default=increment_site_id)
    user = models.CharField(db_column='User', max_length=50, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=50, blank=True, null=True)  # Field name made lowercase.
    locatino_abbr = models.CharField(db_column='Locatino_abbr', max_length=50, blank=True, null=True)  # Field name made lowercase.
    date_created = models.DateTimeField(db_column='Date_created', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'search_create_location_trans'

def increment_site_id():
	last_id = TRefSite.objects.all().aggregate(largest=models.Max('siteid'))['largest']
	if last_id ==None:
		return 1
	else:
		return last_id + 1
	

class TRefSite(models.Model):
    siteid = models.IntegerField(db_column='SiteID', unique=True,default=increment_site_id)  # Field name made lowercase.
    sitestate = models.CharField(db_column='SiteState', max_length=50)  # Field name made lowercase.
    sitecountry = models.CharField(db_column='SiteCountry', max_length=50)  # Field name made lowercase.
    sitename = models.CharField(db_column='SiteName', max_length=255)  # Field name made lowercase.
    siteabbr = models.CharField(db_column='SiteAbbr', primary_key=True, max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_ref_Site'


def increment_shipping_id():
	last_transid = SearchShippingTrans.objects.all().order_by('trans_id').last()
	if not last_transid:
		return 'shp-'+str(datetime.now().strftime('%Y%m%d-'))+ '0000'
	ship_id = last_transid.shipping_id
	ship_int = ship_id[13:17]
	new_ship_int = int(ship_int)+1
	new_ship_id = 'shp-'+str(datetime.now().strftime('%Y%m%d-'))+str(new_ship_int).zfill(4)
	return new_ship_id


class SearchShippingTrans(models.Model):
    shipping_id = models.CharField(db_column='shipping_id',  unique=True, max_length=50, default=increment_shipping_id)
    trans_id = models.AutoField(db_column='trans_id', primary_key= True)
    aqid_out = models.ForeignKey(TUpSearch,db_column='aqid_out',max_length=50, blank=True, null=True,on_delete=models.CASCADE)
    boxid_out = models.CharField(db_column='boxid_out',max_length=50, blank=True, null=True)
    ship_location = models.CharField(db_column='ship_location',max_length=50, blank=True, null=True)
    date_shipped = models.DateTimeField(db_column='date_shipped',blank=True, null=True)
    user = models.CharField(db_column='user',max_length=50, blank=True, null=True)
    condition = models.CharField(db_column='condition',max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'search_shipping_trans'

class SearchReturnTrans(models.Model):
    trans_id = models.AutoField(db_column='trans_id',  primary_key=True)
    aqid_in = models.CharField( db_column='aqid_in', max_length=50,blank=True,null=True)  # Field name made lowercase.
    boxid_in = models.CharField(db_column='boxid_in',max_length=50, blank=True, null=True)
    ship_location = models.CharField(db_column='ship_location',max_length=50, blank=True, null=True)
    date_returned = models.DateTimeField(db_column='date_returned',blank=True, null=True)
    user = models.CharField(db_column='user',max_length=50, blank=True, null=True)
    condition = models.CharField(db_column='condition',max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'search_return_trans'

class TUpSearchTest(models.Model):
    lotid = models.CharField(db_column='LotID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    trialkey = models.CharField(db_column='TrialKey', max_length=50, blank=True, null=True)  # Field name made lowercase.
    studyid = models.CharField(db_column='StudyID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    studydesc = models.CharField(db_column='StudyDesc', max_length=200, blank=True, null=True)  # Field name made lowercase.
    aqid = models.CharField(db_column='AqID', primary_key=True, max_length=50)  # Field name made lowercase.
    #aqid = models.CharField(db_column='AqID', max_length=50)  # Field name made lowercase.
    originalid = models.CharField(db_column='OriginalID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    grid = models.CharField(db_column='Grid', max_length=50, blank=True, null=True)  # Field name made lowercase.
    labelinfo = models.TextField(db_column='LabelInfo', blank=True, null=True)  # Field name made lowercase.
    volume = models.DecimalField(db_column='Volume', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    insertdate = models.DateTimeField(db_column='InsertDate', blank=True, null=True)  # Field name made lowercase.
    invnum = models.CharField(db_column='InvNum', max_length=50, blank=True, null=True)  # Field name made lowercase.
    invcomment = models.TextField(db_column='InvComment', blank=True, null=True)  # Field name made lowercase.
    boxid = models.ForeignKey(TUpInventoryb, db_column='BoxID', max_length=255, on_delete=models.CASCADE)  # Field name made lowercase.
    #boxid = models.CharField(db_column='BoxID', max_length=200)  # Field name made lowercase.
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
    freeze_thaw = models.IntegerField(db_column='Freeze_Thaw', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_up_search_test'

    def __str__(self):
        return self.aqid

    def get_absolute_url(self):
       # return reverse('aliquot_add')
        return reverse("aliquot_dispose", args=[str(self.aqid)])

class TUpInventorya(models.Model):
    aqid = models.CharField(db_column='AqID', max_length=50, blank=True, primary_key=True)  # Field name made lowercase.
    originalid = models.CharField(db_column='OriginalID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    boxid = models.ForeignKey(TUpInventoryb, db_column='BoxID', max_length=255, on_delete=models.CASCADE)  # Field name made lowercase.
    grid = models.CharField(db_column='Grid', max_length=50, blank=True, null=True)  # Field name made lowercase.
    labelinfo = models.TextField(db_column='LabelInfo', blank=True, null=True)  # Field name made lowercase.
    volume = models.DecimalField(db_column='Volume', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    insertdate = models.DateTimeField(db_column='InsertDate', blank=True, null=True)  # Field name made lowercase.
    invnum = models.IntegerField(db_column='InvNum', blank=True, null=True)  # Field name made lowercase.
    invcomment = models.TextField(db_column='InvComment', blank=True, null=True)  # Field name made lowercase.
    checked_out = models.IntegerField(db_column='CheckOut', default=0)
    user = models.CharField(db_column='User', max_length=50, blank=True, null=True)
    datechanged = models.DateTimeField(db_column='Date_Changed',auto_now=True, blank=True, null=True)

    class Meta:
#        managed = False
        db_table = 't_up_InventoryA'
#        db_table = 't_up_InventoryA_test'

    def __str__(self):
        return self.aqid

    def get_absolute_url(self):
       # return reverse('aliquot_add')
        return reverse("aliquot_detail", args=[str(self.aqid)])

class SearchFreezeThawTrans(models.Model):
    transaction_num = models.AutoField(db_column='Transaction_Num',  primary_key=True)  # Field name made lowercase.
    aqid = models.ForeignKey(TUpSearch, db_column='AqID', max_length=50,blank=True,on_delete=models.CASCADE)  # Field name made lowercase.
    #aqid = models.CharField(db_column='AqID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    freeze_thaw = models.IntegerField(db_column='Freeze_Thaw', blank=True, null=True)  # Field name made lowercase.
    datetime_freeze = models.DateTimeField(db_column='DateTime_Freeze', blank=True, null=True)  # Field name made lowercase.
    datetime_thaw = models.DateTimeField(db_column='DateTime_Thaw', blank=True, null=True)  # Field name made lowercase.
    user = models.CharField(db_column='User', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'search_freeze_thaw_trans'
    def __str__(self):
        return self.aqid

    def get_absolute_url(self):
       # return reverse('search:aliquot_add')
        return reverse("freeze_thaw")#,args=[str(self.aqid)])


class Aliquot_Trans(models.Model):
    aqid=models.CharField(db_column='AqID', max_length=50, blank=True, null=True)
    boxid=models.CharField(db_column='BoxID', max_length=50, blank=True, null=True)
    updated=models.IntegerField(db_column='Updated',default=0)
    date_updated=models.DateTimeField(db_column='Date_Updated', blank=True, null=True)
    user=models.CharField(db_column='User', max_length=50, blank=True, null=True)


class Update_Trans(models.Model):
    aqid=models.CharField(db_column='AqID', max_length=50, blank=True, null=True)
    boxid=models.CharField(db_column='BoxID', max_length=50, blank=True, null=True)
    reason=models.CharField(db_column='Reason', max_length=255, blank=True, null=True)
    updated=models.IntegerField(db_column='Updated',default=0)
    date_updated=models.DateTimeField(db_column='Date_Updated', blank=True, null=True)
    user=models.CharField(db_column='User', max_length=50, blank=True, null=True)

class Create_Aliquot_Trans (models.Model):
    aqid=models.CharField(db_column='AqID', max_length=50, blank=True, null=True)
    date_created=models.DateTimeField(db_column='Date_Created', blank=True, null=True)
    user=models.CharField(db_column='User', max_length=50, blank=True, null=True)

class Create_Box_Trans (models.Model):
    boxid=models.CharField(db_column='AqID', max_length=50, blank=True, null=True)
    date_created=models.DateTimeField(db_column='Date_Created', blank=True, null=True)
    user=models.CharField(db_column='User', max_length=50, blank=True, null=True)

class LoginLogout(models.Model):
    user=models.CharField(db_column='User', max_length=50, blank=True, null=True)
    datetime_login =models.DateTimeField(db_column='Datetime_logged_in', blank=True, null=True)
    
    logged_in =models.IntegerField(db_column='logged_in',default=0)
    datetime_logout =models.DateTimeField(db_column='Datetime_logged_out', blank=True, null=True)
    logged_out =models.IntegerField(db_column='logged_out',default=0)

    




class TUpInventoryaBak26Sep(models.Model):
    aqid = models.CharField(db_column='AqID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    originalid = models.CharField(db_column='OriginalID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    boxid = models.CharField(db_column='BoxID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    grid = models.CharField(db_column='Grid', max_length=50, blank=True, null=True)  # Field name made lowercase.
    labelinfo = models.TextField(db_column='LabelInfo', blank=True, null=True)  # Field name made lowercase.
    volume = models.DecimalField(db_column='Volume', max_digits=18, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    insertdate = models.DateTimeField(db_column='InsertDate', blank=True, null=True)  # Field name made lowercase.
    invnum = models.IntegerField(db_column='InvNum')  # Field name made lowercase.
    invcomment = models.TextField(db_column='InvComment', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 't_up_InventoryA_bak26SEP'




class TUpVialissue(models.Model):
    transnum = models.CharField(db_column='TransNum', max_length=50)  # Field name made lowercase.
    originalid = models.CharField(db_column='OriginalID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    aqid = models.CharField(db_column='AqID', max_length=50)  # Field name made lowercase.
    freezethaw = models.SmallIntegerField(db_column='FreezeThaw')  # Field name made lowercase.
    issuevol = models.DecimalField(db_column='IssueVol', max_digits=8, decimal_places=3)  # Field name made lowercase.
    issueall = models.SmallIntegerField(db_column='IssueAll')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 't_up_VialIssue'


class Tblaliquotbdm3(models.Model):
    boxid_grid = models.CharField(db_column='BoxID-Grid', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    boxid = models.CharField(db_column='BoxID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    boxcombo = models.CharField(db_column='BoxCombo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    grid = models.CharField(db_column='Grid', max_length=255, blank=True, null=True)  # Field name made lowercase.
    invdate = models.DateTimeField(db_column='InvDate', blank=True, null=True)  # Field name made lowercase.
    invuser = models.CharField(db_column='InvUser', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAliquotBDM3'


class Tblboxinfo(models.Model):# boxid to show relationship between boxid in this model with TListInventoryb
    

    boxid = models.OneToOneField(TUpInventoryb, db_column='BoxID',primary_key=True,  max_length=255, on_delete=models.CASCADE)  # Field name made lowercase.

    boxtype = models.CharField(db_column='BoxType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contents = models.CharField(db_column='Contents', max_length=255,blank=True, null=True)  # Field name made lowercase.
    insertdate = models.DateTimeField(db_column='InsertDate',blank=True,null=True)  # Field name made lowercase.
    invstatus = models.CharField(db_column='InvStatus', max_length=255,blank=True,null=True)  # Field name made lowercase.

    class Meta:
#        managed =False 
        db_table = 'tblBoxInfo'
#        db_table = 'tblBoxInfo_test'
    def __str__(self):
        return self.boxid

    def get_absolute_url(self):
       # return reverse('aliquot_add')
        return reverse("aliquot_detail", args=[str(self.boxid)])




class Tlkupcages(models.Model):
    cagenumber = models.CharField(db_column='CageNumber', primary_key=True, max_length=20)  # Field name made lowercase.
    keynumber = models.CharField(db_column='KeyNumber', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tlkupCages'


class Tlkupcanes(models.Model):
    canenum = models.CharField(db_column='CaneNum', primary_key=True, max_length=10)  # Field name made lowercase.
    canecapacity = models.IntegerField(db_column='CaneCapacity', blank=True, null=True)  # Field name made lowercase.
    caneinfo = models.CharField(db_column='CaneInfo', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tlkupCanes'


class Tlkupfreezers(models.Model):
    freezer = models.CharField(db_column='Freezer', primary_key=True, max_length=10)  # Field name made lowercase.
    freezertemp = models.CharField(db_column='FreezerTemp', max_length=10)  # Field name made lowercase.
    freezerloc = models.CharField(db_column='FreezerLoc', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tlkupFreezers'


class Tmphivsummary110(models.Model):
    plotid = models.CharField(db_column='PLotID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    poriginalid = models.CharField(db_column='POriginalID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lotid = models.CharField(db_column='LotID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    orignalid = models.CharField(db_column='OrignalID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pmatrix = models.CharField(db_column='Pmatrix', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pdx = models.CharField(db_column='PDx', max_length=50, blank=True, null=True)  # Field name made lowercase.
    psource = models.CharField(db_column='Psource', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pdrawdt = models.DateTimeField(db_column='PDrawDt', blank=True, null=True)  # Field name made lowercase.
    precdt = models.DateTimeField(db_column='PRecDt', blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=50, blank=True, null=True)  # Field name made lowercase.
    assaygrp = models.CharField(db_column='AssayGrp', max_length=50, blank=True, null=True)  # Field name made lowercase.
    assayname = models.CharField(db_column='AssayName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    abag = models.CharField(db_column='AbAg', max_length=10, blank=True, null=True)  # Field name made lowercase.
    analyte = models.CharField(db_column='Analyte', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pinter = models.CharField(db_column='Pinter', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bands = models.TextField(db_column='Bands', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tmpHIVSummary_110'


class Tmppediatrics110(models.Model):
    lotid = models.CharField(db_column='LotID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    originalid = models.CharField(db_column='OriginalID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    specid = models.CharField(db_column='SpecID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=50, blank=True, null=True)  # Field name made lowercase.
    demogroup = models.CharField(db_column='DemoGroup', max_length=50, blank=True, null=True)  # Field name made lowercase.
    riskgroup = models.CharField(db_column='RiskGroup', max_length=50)  # Field name made lowercase.
    studydesc = models.CharField(db_column='StudyDesc', max_length=255, blank=True, null=True)  # Field name made lowercase.
    volume = models.DecimalField(db_column='Volume', max_digits=8, decimal_places=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tmpPediatrics_110'


class TmpRefRiskgroups(models.Model):
    riskcategory = models.CharField(db_column='RiskCategory', max_length=20)  # Field name made lowercase.
    riskgroupdesc = models.CharField(db_column='RiskGroupDesc', max_length=200, blank=True, null=True)  # Field name made lowercase.
    riskgroupid = models.IntegerField(db_column='RiskGroupID')  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tmp_ref_RiskGroups'


class TmpUpInventorya(models.Model):
    aqid = models.CharField(db_column='AqID', max_length=511, blank=True, null=True)  # Field name made lowercase.
    specimenid = models.CharField(db_column='SpecimenID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    boxid = models.CharField(db_column='BoxID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    grid = models.CharField(db_column='Grid', max_length=255, blank=True, null=True)  # Field name made lowercase.
    labelinfo = models.TextField(db_column='LabelInfo', blank=True, null=True)  # Field name made lowercase.
    volume = models.FloatField(db_column='Volume', blank=True, null=True)  # Field name made lowercase.
    insertdate = models.DateTimeField(db_column='InsertDate', blank=True, null=True)  # Field name made lowercase.
    invnum = models.IntegerField(db_column='InvNum')  # Field name made lowercase.
    invcomment = models.TextField(db_column='InvComment', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'tmp_up_InventoryA'
