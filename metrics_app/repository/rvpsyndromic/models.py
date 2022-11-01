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



class BrpcrExclusionTrans(models.Model):
    id = models.CharField(max_length=50, blank=True, primary_key=True)
    user = models.CharField(max_length=50, blank=True, null=True)
    date_exclusion = models.DateTimeField(blank=True, null=True)

    class Meta:
#        managed = False
        db_table = 'brpcr_exclusion_trans'


class EcrfExclusionTrans(models.Model):
    ecrfrow = models.IntegerField()  # Field name made lowercase.
    subjectid = models.CharField(max_length=50, blank=True, null=True)
    specimenid = models.CharField(max_length=50, blank=True, null=True)
    user = models.CharField(max_length=50, blank=True, null=True)
    date_exclusion = models.DateTimeField(blank=True, null=True)

    class Meta:
 #       managed = False
        db_table = 'ecrf_exclusion_trans'

class Stg1Cov2PcrExclTrans(models.Model):
    refcov2row_1 = models.IntegerField(blank=True, null=True)
    refcov2row_2 = models.IntegerField(blank=True, null=True)
    refcov2_date = models.DateTimeField(blank=True, null=True)
    sample = models.CharField(max_length=50, blank=True, null=True)
    user = models.CharField(max_length=50, blank=True, null=True)
    date_exclusion = models.DateTimeField(blank=True, null=True)

    class Meta:
#        managed = False
        db_table = 'stg1_cov2pcr_excl_trans'


class Stg1RefflupcrExclTrans(models.Model):
    refflupcrrow_1 = models.IntegerField(blank=True, null=True)
    refflupcrrow_2 = models.IntegerField(blank=True, null=True)
    refrun_date = models.DateTimeField(blank=True, null=True)
    user = models.CharField(max_length=50, blank=True, null=True)
    date_exclusion = models.DateTimeField(blank=True, null=True)

    class Meta:
 #       managed = False
        db_table = 'stg1_refflupcr_excl_trans'

class TStg1FlupcrUpdate(models.Model):
    dep = models.SmallIntegerField(db_column='DEP', blank=True, null=True)  # Field name made lowercase.
    sample = models.CharField(db_column='Sample', max_length=25, blank=True, null=True)  # Field name made lowercase.
    reffluoperator = models.CharField(db_column='RefFluOperator', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refflukitname = models.CharField(db_column='RefFluKitName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refflukitlot = models.CharField(db_column='RefFluKitLot', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refflukitexp = models.DateTimeField(db_column='RefFluKitExp', blank=True, null=True)  # Field name made lowercase.
    refflu_date = models.DateTimeField(db_column='RefFlu_Date', blank=True, null=True)  # Field name made lowercase.
    refflua_well = models.CharField(db_column='RefFluA_Well', max_length=5, blank=True, null=True)  # Field name made lowercase.
    refflua_cqvalue = models.CharField(db_column='RefFluA_CqValue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refflua_interp = models.CharField(db_column='RefFluA_Interp', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refflub_well = models.CharField(db_column='RefFluB_Well', max_length=5, blank=True, null=True)  # Field name made lowercase.
    refflub_cqvalue = models.CharField(db_column='RefFluB_CqValue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refflub_interp = models.CharField(db_column='RefFluB_Interp', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refrsv_cqvalue = models.CharField(db_column='RefRSV_CqValue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refrsv_interp = models.CharField(db_column='RefRSV_Interp', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refnotes = models.TextField(db_column='RefNotes', blank=True, null=True)  # Field name made lowercase.
    excl_flag = models.SmallIntegerField(db_column='Excl_Flag', blank=True, null=True)  # Field name made lowercase.
    userid = models.CharField(max_length=50, blank=True, null=True)
    post_date = models.DateTimeField(blank=True, null=True)
    class Meta:
#        managed = False
        db_table = 't_stg1_FLUPCR_UPDATE'




class TStg0Brpcr(models.Model):
    brpcrrow = models.IntegerField(db_column='BRPCRRow', primary_key=True)  # Field name made lowercase.
    siteabbr = models.CharField(db_column='SiteAbbr', max_length=255, blank=True, null=True)  # Field name made lowercase.
    operator = models.CharField(db_column='Operator', max_length=255, blank=True, null=True)  # Field name made lowercase.
    kitname = models.CharField(db_column='KitName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    kitlot = models.CharField(db_column='KitLot', max_length=255, blank=True, null=True)  # Field name made lowercase.
    kitexp = models.DateTimeField(db_column='KitExp', blank=True, null=True)  # Field name made lowercase.
    file_name = models.CharField(db_column='File_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    created_by = models.CharField(db_column='Created_By', max_length=255, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    plateid = models.CharField(db_column='PlateID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    run_started = models.DateTimeField(db_column='Run_Started', blank=True, null=True)  # Field name made lowercase.
    run_ended = models.DateTimeField(db_column='Run_Ended', blank=True, null=True)  # Field name made lowercase.
    sample_vol = models.CharField(db_column='Sample_Vol', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lid_temp = models.CharField(db_column='Lid_Temp', max_length=255, blank=True, null=True)  # Field name made lowercase.
    protocol_file_name = models.CharField(db_column='Protocol_File_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    plate_setup_file_name = models.CharField(db_column='Plate_Setup_File_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    base_serial_number = models.CharField(db_column='Base_Serial_Number', max_length=255, blank=True, null=True)  # Field name made lowercase.
    optical_head_serial_number = models.CharField(db_column='Optical_Head_Serial_Number', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cfx_maestro_version = models.CharField(db_column='CFX_Maestro_Version', max_length=255, blank=True, null=True)  # Field name made lowercase.
    well_group = models.CharField(db_column='Well_Group', max_length=255, blank=True, null=True)  # Field name made lowercase.
    amplification_step = models.CharField(db_column='Amplification_Step', max_length=255, blank=True, null=True)  # Field name made lowercase.
    melt_step = models.CharField(db_column='Melt_Step', max_length=255, blank=True, null=True)  # Field name made lowercase.
    well = models.CharField(db_column='Well', max_length=5, blank=True, null=True)  # Field name made lowercase.
    fluor = models.CharField(db_column='Fluor', max_length=25, blank=True, null=True)  # Field name made lowercase.
    target = models.CharField(db_column='Target', max_length=25, blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(db_column='Content', max_length=25, blank=True, null=True)  # Field name made lowercase.
    sample = models.CharField(db_column='Sample', max_length=25, blank=True, null=True)  # Field name made lowercase.
    cq = models.CharField(db_column='Cq', max_length=25, blank=True, null=True)  # Field name made lowercase.
    starting_quantity = models.CharField(db_column='Starting_Quantity', max_length=25, blank=True, null=True)  # Field name made lowercase.


    class Meta:
        managed = False
        db_table = 't_stg0_BRPCR'


class TStg0Refcov2Pcr1(models.Model):
    refcov2row_1 = models.IntegerField(db_column='RefCov2Row_1')  # Field name made lowercase.
    refcov2file_name = models.CharField(db_column='RefCoV2File_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ref1_entered_by = models.CharField(db_column='Ref1_Entered_By', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ref1_entereddate = models.DateTimeField(db_column='Ref1_EnteredDate', blank=True, null=True)  # Field name made lowercase.
    refcov2_date = models.DateTimeField(db_column='RefCoV2_Date', blank=True, null=True)  # Field name made lowercase.
    sample = models.CharField(db_column='Sample', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refcov2_well = models.CharField(db_column='RefCoV2_Well', max_length=5, blank=True, null=True)  # Field name made lowercase.
    refcov2_cqvalue = models.CharField(db_column='RefCoV2_CqValue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refcov2_interp = models.CharField(db_column='RefCoV2_Interp', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refcov2notes = models.CharField(db_column='RefCoV2Notes', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_stg0_RefCoV2PCR_1'


class TStg0Refcov2Pcr2(models.Model):
    refcov2row_2 = models.IntegerField(db_column='RefCov2Row_2')  # Field name made lowercase.
    refcov2file_name = models.CharField(db_column='RefCoV2File_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ref2_entered_by = models.CharField(db_column='Ref2_Entered_By', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ref2_entereddate = models.DateTimeField(db_column='Ref2_EnteredDate', blank=True, null=True)  # Field name made lowercase.
    refcov2_date = models.DateTimeField(db_column='RefCoV2_Date', blank=True, null=True)  # Field name made lowercase.
    sample = models.CharField(db_column='Sample', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refcov2_well = models.CharField(db_column='RefCoV2_Well', max_length=5, blank=True, null=True)  # Field name made lowercase.
    refcov2_cqvalue = models.CharField(db_column='RefCoV2_CqValue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refcov2_interp = models.CharField(db_column='RefCoV2_Interp', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refcov2notes = models.CharField(db_column='RefCoV2Notes', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_stg0_RefCoV2PCR_2'

def increment_refflupcrrow():
	last_id = TStg0Refflupcr1.objects.all().aggregate(largest=models.Max('refflupcrrow_1'))['largest']
	if last_id ==None:
		return 1
	else:
		return last_id + 1

class TStg0Refflupcr1(models.Model):
    refflupcrrow_1 = models.IntegerField(db_column='RefFluPCRRow_1',unique=True,default=increment_refflupcrrow, primary_key=True)  # Field name made lowercase.
    refflufile_name = models.CharField(db_column='RefFluFile_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reffluoperator = models.CharField(db_column='RefFluOperator', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refflukitname = models.CharField(db_column='RefFluKitName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refflukitlot = models.CharField(db_column='RefFluKitLot', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refflukitexp = models.DateTimeField(db_column='RefFluKitExp', blank=True, null=True)  # Field name made lowercase.
    ref1_entered_by = models.CharField(db_column='Ref1_Entered_By', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ref1_entereddate = models.DateTimeField(db_column='Ref1_EnteredDate', blank=True, null=True)  # Field name made lowercase.
    refflu_date = models.DateTimeField(db_column='RefFlu_Date', blank=True, null=True)  # Field name made lowercase.
    sample = models.CharField(db_column='Sample', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refflua_well = models.CharField(db_column='RefFLuA_Well', max_length=5, blank=True, null=True)  # Field name made lowercase.
    refflua_cqvalue = models.CharField(db_column='RefFLuA_CqValue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refflua_interp = models.CharField(db_column='RefFLuA_Interp', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refflub_cqvalue = models.CharField(db_column='RefFLuB_CqValue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refflub_interp = models.CharField(db_column='RefFLuB_Interp', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refrsv_cqvalue = models.CharField(db_column='RefRSV_CqValue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refrsv_interp = models.CharField(db_column='RefRSV_Interp', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refnotes = models.CharField(db_column='RefNotes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reffluexcld = models.IntegerField(db_column='RefFluExcld', blank=True, null=True)  # Field name made lowercase.

    class Meta:
     #   managed = False
        db_table = 't_stg0_RefFluPCR_1'

    def __str__(self):
        return self.refflupcrrow_1

def increment_refflupcrrow_2():
	last_id = TStg0Refflupcr2.objects.all().aggregate(largest=models.Max('refflupcrrow_2'))['largest']
	if last_id ==None:
		return 1
	else:
		return last_id + 1

class TStg0Refflupcr2(models.Model):
    refflupcrrow_2 = models.IntegerField(db_column='RefFluPCRRow_2',unique=True,default=increment_refflupcrrow_2, primary_key=True)  # Field name made lowercase.
    refflufile_name = models.CharField(db_column='RefFluFile_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reffluoperator = models.CharField(db_column='RefFluOperator', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refflukitname = models.CharField(db_column='RefFluKitName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refflukitlot = models.CharField(db_column='RefFluKitLot', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refflukitexp = models.DateTimeField(db_column='RefFluKitExp', blank=True, null=True)  # Field name made lowercase.
    ref2_entered_by = models.CharField(db_column='Ref2_Entered_By', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ref2_entereddate = models.DateTimeField(db_column='Ref2_EnteredDate', blank=True, null=True)  # Field name made lowercase.
    refflu_date = models.DateTimeField(db_column='RefFlu_Date', blank=True, null=True)  # Field name made lowercase.
    sample = models.CharField(db_column='Sample', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refflua_well = models.CharField(db_column='RefFLuA_Well', max_length=5, blank=True, null=True)  # Field name made lowercase.
    refflua_cqvalue = models.CharField(db_column='RefFLuA_CqValue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refflua_interp = models.CharField(db_column='RefFLuA_Interp', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refflub_cqvalue = models.CharField(db_column='RefFLuB_CqValue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refflub_interp = models.CharField(db_column='RefFLuB_Interp', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refrsv_cqvalue = models.CharField(db_column='RefRSV_CqValue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refrsv_interp = models.CharField(db_column='RefRSV_Interp', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refnotes = models.CharField(db_column='RefNotes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reffluexcld = models.IntegerField(db_column='RefFluExcld', blank=True, null=True)  # Field name made lowercase.

    class Meta:
      #  managed = False
        db_table = 't_stg0_RefFluPCR_2'

    def __str__(self):
        return self.refflupcrrow_2


class TStg0Ecrf(models.Model):
    ecrfrow = models.IntegerField(db_column='eCRFRow')  # Field name made lowercase.
    subjectid = models.CharField(db_column='SubjectID', max_length=25, blank=True, null=True)  # Field name made lowercase.
    specimenid = models.CharField(db_column='SpecimenID', max_length=25, blank=True, null=True)  # Field name made lowercase.
    subject_age = models.CharField(db_column='Subject_Age', max_length=25, blank=True, null=True)  # Field name made lowercase.
    subject_sex = models.CharField(db_column='Subject_Sex', max_length=3, blank=True, null=True)  # Field name made lowercase.
    collection_date = models.DateTimeField(db_column='Collection_Date', blank=True, null=True)  # Field name made lowercase.
    symptom_date = models.DateTimeField(db_column='Symptom_Date', blank=True, null=True)  # Field name made lowercase.
    symptom_desc = models.TextField(db_column='Symptom_Desc', blank=True, null=True)  # Field name made lowercase.
    symptom_cough = models.CharField(db_column='Symptom_Cough', max_length=3, blank=True, null=True)  # Field name made lowercase.
    symptom_conges = models.CharField(db_column='Symptom_Conges', max_length=3, blank=True, null=True)  # Field name made lowercase.
    symptom_rhinorrhea = models.CharField(db_column='Symptom_Rhinorrhea', max_length=3, blank=True, null=True)  # Field name made lowercase.
    symptom_sore_throat = models.CharField(db_column='Symptom_Sore_Throat', max_length=3, blank=True, null=True)  # Field name made lowercase.
    symptom_fever = models.CharField(db_column='Symptom_Fever', max_length=3, blank=True, null=True)  # Field name made lowercase.
    symptom_headache = models.CharField(db_column='Symptom_Headache', max_length=3, blank=True, null=True)  # Field name made lowercase.
    symptom_myalgia = models.CharField(db_column='Symptom_Myalgia', max_length=3, blank=True, null=True)  # Field name made lowercase.
    symptom_other = models.TextField(db_column='Symptom_Other', blank=True, null=True)  # Field name made lowercase.
    symptom_hospitalized = models.CharField(db_column='Symptom_Hospitalized', max_length=25, blank=True, null=True)  # Field name made lowercase.
    influzab_kitname = models.CharField(db_column='InfluzAB_KitName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    influza_testresult = models.CharField(db_column='InfluzA_TestResult', max_length=25, blank=True, null=True)  # Field name made lowercase.
    influza_ctvalue = models.CharField(db_column='InfluzA_CTvalue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    influzb_testresult = models.CharField(db_column='InfluzB_TestResult', max_length=25, blank=True, null=True)  # Field name made lowercase.
    influzb_ctvalue = models.CharField(db_column='InfluzB_CTvalue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    rsv_kitname = models.CharField(db_column='RSV_KitName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rsv_testvalue = models.CharField(db_column='RSV_TestValue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    rsv_ctvalues = models.CharField(db_column='RSV_CTvalues', max_length=25, blank=True, null=True)  # Field name made lowercase.
    cov2_kitname = models.CharField(db_column='COV2_KitName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cov2_testresult = models.CharField(db_column='COV2_TestResult', max_length=25, blank=True, null=True)  # Field name made lowercase.
    cov2_ctvalue = models.CharField(db_column='COV2_CTvalue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    userid = models.CharField(max_length=255, blank=True, null=True)
    post_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_stg0_eCRF'

class TStg1Brpcr(models.Model):
    sampleid = models.CharField(db_column='SampleID', max_length=25, blank=True, primary_key=True)  # Field name made lowercase.
    inv_site = models.CharField(db_column='Inv_Site', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_equipment = models.CharField(db_column='Inv_Equipment', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_test_name = models.CharField(db_column='Inv_Test_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_test_date = models.CharField(db_column='Inv_Test_Date',max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_kit_name = models.CharField(db_column='Inv_Kit_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_kit_lotid = models.CharField(db_column='Inv_Kit_LotID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_kit_expiration_date = models.CharField(db_column='Inv_Kit_Expiration_Date',max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_operator = models.CharField(db_column='Inv_Operator', max_length=25, blank=True, null=True)  # Field name made lowercase.
    inv_well_id = models.CharField(db_column='Inv_Well_ID', max_length=25, blank=True, null=True)  # Field name made lowercase.
    inv_sarscov2_concentration = models.CharField(db_column='Inv_Sarscov2_Concentration', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_infa_concentration = models.CharField(db_column='Inv_InfA_Concentration', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_infb_concentration = models.CharField(db_column='Inv_InfB_Concentration', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_rp_concentration = models.CharField(db_column='Inv_RP_Concentration', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_sarscov2_interpretation = models.CharField(db_column='Inv_Sarscov2_Interpretation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_infa_interpretation = models.CharField(db_column='Inv_InfA_Interpretation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_infb_interpretation = models.CharField(db_column='Inv_InfB_Interpretation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_rp_interpretation = models.CharField(db_column='Inv_RP_Interpretation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_notes = models.TextField(db_column='Inv_Notes', blank=True, null=True)  # Field name made lowercase.
    excl_flag = models.IntegerField(db_column='Excl_Flag', blank=True, null=True)  # Field name made lowercase.
    userid = models.CharField(max_length=255, blank=True, null=True)
    post_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_stg1_BRPCR'
    def __str__(self):
        return self.sampleid
    def get_absolute_url(self):
       # return reverse('search:aliquot_add')
        return reverse("rvpsyndromic:index_rvp")



class TStg1Cov2(models.Model):
    sampleid = models.CharField(db_column='SampleID', max_length=25, blank=True, primary_key=True)  # Field name made lowercase.
    refcov2_test_name = models.CharField(db_column='RefCov2_Test_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refcov2_test_date = models.CharField(db_column='RefCov2_Test_Date',max_length=255, blank=True, null=True)  # Field name made lowercase.
    refcov2_kit_name = models.CharField(db_column='RefCov2_Kit_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refcov2_kit_lotid = models.CharField(db_column='RefCov2_Kit_LotID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refcov2_kit_expiration_date = models.CharField(db_column='RefCov2_Kit_Expiration_Date',max_length=255, blank=True, null=True)  #de lowercase.
    refcov2_operator = models.CharField(db_column='RefCov2_Operator', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refcov2_well_id = models.CharField(db_column='RefCov2_Well_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refcov2_n1_concentration = models.CharField(db_column='RefCov2_N1_Concentration', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refcov2_n2_concentration = models.CharField(db_column='RefCov2_N2_Concentration', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refcov2_rp_concentration = models.CharField(db_column='RefCov2_RP_Concentration', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refcov2_n1_droplet_count = models.CharField(db_column='RefCov2_N1_Droplet_Count', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refcov2_n2_droplet_count = models.CharField(db_column='RefCov2_N2_Droplet_Count', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refcov2_rp_droplet_count = models.CharField(db_column='RefCov2_RP_Droplet_Count', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refcov2_result_interpretation = models.CharField(db_column='RefCov2_Result_Interpretation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refcov2_notes = models.TextField(db_column='RefCov2_Notes', blank=True, null=True)  # Field name made lowercase.
    excl_flag = models.IntegerField(db_column='Excl_Flag')  # Field name made lowercase.
    userid = models.CharField(max_length=255, blank=True, null=True)
    post_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_stg1_COV2'

class TStg1Cov2Invalid(models.Model):
    sampleid = models.CharField(db_column='SampleID', max_length=25, blank=True, primary_key=True)  # Field name made lowercase.
    refcov2_test_name = models.CharField(db_column='RefCov2_Test_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refcov2_test_date = models.CharField(db_column='RefCov2_Test_Date',max_length=255, blank=True, null=True)  # Field name made lowercase.
    refcov2_kit_name = models.CharField(db_column='RefCov2_Kit_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refcov2_kit_lotid = models.CharField(db_column='RefCov2_Kit_LotID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refcov2_kit_expiration_date = models.CharField(db_column='RefCov2_Kit_Expiration_Date',max_length=255, blank=True, null=True)  # Field name made lowercase.
    refcov2_operator = models.CharField(db_column='RefCov2_Operator', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refcov2_well_id = models.CharField(db_column='RefCov2_Well_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refcov2_n1_concentration = models.CharField(db_column='RefCov2_N1_Concentration', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refcov2_n2_concentration = models.CharField(db_column='RefCov2_N2_Concentration', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refcov2_rp_concentration = models.CharField(db_column='RefCov2_RP_Concentration', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refcov2_n1_droplet_count = models.CharField(db_column='RefCov2_N1_Droplet_Count', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refcov2_n2_droplet_count = models.CharField(db_column='RefCov2_N2_Droplet_Count', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refcov2_rp_droplet_count = models.CharField(db_column='RefCov2_RP_Droplet_Count', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refcov2_result_interpretation = models.CharField(db_column='RefCov2_Result_Interpretation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refcov2_notes = models.TextField(db_column='RefCov2_Notes', blank=True, null=True)  # Field name made lowercase.
    excl_flag = models.IntegerField(db_column='Excl_Flag', blank=True, null=True)  # Field name made lowercase.
    userid = models.CharField(max_length=255, blank=True, null=True)
    post_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_stg1_COV2_INVALID'


class TStg1Cov2Update(models.Model):
    sampleid = models.CharField(db_column='SampleID', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refcov2_test_name = models.CharField(db_column='RefCov2_Test_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refcov2_test_date = models.DateField(db_column='RefCov2_Test_Date', blank=True, null=True)  # Field name made lowercase.
    refcov2_kit_name = models.CharField(db_column='RefCov2_Kit_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refcov2_kit_lotid = models.CharField(db_column='RefCov2_Kit_LotID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refcov2_kit_expiration_date = models.DateField(db_column='RefCov2_Kit_Expiration_Date', blank=True, null=True)  # Field name made lowercase.
    refcov2_operator = models.CharField(db_column='RefCov2_Operator', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refcov2_well_id = models.CharField(db_column='RefCov2_Well_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refcov2_n1_concentration = models.CharField(db_column='RefCov2_N1_Concentration', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refcov2_n2_concentration = models.CharField(db_column='RefCov2_N2_Concentration', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refcov2_rp_concentration = models.CharField(db_column='RefCov2_RP_Concentration', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refcov2_n1_droplet_count = models.CharField(db_column='RefCov2_N1_Droplet_Count', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refcov2_n2_droplet_count = models.CharField(db_column='RefCov2_N2_Droplet_Count', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refcov2_rp_droplet_count = models.CharField(db_column='RefCov2_RP_Droplet_Count', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refcov2_result_interpretation = models.CharField(db_column='RefCov2_Result_Interpretation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refcov2_notes = models.TextField(db_column='RefCov2_Notes', blank=True, null=True)  # Field name made lowercase.
    excl_flag = models.IntegerField(db_column='Excl_Flag', blank=True, null=True)  # Field name made lowercase.
    userid = models.CharField(max_length=255, blank=True, null=True)
    post_date = models.DateTimeField(blank=True, null=True)

    class Meta:
    #    managed = False
        db_table = 't_stg1_COV2_UPDATE'

class TStg1Cov2Pcr(models.Model):
    refcov2row_1 = models.IntegerField(db_column='RefCov2Row_1', blank=True, primary_key=True)  # Field name made lowercase.
    refcov2row_2 = models.IntegerField(db_column='RefCov2Row_2', blank=True, null=True)  # Field name made lowercase.
    refcov2file_name = models.CharField(db_column='RefCoV2File_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refcov2_date = models.DateTimeField(db_column='RefCoV2_Date', blank=True, null=True)  # Field name made lowercase.
    sample = models.CharField(db_column='Sample', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refcov2_well = models.CharField(db_column='RefCoV2_Well', max_length=5, blank=True, null=True)  # Field name made lowercase.
    refcov2_cqvalue = models.CharField(db_column='RefCoV2_CqValue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refcov2_interp = models.CharField(db_column='RefCoV2_Interp', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refcov2notes = models.CharField(db_column='RefCoV2Notes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refcov2exclud = models.IntegerField(db_column='RefCoV2Exclud', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_stg1_CoV2PCR'




class TStg1Ecrf(models.Model):
    subjectid = models.CharField(db_column='SubjectID', max_length=25, blank=True, primary_key=True)  # Field name made lowercase.
    specimenid = models.CharField(db_column='SpecimenID', max_length=25, blank=True, null=True)  # Field name made lowercase.
    subject_age = models.CharField(db_column='Subject_Age', max_length=25, blank=True, null=True)  # Field name made lowercase.
    subject_sex = models.CharField(db_column='Subject_Sex', max_length=3, blank=True, null=True)  # Field name made lowercase.
    subject_race = models.CharField(db_column='Subject_Race', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subject_ethnicity = models.CharField(db_column='Subject_Ethnicity', max_length=50, blank=True, null=True)  # Field name made lowercase.
    collection_date = models.CharField(db_column='Collection_Date',max_length=255, blank=True, null=True)  # Field name made lowercase.
    symptom_date = models.CharField(db_column='Symptom_Date',max_length=255, blank=True, null=True)  # Field name made lowercase.
    symptom_desc = models.TextField(db_column='Symptom_Desc', blank=True, null=True)  # Field name made lowercase.
    symptom_cough = models.CharField(db_column='Symptom_Cough', max_length=3, blank=True, null=True)  # Field name made lowercase.
    symptom_conges = models.CharField(db_column='Symptom_Conges', max_length=3, blank=True, null=True)  # Field name made lowercase.
    symptom_rhinorrhea = models.CharField(db_column='Symptom_Rhinorrhea', max_length=3, blank=True, null=True)  # Field name made lowercase.
    symptom_sore_throat = models.CharField(db_column='Symptom_Sore_Throat', max_length=3, blank=True, null=True)  # Field name made lowercase.
    symptom_fever = models.CharField(db_column='Symptom_Fever', max_length=3, blank=True, null=True)  # Field name made lowercase.
    symptom_headache = models.CharField(db_column='Symptom_Headache', max_length=3, blank=True, null=True)  # Field name made lowercase.
    symptom_myalgia = models.CharField(db_column='Symptom_Myalgia', max_length=3, blank=True, null=True)  # Field name made lowercase.
    symptom_other = models.TextField(db_column='Symptom_Other', blank=True, null=True)  # Field name made lowercase.
    symptom_hospitalized = models.CharField(db_column='Symptom_Hospitalized', max_length=25, blank=True, null=True)  # Field name made lowercase.
    influzab_kitname = models.CharField(db_column='InfluzAB_KitName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    influza_testresult = models.CharField(db_column='InfluzA_TestResult', max_length=25, blank=True, null=True)  # Field name made lowercase.
    influza_ctvalue = models.CharField(db_column='InfluzA_CTvalue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    influzb_testresult = models.CharField(db_column='InfluzB_TestResult', max_length=25, blank=True, null=True)  # Field name made lowercase.
    influzb_ctvalue = models.CharField(db_column='InfluzB_CTvalue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    rsv_kitname = models.CharField(db_column='RSV_KitName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rsv_testvalue = models.CharField(db_column='RSV_TestValue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    rsv_ctvalues = models.CharField(db_column='RSV_CTvalues', max_length=25, blank=True, null=True)  # Field name made lowercase.
    cov2_kitname = models.CharField(db_column='COV2_KitName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cov2_testresult = models.CharField(db_column='COV2_TestResult', max_length=25, blank=True, null=True)  # Field name made lowercase.
    cov2_ctvalue = models.CharField(db_column='COV2_CTvalue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    excl_flag = models.IntegerField(db_column='Excl_Flag')  # Field name made lowercase.
    userid = models.CharField(max_length=255, blank=True, null=True)
    post_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_stg1_ECRF'

    def __str__(self):
        return self.subjectid

    def get_absolute_url(self):
    #   return reverse('search:aliquot_add')
        return reverse("rvpsyndromic:index_rvp")

class TStg1EcrfUpdate(models.Model):
    subjectid = models.CharField(db_column='SubjectID', max_length=25, blank=True, null=True)  # Field name made lowercase.
    specimenid = models.CharField(db_column='SpecimenID', max_length=25, blank=True, null=True)  # Field name made lowercase.
    subject_age = models.CharField(db_column='Subject_Age', max_length=25, blank=True, null=True)  # Field name made lowercase.
    subject_sex = models.CharField(db_column='Subject_Sex', max_length=3, blank=True, null=True)  # Field name made lowercase.
    subject_race = models.CharField(db_column='Subject_Race', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subject_ethnicity = models.CharField(db_column='Subject_Ethnicity', max_length=50, blank=True, null=True)  # Field name made lowercase.
    collection_date = models.DateField(db_column='Collection_Date', blank=True, null=True)  # Field name made lowercase.
    symptom_date = models.DateField(db_column='Symptom_Date', blank=True, null=True)  # Field name made lowercase.
    symptom_desc = models.TextField(db_column='Symptom_Desc', blank=True, null=True)  # Field name made lowercase.
    symptom_cough = models.CharField(db_column='Symptom_Cough', max_length=3, blank=True, null=True)  # Field name made lowercase.
    symptom_conges = models.CharField(db_column='Symptom_Conges', max_length=3, blank=True, null=True)  # Field name made lowercase.
    symptom_rhinorrhea = models.CharField(db_column='Symptom_Rhinorrhea', max_length=3, blank=True, null=True)  # Field name made lowercase.
    symptom_sore_throat = models.CharField(db_column='Symptom_Sore_Throat', max_length=3, blank=True, null=True)  # Field name made lowercase.
    symptom_fever = models.CharField(db_column='Symptom_Fever', max_length=3, blank=True, null=True)  # Field name made lowercase.
    symptom_headache = models.CharField(db_column='Symptom_Headache', max_length=3, blank=True, null=True)  # Field name made lowercase.
    symptom_myalgia = models.CharField(db_column='Symptom_Myalgia', max_length=3, blank=True, null=True)  # Field name made lowercase.
    symptom_other = models.TextField(db_column='Symptom_Other', blank=True, null=True)  # Field name made lowercase.
    symptom_hospitalized = models.CharField(db_column='Symptom_Hospitalized', max_length=25, blank=True, null=True)  # Field name made lowercase.
    influzab_kitname = models.CharField(db_column='InfluzAB_KitName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    influza_testresult = models.CharField(db_column='InfluzA_TestResult', max_length=25, blank=True, null=True)  # Field name made lowercase.
    influza_ctvalue = models.CharField(db_column='InfluzA_CTvalue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    influzb_testresult = models.CharField(db_column='InfluzB_TestResult', max_length=25, blank=True, null=True)  # Field name made lowercase.
    influzb_ctvalue = models.CharField(db_column='InfluzB_CTvalue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    rsv_kitname = models.CharField(db_column='RSV_KitName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rsv_testvalue = models.CharField(db_column='RSV_TestValue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    rsv_ctvalues = models.CharField(db_column='RSV_CTvalues', max_length=25, blank=True, null=True)  # Field name made lowercase.
    cov2_kitname = models.CharField(db_column='COV2_KitName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cov2_testresult = models.CharField(db_column='COV2_TestResult', max_length=25, blank=True, null=True)  # Field name made lowercase.
    cov2_ctvalue = models.CharField(db_column='COV2_CTvalue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    excl_flag = models.IntegerField(db_column='Excl_Flag')  # Field name made lowercase.
    userid = models.CharField(max_length=255, blank=True, null=True)
    post_date = models.DateTimeField(blank=True, null=True)

    class Meta:
#        managed = False
        db_table = 't_stg1_ECRF_UPDATE'

class TStg1BrpcrInvalid(models.Model):
    sampleid = models.CharField(db_column='SampleID', max_length=25, blank=True, primary_key=True)  # Field name made lowercase.
    inv_site = models.CharField(db_column='Inv_Site', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_equipment = models.CharField(db_column='Inv_Equipment', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_test_name = models.CharField(db_column='Inv_Test_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_test_date = models.CharField(db_column='Inv_Test_Date', max_length=255,blank=True, null=True)  # Field name made lowercase.
    inv_kit_name = models.CharField(db_column='Inv_Kit_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_kit_lotid = models.CharField(db_column='Inv_Kit_LotID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_kit_expiration_date = models.CharField(db_column='Inv_Kit_Expiration_Date',max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_operator = models.CharField(db_column='Inv_Operator', max_length=25, blank=True, null=True)  # Field name made lowercase.
    inv_well_id = models.CharField(db_column='Inv_Well_ID', max_length=25, blank=True, null=True)  # Field name made lowercase.
    inv_sarscov2_concentration = models.CharField(db_column='Inv_Sarscov2_Concentration', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_infa_concentration = models.CharField(db_column='Inv_InfA_Concentration', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_infb_concentration = models.CharField(db_column='Inv_InfB_Concentration', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_rp_concentration = models.CharField(db_column='Inv_RP_Concentration', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_sarscov2_interpretation = models.CharField(db_column='Inv_Sarscov2_Interpretation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_infa_interpretation = models.CharField(db_column='Inv_InfA_Interpretation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_infb_interpretation = models.CharField(db_column='Inv_InfB_Interpretation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_rp_interpretation = models.CharField(db_column='Inv_RP_Interpretation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_notes = models.TextField(db_column='Inv_Notes', blank=True, null=True)  # Field name made lowercase.
    excl_flag = models.IntegerField(db_column='Excl_Flag', blank=True, null=True)  # Field name made lowercase.
    userid = models.CharField(max_length=255, blank=True, null=True)
    post_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_stg1_BRPCR_INVALID'


class TStg1BrpcrUpdate(models.Model):
    sampleid = models.CharField(db_column='SampleID', max_length=25, blank=True, null=True)  # Field name made lowercase.
    inv_site = models.CharField(db_column='Inv_Site', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_equipment = models.CharField(db_column='Inv_Equipment', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_test_name = models.CharField(db_column='Inv_Test_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_test_date = models.DateField(db_column='Inv_Test_Date', blank=True, null=True)  # Field name made lowercase.
    inv_kit_name = models.CharField(db_column='Inv_Kit_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_kit_lotid = models.CharField(db_column='Inv_Kit_LotID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_kit_expiration_date = models.DateField(db_column='Inv_Kit_Expiration_Date', blank=True, null=True)  # Field name made lowercase.
    inv_operator = models.CharField(db_column='Inv_Operator', max_length=25, blank=True, null=True)  # Field name made lowercase.
    inv_well_id = models.CharField(db_column='Inv_Well_ID', max_length=25, blank=True, null=True)  # Field name made lowercase.
    inv_sarscov2_concentration = models.CharField(db_column='Inv_Sarscov2_Concentration', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_infa_concentration = models.CharField(db_column='Inv_InfA_Concentration', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_infb_concentration = models.CharField(db_column='Inv_InfB_Concentration', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_rp_concentration = models.CharField(db_column='Inv_RP_Concentration', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_sarscov2_interpretation = models.CharField(db_column='Inv_Sarscov2_Interpretation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_infa_interpretation = models.CharField(db_column='Inv_InfA_Interpretation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_infb_interpretation = models.CharField(db_column='Inv_InfB_Interpretation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_rp_interpretation = models.CharField(db_column='Inv_RP_Interpretation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_notes = models.TextField(db_column='Inv_Notes', blank=True, null=True)  # Field name made lowercase.
    excl_flag = models.IntegerField(db_column='Excl_Flag', blank=True, null=True)  # Field name made lowercase.
    userid = models.CharField(max_length=255, blank=True, null=True)
    post_date = models.DateTimeField(blank=True, null=True)

    class Meta:
#        managed = False
        db_table = 't_stg1_BRPCR_UPDATE'

class TStg1Refflu(models.Model):
    sample = models.CharField(db_column='Sample', max_length=25, blank=True, primary_key=True)  # Field name made lowercase.
    reffluoperator = models.CharField(db_column='RefFluOperator', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refflukitname = models.CharField(db_column='RefFluKitName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refflukitlot = models.CharField(db_column='RefFluKitLot', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refflukitexp = models.CharField(db_column='RefFluKitExp',max_length=255, blank=True, null=True)  # Field name made lowercase.
    refflu_date = models.CharField(db_column='RefFlu_Date',max_length=255, blank=True, null=True)  # Field name made lowercase.
    refflua_well = models.CharField(db_column='RefFluA_Well', max_length=5, blank=True, null=True)  # Field name made lowercase.
    refflua_cqvalue = models.CharField(db_column='RefFluA_CqValue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refflua_interp = models.CharField(db_column='RefFluA_Interp', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refflub_well = models.CharField(db_column='RefFluB_Well', max_length=5, blank=True, null=True)  # Field name made lowercase.
    refflub_cqvalue = models.CharField(db_column='RefFluB_CqValue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refflub_interp = models.CharField(db_column='RefFluB_Interp', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refrsv_well = models.CharField(db_column='RefRSV_Well', max_length=5, blank=True, null=True)  # Field name made lowercase.
    refrsv_cqvalue = models.CharField(db_column='RefRSV_CqValue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refrsv_interp = models.CharField(db_column='RefRSV_Interp', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refnotes = models.TextField(db_column='RefNotes', blank=True, null=True)  # Field name made lowercase.
    excl_flag = models.IntegerField(db_column='Excl_Flag', blank=True, null=True)  # Field name made lowercase.
    userid = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_stg1_RefFlu'

class TStg1ReffluInvalid(models.Model):
    sample = models.CharField(db_column='Sample', max_length=25, blank=True, primary_key=True)  # Field name made lowercase.
    reffluoperator = models.CharField(db_column='RefFluOperator', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refflukitname = models.CharField(db_column='RefFluKitName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refflukitlot = models.CharField(db_column='RefFluKitLot', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refflukitexp = models.CharField(db_column='RefFluKitExp',max_length=255, blank=True, null=True)  # Field name made lowercase.
    refflu_date = models.CharField(db_column='RefFlu_Date',max_length=255, blank=True, null=True)  # Field name made lowercase.
    refflua_well = models.CharField(db_column='RefFluA_Well', max_length=5, blank=True, null=True)  # Field name made lowercase.
    refflua_cqvalue = models.CharField(db_column='RefFluA_CqValue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refflua_interp = models.CharField(db_column='RefFluA_Interp', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refflub_well = models.CharField(db_column='RefFluB_Well', max_length=5, blank=True, null=True)  # Field name made lowercase.
    refflub_cqvalue = models.CharField(db_column='RefFluB_CqValue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refflub_interp = models.CharField(db_column='RefFluB_Interp', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refrsv_well = models.CharField(db_column='RefRSV_Well', max_length=5, blank=True, null=True)  # Field name made lowercase.
    refrsv_cqvalue = models.CharField(db_column='RefRSV_CqValue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refrsv_interp = models.CharField(db_column='RefRSV_Interp', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refexclnotes = models.TextField(db_column='RefExclNotes', blank=True, null=True)  # Field name made lowercase.
    excl_flag = models.IntegerField(db_column='Excl_Flag', blank=True, null=True)  # Field name made lowercase.
    userid = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_stg1_RefFlu_INVALID'


class TStg1ReffluMatch(models.Model):
    dep1_sample = models.CharField(db_column='DEP1_Sample', max_length=25, blank=True, primary_key=True)  # Field name made lowercase.
    dep1_reffluoperator = models.CharField(db_column='DEP1_RefFluOperator', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dep1_refflukitname = models.CharField(db_column='DEP1_RefFluKitName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dep1_refflukitlot = models.CharField(db_column='DEP1_RefFluKitLot', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dep1_refflukitexp = models.CharField(db_column='DEP1_RefFluKitExp',max_length=255, blank=True, null=True)  # Field name made lowercase.
    dep1_refflu_date = models.CharField(db_column='DEP1_RefFlu_Date',max_length=255, blank=True, null=True)  # Field name made lowercase.
    dep1_refflua_well = models.CharField(db_column='DEP1_RefFLuA_Well', max_length=5, blank=True, null=True)  # Field name made lowercase.
    dep1_refflua_cqvalue = models.CharField(db_column='DEP1_RefFLuA_CqValue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    dep1_refflua_interp = models.CharField(db_column='DEP1_RefFLuA_Interp', max_length=25, blank=True, null=True)  # Field name made lowercase.
    dep1_refflub_well = models.CharField(db_column='DEP1_RefFLuB_Well', max_length=5, blank=True, null=True)  # Field name made lowercase.
    dep1_refflub_cqvalue = models.CharField(db_column='DEP1_RefFLuB_CqValue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    dep1_refflub_interp = models.CharField(db_column='DEP1_RefFLuB_Interp', max_length=25, blank=True, null=True)  # Field name made lowercase.
    dep1_refrsv_well = models.CharField(db_column='DEP1_RefRSV_Well', max_length=5, blank=True, null=True)  # Field name made lowercase.
    dep1_refrsv_cqvalue = models.CharField(db_column='DEP1_RefRSV_CqValue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    dep1_refrsv_interp = models.CharField(db_column='DEP1_RefRSV_Interp', max_length=25, blank=True, null=True)  # Field name made lowercase.
    dep1_refnotes = models.TextField(db_column='DEP1_RefNotes', blank=True, null=True)  # Field name made lowercase.
    dep1_excl_flag = models.IntegerField(db_column='DEP1_Excl_Flag', blank=True, null=True)  # Field name made lowercase.
    dep1_userid = models.CharField(db_column='DEP1_userid', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dep1_post_date = models.CharField(db_column='DEP1_post_date',max_length=255, blank=True, null=True)  # Field name made lowercase.
    dep2_sample = models.CharField(db_column='DEP2_Sample', max_length=25, blank=True, null=True)  # Field name made lowercase.
    dep2_reffluoperator = models.CharField(db_column='DEP2_RefFluOperator', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dep2_refflukitname = models.CharField(db_column='DEP2_RefFluKitName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dep2_refflukitlot = models.CharField(db_column='DEP2_RefFluKitLot', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dep2_refflukitexp = models.CharField(db_column='DEP2_RefFluKitExp',max_length=255, blank=True, null=True)  # Field name made lowercase.
    dep2_refflu_date = models.CharField(db_column='DEP2_RefFlu_Date',max_length=255, blank=True, null=True)  # Field name made lowercase.
    dep2_refflua_well = models.CharField(db_column='DEP2_RefFLuA_Well', max_length=5, blank=True, null=True)  # Field name made lowercase.
    dep2_refflua_cqvalue = models.CharField(db_column='DEP2_RefFLuA_CqValue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    dep2_refflua_interp = models.CharField(db_column='DEP2_RefFLuA_Interp', max_length=25, blank=True, null=True)  # Field name made lowercase.
    dep2_refflub_well = models.CharField(db_column='DEP2_RefFLuB_Well', max_length=5, blank=True, null=True)  # Field name made lowercase.
    dep2_refflub_cqvalue = models.CharField(db_column='DEP2_RefFLuB_CqValue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    dep2_refflub_interp = models.CharField(db_column='DEP2_RefFLuB_Interp', max_length=25, blank=True, null=True)  # Field name made lowercase.
    dep2_refrsv_well = models.CharField(db_column='DEP2_RefRSV_Well', max_length=5, blank=True, null=True)  # Field name made lowercase.
    dep2_refrsv_cqvalue = models.CharField(db_column='DEP2_RefRSV_CqValue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    dep2_refrsv_interp = models.CharField(db_column='DEP2_RefRSV_Interp', max_length=25, blank=True, null=True)  # Field name made lowercase.
    dep2_refnotes = models.TextField(db_column='DEP2_RefNotes', blank=True, null=True)  # Field name made lowercase.
    dep2_excl_flag = models.IntegerField(db_column='DEP2_Excl_Flag', blank=True, null=True)  # Field name made lowercase.
    dep2_userid = models.CharField(db_column='DEP2_userid', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dep2_post_date = models.CharField(db_column='DEP2_post_date',max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_stg1_RefFlu_Match'

class TStg1ReffluMismatch(models.Model):
    dep1_sample = models.CharField(db_column='DEP1_Sample', max_length=25, blank=True, primary_key=True)  # Field name made lowercase.
    dep1_reffluoperator = models.CharField(db_column='DEP1_RefFluOperator', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dep1_refflukitname = models.CharField(db_column='DEP1_RefFluKitName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dep1_refflukitlot = models.CharField(db_column='DEP1_RefFluKitLot', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dep1_refflukitexp = models.CharField(db_column='DEP1_RefFluKitExp',max_length=255, blank=True, null=True)  # Field name made lowercase.
    dep1_refflu_date = models.CharField(db_column='DEP1_RefFlu_Date',max_length=255, blank=True, null=True)  # Field name made lowercase.
    dep1_refflua_well = models.CharField(db_column='DEP1_RefFLuA_Well', max_length=5, blank=True, null=True)  # Field name made lowercase.
    dep1_refflua_cqvalue = models.CharField(db_column='DEP1_RefFLuA_CqValue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    dep1_refflua_interp = models.CharField(db_column='DEP1_RefFLuA_Interp', max_length=25, blank=True, null=True)  # Field name made lowercase.
    dep1_refflub_well = models.CharField(db_column='DEP1_RefFLuB_Well', max_length=5, blank=True, null=True)  # Field name made lowercase.
    dep1_refflub_cqvalue = models.CharField(db_column='DEP1_RefFLuB_CqValue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    dep1_refflub_interp = models.CharField(db_column='DEP1_RefFLuB_Interp', max_length=25, blank=True, null=True)  # Field name made lowercase.
    dep1_refrsv_well = models.CharField(db_column='DEP1_RefRSV_Well', max_length=5, blank=True, null=True)  # Field name made lowercase.
    dep1_refrsv_cqvalue = models.CharField(db_column='DEP1_RefRSV_CqValue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    dep1_refrsv_interp = models.CharField(db_column='DEP1_RefRSV_Interp', max_length=25, blank=True, null=True)  # Field name made lowercase.
    dep1_refnotes = models.TextField(db_column='DEP1_RefNotes', blank=True, null=True)  # Field name made lowercase.
    dep1_excl_flag = models.IntegerField(db_column='DEP1_Excl_Flag', blank=True, null=True)  # Field name made lowercase.
    dep1_userid = models.CharField(db_column='DEP1_userid', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dep1_post_date = models.CharField(db_column='DEP1_post_date',max_length=255, blank=True, null=True)  # Field name made lowercase.
    dep2_sample = models.CharField(db_column='DEP2_Sample', max_length=25, blank=True, null=True)  # Field name made lowercase.
    dep2_reffluoperator = models.CharField(db_column='DEP2_RefFluOperator', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dep2_refflukitname = models.CharField(db_column='DEP2_RefFluKitName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dep2_refflukitlot = models.CharField(db_column='DEP2_RefFluKitLot', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dep2_refflukitexp = models.CharField(db_column='DEP2_RefFluKitExp',max_length=255, blank=True, null=True)  # Field name made lowercase.
    dep2_refflu_date = models.CharField(db_column='DEP2_RefFlu_Date',max_length=255, blank=True, null=True)  # Field name made lowercase.
    dep2_refflua_well = models.CharField(db_column='DEP2_RefFLuA_Well', max_length=5, blank=True, null=True)  # Field name made lowercase.
    dep2_refflua_cqvalue = models.CharField(db_column='DEP2_RefFLuA_CqValue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    dep2_refflua_interp = models.CharField(db_column='DEP2_RefFLuA_Interp', max_length=25, blank=True, null=True)  # Field name made lowercase.
    dep2_refflub_well = models.CharField(db_column='DEP2_RefFLuB_Well', max_length=5, blank=True, null=True)  # Field name made lowercase.
    dep2_refflub_cqvalue = models.CharField(db_column='DEP2_RefFLuB_CqValue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    dep2_refflub_interp = models.CharField(db_column='DEP2_RefFLuB_Interp', max_length=25, blank=True, null=True)  # Field name made lowercase.
    dep2_refrsv_well = models.CharField(db_column='DEP2_RefRSV_Well', max_length=5, blank=True, null=True)  # Field name made lowercase.
    dep2_refrsv_cqvalue = models.CharField(db_column='DEP2_RefRSV_CqValue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    dep2_refrsv_interp = models.CharField(db_column='DEP2_RefRSV_Interp', max_length=25, blank=True, null=True)  # Field name made lowercase.
    dep2_refnotes = models.TextField(db_column='DEP2_RefNotes', blank=True, null=True)  # Field name made lowercase.
    dep2_excl_flag = models.IntegerField(db_column='DEP2_Excl_Flag', blank=True, null=True)  # Field name made lowercase.
    dep2_userid = models.CharField(db_column='DEP2_userid', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dep2_post_date = models.CharField(db_column='DEP2_post_date',max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_stg1_RefFlu_Mismatch'

class TStg2Demo(models.Model):
    subjectid = models.CharField(db_column='SubjectID', max_length=25, blank=True, primary_key=True)  # Field name made lowercase.
    specimenid = models.CharField(db_column='SpecimenID', max_length=25, blank=True, null=True)  # Field name made lowercase.
    subject_age = models.CharField(db_column='Subject_Age', max_length=25, blank=True, null=True)  # Field name made lowercase.
    subject_sex = models.CharField(db_column='Subject_Sex', max_length=3, blank=True, null=True)  # Field name made lowercase.
    subject_race = models.CharField(db_column='Subject_Race', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subject_ethnicity = models.CharField(db_column='Subject_Ethnicity', max_length=50, blank=True, null=True)  # Field name made lowercase.
    collection_date = models.CharField(db_column='Collection_Date', max_length=25, blank=True, null=True)  # Field name made lowercase.
    symptom_date = models.CharField(db_column='Symptom_Date', max_length=25, blank=True, null=True)  # Field name made lowercase.
    symptom_desc = models.TextField(db_column='Symptom_Desc', blank=True, null=True)  # Field name made lowercase.
    symptom_cough = models.CharField(db_column='Symptom_Cough', max_length=3, blank=True, null=True)  # Field name made lowercase.
    symptom_conges = models.CharField(db_column='Symptom_Conges', max_length=3, blank=True, null=True)  # Field name made lowercase.
    symptom_rhinorrhea = models.CharField(db_column='Symptom_Rhinorrhea', max_length=3, blank=True, null=True)  # Field name made lowercase.
    symptom_sore_throat = models.CharField(db_column='Symptom_Sore_Throat', max_length=3, blank=True, null=True)  # Field name made lowercase.
    symptom_fever = models.CharField(db_column='Symptom_Fever', max_length=3, blank=True, null=True)  # Field name made lowercase.
    symptom_headache = models.CharField(db_column='Symptom_Headache', max_length=3, blank=True, null=True)  # Field name made lowercase.
    symptom_myalgia = models.CharField(db_column='Symptom_Myalgia', max_length=3, blank=True, null=True)  # Field name made lowercase.
    symptom_other = models.TextField(db_column='Symptom_Other', blank=True, null=True)  # Field name made lowercase.
    symptom_hospitalized = models.CharField(db_column='Symptom_Hospitalized', max_length=25, blank=True, null=True)  # Field name made lowercase.
    influzab_kitname = models.CharField(db_column='InfluzAB_KitName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    influza_testresult = models.CharField(db_column='InfluzA_TestResult', max_length=25, blank=True, null=True)  # Field name made lowercase.
    influza_ctvalue = models.CharField(db_column='InfluzA_CTvalue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    influzb_testresult = models.CharField(db_column='InfluzB_TestResult', max_length=25, blank=True, null=True)  # Field name made lowercase.
    influzb_ctvalue = models.CharField(db_column='InfluzB_CTvalue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    rsv_kitname = models.CharField(db_column='RSV_KitName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rsv_testvalue = models.CharField(db_column='RSV_TestValue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    rsv_ctvalues = models.CharField(db_column='RSV_CTvalues', max_length=25, blank=True, null=True)  # Field name made lowercase.
    cov2_kitname = models.CharField(db_column='COV2_KitName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cov2_testresult = models.CharField(db_column='COV2_TestResult', max_length=25, blank=True, null=True)  # Field name made lowercase.
    cov2_ctvalue = models.CharField(db_column='COV2_CTvalue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    excl_flag = models.IntegerField(db_column='Excl_Flag', blank=True, null=True)  # Field name made lowercase.
    userid = models.CharField(max_length=255, blank=True, null=True)
    post_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_stg2_DEMO'

class TStg2Subjexcl(models.Model):
    subjectid = models.CharField(db_column='SubjectID', max_length=25, blank=True, primary_key=True)  # Field name made lowercase.
    specimenid = models.CharField(db_column='SpecimenID', max_length=25, blank=True, null=True)  # Field name made lowercase.
    subject_age = models.CharField(db_column='Subject_Age', max_length=25, blank=True, null=True)  # Field name made lowercase.
    subject_sex = models.CharField(db_column='Subject_Sex', max_length=3, blank=True, null=True)  # Field name made lowercase.
    subject_race = models.CharField(db_column='Subject_Race', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subject_ethnicity = models.CharField(db_column='Subject_Ethnicity', max_length=50, blank=True, null=True)  # Field name made lowercase.
    collection_date = models.CharField(db_column='Collection_Date', max_length=25, blank=True, null=True)  # Field name made lowercase.
    symptom_date = models.CharField(db_column='Symptom_Date', max_length=25, blank=True, null=True)  # Field name made lowercase.
    symptom_desc = models.TextField(db_column='Symptom_Desc', blank=True, null=True)  # Field name made lowercase.
    symptom_cough = models.CharField(db_column='Symptom_Cough', max_length=3, blank=True, null=True)  # Field name made lowercase.
    symptom_conges = models.CharField(db_column='Symptom_Conges', max_length=3, blank=True, null=True)  # Field name made lowercase.
    symptom_rhinorrhea = models.CharField(db_column='Symptom_Rhinorrhea', max_length=3, blank=True, null=True)  # Field name made lowercase.
    symptom_sore_throat = models.CharField(db_column='Symptom_Sore_Throat', max_length=3, blank=True, null=True)  # Field name made lowercase.
    symptom_fever = models.CharField(db_column='Symptom_Fever', max_length=3, blank=True, null=True)  # Field name made lowercase.
    symptom_headache = models.CharField(db_column='Symptom_Headache', max_length=3, blank=True, null=True)  # Field name made lowercase.
    symptom_myalgia = models.CharField(db_column='Symptom_Myalgia', max_length=3, blank=True, null=True)  # Field name made lowercase.
    symptom_other = models.TextField(db_column='Symptom_Other', blank=True, null=True)  # Field name made lowercase.
    symptom_hospitalized = models.CharField(db_column='Symptom_Hospitalized', max_length=25, blank=True, null=True)  # Field name made lowercase.
    influzab_kitname = models.CharField(db_column='InfluzAB_KitName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    influza_testresult = models.CharField(db_column='InfluzA_TestResult', max_length=25, blank=True, null=True)  # Field name made lowercase.
    influza_ctvalue = models.CharField(db_column='InfluzA_CTvalue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    influzb_testresult = models.CharField(db_column='InfluzB_TestResult', max_length=25, blank=True, null=True)  # Field name made lowercase.
    influzb_ctvalue = models.CharField(db_column='InfluzB_CTvalue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    rsv_kitname = models.CharField(db_column='RSV_KitName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rsv_testvalue = models.CharField(db_column='RSV_TestValue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    rsv_ctvalues = models.CharField(db_column='RSV_CTvalues', max_length=25, blank=True, null=True)  # Field name made lowercase.
    cov2_kitname = models.CharField(db_column='COV2_KitName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cov2_testresult = models.CharField(db_column='COV2_TestResult', max_length=25, blank=True, null=True)  # Field name made lowercase.
    cov2_ctvalue = models.CharField(db_column='COV2_CTvalue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    excl_flag = models.IntegerField(db_column='Excl_Flag', blank=True, null=True)  # Field name made lowercase.
    userid = models.CharField(max_length=255, blank=True, null=True)
    post_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_stg2_SUBJEXCL'

class TStg2Ad(models.Model):
    sampleid = models.CharField(db_column='SampleID', max_length=25, blank=True, primary_key=True)  # Field name made lowercase.
    inv_site = models.CharField(db_column='Inv_Site', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_equipment = models.CharField(db_column='Inv_Equipment', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_test_name = models.CharField(db_column='Inv_Test_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_test_date = models.CharField(db_column='Inv_Test_Date', max_length=25, blank=True, null=True)  # Field name made lowercase.
    inv_operator = models.CharField(db_column='Inv_Operator', max_length=25, blank=True, null=True)  # Field name made lowercase.
    inv_well_id = models.CharField(db_column='Inv_Well_ID', max_length=25, blank=True, null=True)  # Field name made lowercase.
    inv_sarscov2_concentration = models.CharField(db_column='Inv_Sarscov2_Concentration', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_infa_concentration = models.CharField(db_column='Inv_InfA_Concentration', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_infb_concentration = models.CharField(db_column='Inv_InfB_Concentration', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_rp_concentration = models.CharField(db_column='Inv_RP_Concentration', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_sarscov2_interpretation = models.CharField(db_column='Inv_Sarscov2_Interpretation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_infa_interpretation = models.CharField(db_column='Inv_InfA_Interpretation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_infb_interpretation = models.CharField(db_column='Inv_InfB_Interpretation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_rp_interpretation = models.CharField(db_column='Inv_RP_Interpretation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reffluoperator = models.CharField(db_column='RefFluOperator', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refflukitname = models.CharField(db_column='RefFluKitName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refflu_date = models.CharField(db_column='RefFlu_Date', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refflua_well = models.CharField(db_column='RefFluA_Well', max_length=5, blank=True, null=True)  # Field name made lowercase.
    refflub_well = models.CharField(db_column='RefFluB_Well', max_length=5, blank=True, null=True)  # Field name made lowercase.
    refrsv_well = models.CharField(db_column='RefRSV_Well', max_length=5, blank=True, null=True)  # Field name made lowercase.
    refflua_cqvalue = models.CharField(db_column='RefFluA_CqValue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refflub_cqvalue = models.CharField(db_column='RefFluB_CqValue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refrsv_cqvalue = models.CharField(db_column='RefRSV_CqValue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refflua_interp = models.CharField(db_column='RefFluA_Interp', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refflub_interp = models.CharField(db_column='RefFluB_Interp', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refrsv_interp = models.CharField(db_column='RefRSV_Interp', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refcov2_test_name = models.CharField(db_column='RefCov2_Test_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refcov2_test_date = models.CharField(db_column='RefCov2_Test_Date', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refcov2_kit_name = models.CharField(db_column='RefCov2_Kit_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refcov2_operator = models.CharField(db_column='RefCov2_Operator', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refcov2_well_id = models.CharField(db_column='RefCov2_Well_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refcov2_n1_concentration = models.CharField(db_column='RefCov2_N1_Concentration', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refcov2_n2_concentration = models.CharField(db_column='RefCov2_N2_Concentration', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refcov2_rp_concentration = models.CharField(db_column='RefCov2_RP_Concentration', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refcov2_n1_droplet_count = models.CharField(db_column='RefCov2_N1_Droplet_Count', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refcov2_n2_droplet_count = models.CharField(db_column='RefCov2_N2_Droplet_Count', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refcov2_rp_droplet_count = models.CharField(db_column='RefCov2_RP_Droplet_Count', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refcov2_result_interpretation = models.CharField(db_column='RefCov2_Result_Interpretation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inv_notes = models.TextField(db_column='Inv_Notes', blank=True, null=True)  # Field name made lowercase.
    ref_notes = models.TextField(db_column='Ref_Notes', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_stg2_AD'
