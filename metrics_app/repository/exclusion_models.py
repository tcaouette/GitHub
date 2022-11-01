# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BrpcrExclusionTrans(models.Model):
    id = models.CharField(max_length=50, blank=True, null=True)
    user = models.CharField(max_length=50, blank=True, null=True)
    date_exclusion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'brpcr_exclusion_trans'


class EcrfExclusionTrans(models.Model):
    ecrfrow = models.IntegerField(blank=True, null=True)
    subjectid = models.CharField(max_length=50, blank=True, null=True)
    specimenid = models.CharField(max_length=50, blank=True, null=True)
    user = models.CharField(max_length=50, blank=True, null=True)
    date_exclusion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ecrf_exclusion_trans'


class Stg1Cov2PcrExclTrans(models.Model):
    refcov2row_1 = models.IntegerField(blank=True, null=True)
    refcov2row_2 = models.IntegerField(blank=True, null=True)
    refcov2_date = models.DateTimeField(blank=True, null=True)
    sample = models.CharField(max_length=50, blank=True, null=True)
    user = models.CharField(max_length=50, blank=True, null=True)
    date_exclusion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stg1_cov2pcr_excl_trans'


class Stg1RefflupcrExclTrans(models.Model):
    refflupcrrow_1 = models.IntegerField(blank=True, null=True)
    refflupcrrow_2 = models.IntegerField(blank=True, null=True)
    refrun_date = models.DateTimeField(blank=True, null=True)
    user = models.CharField(max_length=50, blank=True, null=True)
    date_exclusion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stg1_refflupcr_excl_trans'


class TStg0Brpcr(models.Model):
    brpcrrow = models.AutoField(db_column='BRPCRRow')  # Field name made lowercase.
    file_name = models.CharField(db_column='File_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    created_by = models.CharField(db_column='Created_By', max_length=255, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(db_column='ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
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
    refcov2row_1 = models.AutoField(db_column='RefCov2Row_1')  # Field name made lowercase.
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
    refcov2row_2 = models.AutoField(db_column='RefCov2Row_2')  # Field name made lowercase.
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


class TStg0Refflupcr1(models.Model):
    refflupcrrow_1 = models.IntegerField(db_column='RefFluPCRRow_1', blank=True, null=True)  # Field name made lowercase.
    refflufile_name = models.CharField(db_column='RefFluFile_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reffluoperator = models.CharField(db_column='RefFluOperator', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ref1_entered_by = models.CharField(db_column='Ref1_Entered_By', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ref1_entereddate = models.DateTimeField(db_column='Ref1_EnteredDate', blank=True, null=True)  # Field name made lowercase.
    refflu_date = models.DateTimeField(db_column='RefFlu_Date', blank=True, null=True)  # Field name made lowercase.
    sample = models.CharField(db_column='Sample', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refflua_well = models.CharField(db_column='RefFLuA_Well', max_length=5, blank=True, null=True)  # Field name made lowercase.
    refflua_cqvalue = models.CharField(db_column='RefFLuA_CqValue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refflua_interp = models.CharField(db_column='RefFLuA_Interp', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refflub_well = models.CharField(db_column='RefFLuB_Well', max_length=5, blank=True, null=True)  # Field name made lowercase.
    refflub_cqvalue = models.CharField(db_column='RefFLuB_CqValue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refflub_interp = models.CharField(db_column='RefFLuB_Interp', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refnotes = models.CharField(db_column='RefNotes', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_stg0_RefFluPCR_1'


class TStg0Refflupcr2(models.Model):
    refflupcrrow_2 = models.IntegerField(db_column='RefFluPCRRow_2')  # Field name made lowercase.
    refflufile_name = models.CharField(db_column='RefFluFile_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reffluoperator = models.CharField(db_column='RefFluOperator', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ref2_entered_by = models.CharField(db_column='Ref2_Entered_By', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ref2_entereddate = models.DateTimeField(db_column='Ref2_EnteredDate', blank=True, null=True)  # Field name made lowercase.
    refflu_date = models.DateTimeField(db_column='RefFlu_Date', blank=True, null=True)  # Field name made lowercase.
    sample = models.CharField(db_column='Sample', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refflua_well = models.CharField(db_column='RefFLuA_Well', max_length=5, blank=True, null=True)  # Field name made lowercase.
    refflua_cqvalue = models.CharField(db_column='RefFLuA_CqValue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refflua_interp = models.CharField(db_column='RefFLuA_Interp', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refflub_well = models.CharField(db_column='RefFLuB_Well', max_length=5, blank=True, null=True)  # Field name made lowercase.
    refflub_cqvalue = models.CharField(db_column='RefFLuB_CqValue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refflub_interp = models.CharField(db_column='RefFLuB_Interp', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refnotes = models.CharField(db_column='RefNotes', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_stg0_RefFluPCR_2'


class TStg0Ecrf(models.Model):
    ecrfrow = models.AutoField(db_column='eCRFRow')  # Field name made lowercase.
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

    class Meta:
        managed = False
        db_table = 't_stg0_eCRF'


class TStg1Brpcr(models.Model):
    brpcrrow = models.IntegerField(db_column='BRPCRRow')  # Field name made lowercase.
    file_name = models.CharField(db_column='File_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    created_by = models.CharField(db_column='Created_By', max_length=255, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(db_column='ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
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
    brpcr_exclud = models.IntegerField(db_column='BRPCR_Exclud', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_stg1_BRPCR'


class TStg1Cov2Pcr(models.Model):
    refcov2row_1 = models.IntegerField(db_column='RefCov2Row_1', blank=True, null=True)  # Field name made lowercase.
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


class TStg1Refflupcr(models.Model):
    refflupcrrow_1 = models.IntegerField(db_column='RefFluPCRRow_1', blank=True, null=True)  # Field name made lowercase.
    refflupcrrow_2 = models.IntegerField(db_column='RefFluPCRRow_2', blank=True, null=True)  # Field name made lowercase.
    reffile_name = models.CharField(db_column='RefFile_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refrun_date = models.DateTimeField(db_column='RefRun_Date', blank=True, null=True)  # Field name made lowercase.
    sample = models.CharField(db_column='Sample', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refflua_well = models.CharField(db_column='RefFLuA_Well', max_length=5, blank=True, null=True)  # Field name made lowercase.
    refflua_cqvalue = models.CharField(db_column='RefFLuA_CqValue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refflua_interp = models.CharField(db_column='RefFLuA_Interp', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refflub_well = models.CharField(db_column='RefFLuB_Well', max_length=5, blank=True, null=True)  # Field name made lowercase.
    refflub_cqvalue = models.CharField(db_column='RefFLuB_CqValue', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refflub_interp = models.CharField(db_column='RefFLuB_Interp', max_length=25, blank=True, null=True)  # Field name made lowercase.
    refnotes = models.CharField(db_column='RefNotes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    refflupcrexcld = models.IntegerField(db_column='RefFluPCRExcld', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_stg1_RefFluPCR'


class TStg1Ecrf(models.Model):
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
    sampleexclud = models.IntegerField(db_column='SampleExclud', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_stg1_eCRF'
