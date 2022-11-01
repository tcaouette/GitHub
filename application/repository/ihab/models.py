from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# This is the Primary Data Entry Person
class stg1_dataentryperson_ihab_abid_1(models.Model):
    site_code = models.CharField(db_column = 'SiteCode', max_length = 5, blank = True, null = True)  # Sitecode
    sample_id = models.CharField(db_column = 'SampleID', max_length = 50, blank = True, null = True)  # SampleID
    analyte = models.SmallIntegerField(db_column = 'Analyte', blank = True, null = True)  # Analyte = Panel 11 IgG(1)/Papain (2)/Panel Plus 6 (3) 
    test_date = models.DateTimeField(db_column = 'TestDate', blank = True, null = True)  # Test date 
    method = models.SmallIntegerField(db_column = 'Method', blank = True, null = True)  # Method = test(1)/reference(2)/referee(3)
    rep = models.SmallIntegerField(db_column = 'Rep', blank = True, null = True)  # Rep = initial(1)/repeat(2) 
    lot = models.CharField(db_column = 'Lot', max_length = 50, blank = True, null = True)  # LotID
    lot_exp = models.DateTimeField(db_column = 'LotExpDate', blank = True, null = True)  # Lot expiration date 
    exc_comments = models.TextField(db_column = 'ExclusionComments', blank = True, null = True)  # Exclusion comments (for Line Listings).
    misc_comments = models.TextField(db_column = 'MiscComments', blank = True, null = True)  # Miscellaneous comments (NOT for line listings).
    #data_entry_id = models.ForeignKey(get_user_model(), db_column = 'DataEntryPersonID', blank = True, null = True)  # date entry person id 
    date_entry_datetime = models.DateTimeField(db_column = 'DateEntryTime', auto_now_add=True, blank = True)  # data entry transaction time 
    i_well_1 = models.SmallIntegerField(db_column = 'Init_WellResult_1', blank = True, null = True)  # Well 1 initial id -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
    i_well_2 = models.SmallIntegerField(db_column = 'Init_WellResult_2', blank = True, null = True)  # Well 2 initial id -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
    i_well_3 = models.SmallIntegerField(db_column = 'Init_WellResult_3', blank = True, null = True)  # Well 3 initial id -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
    i_well_4 = models.SmallIntegerField(db_column = 'Init_WellResult_4', blank = True, null = True)  # Well 4 initial id -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
    i_well_5 = models.SmallIntegerField(db_column = 'Init_WellResult_5', blank = True, null = True)  # Well 5 initial id -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
    i_well_6 = models.SmallIntegerField(db_column = 'Init_WellResult_6', blank = True, null = True)  # Well 6 initial id -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
    i_well_7 = models.SmallIntegerField(db_column = 'Init_WellResult_7', blank = True, null = True)  # Well 7 initial id -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
    i_well_8 = models.SmallIntegerField(db_column = 'Init_WellResult_8', blank = True, null = True)  # Well 8 initial id -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
    i_well_9 = models.SmallIntegerField(db_column = 'Init_WellResult_9', blank = True, null = True)  # Well 9 initial id -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
    i_well_10 = models.SmallIntegerField(db_column = 'Init_WellResult_10', blank = True, null = True)  # Well 10 initial id -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
    i_well_11 = models.SmallIntegerField(db_column = 'Init_WellResult_11', blank = True, null = True)  # Well 11 initial id -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
    e_well_1 = models.SmallIntegerField(db_column = 'Edit_WellResult_1', blank = True, null = True)  # Well 1 edited id -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
    e_well_2 = models.SmallIntegerField(db_column = 'Edit_WellResult_2', blank = True, null = True)  # Well 2 edited id -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
    e_well_3 = models.SmallIntegerField(db_column = 'Edit_WellResult_3', blank = True, null = True)  # Well 3 edited id -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
    e_well_4 = models.SmallIntegerField(db_column = 'Edit_WellResult_4', blank = True, null = True)  # Well 4 edited id -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
    e_well_5 = models.SmallIntegerField(db_column = 'Edit_WellResult_5', blank = True, null = True)  # Well 5 edited id -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
    e_well_6 = models.SmallIntegerField(db_column = 'Edit_WellResult_6', blank = True, null = True)  # Well 6 edited id -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
    e_well_7 = models.SmallIntegerField(db_column = 'Edit_WellResult_7', blank = True, null = True)  # Well 7 edited id -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
    e_well_8 = models.SmallIntegerField(db_column = 'Edit_WellResult_8', blank = True, null = True)  # Well 8 edited id -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
    e_well_9 = models.SmallIntegerField(db_column = 'Edit_WellResult_9', blank = True, null = True)  # Well 9 edited id -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
    e_well_10 = models.SmallIntegerField(db_column = 'Edit_WellResult_10', blank = True, null = True)  # Well 10 edited id -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
    e_well_11 = models.SmallIntegerField(db_column = 'Edit_WellResult_11', blank = True, null = True)  # Well 11 edited id -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
 
    card_result = models.SmallIntegerField(db_column = 'CardResult', blank = True, null = True)  # Card summary result id -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
    abid_interp = models.CharField(db_column = 'AbID_Result', max_length = 50, blank = True, null = True)  # Antibody interpreted result 
    date_insert=models.CharField(db_column='Date_Inserted',max_length=50, blank=True, null=True)
    user=models.CharField(db_column='User', max_length=50, blank=True, null=True)

    class Meta:
        managed = False 
        db_table = 'stg1_dataentryperson_abid_1'
    def __str__(self):
        return self.sample_id

    def get_absolute_url(self):
       # return reverse('search:aliquot_add')
        return reverse("search:index")

# This is the Secondary Data Entry Person
class stg1_dataentryperson_ihab_abid_2(models.Model):
    site_code = models.CharField(db_column = 'SiteCode', max_length = 5, blank = True, null = True)  # Sitecode
    sample_id = models.CharField(db_column = 'SampleID', max_length = 50, blank = True, null = True)  # SampleID
    analyte = models.SmallIntegerField(db_column = 'Analyte', blank = True, null = True)  # Analyte = Panel 11 IgG(1)/Papain (2)/Panel Plus 6 (3) 
    test_date = models.DateTimeField(db_column = 'TestDate', blank = True, null = True)  # Test date 
    method = models.SmallIntegerField(db_column = 'Method', blank = True, null = True)  # Method = test(1)/reference(2)/referee(3)
    rep = models.SmallIntegerField(db_column = 'Rep', blank = True, null = True)  # Rep = initial(1)/repeat(2) 
    lot = models.CharField(db_column = 'Lot', max_length = 50, blank = True, null = True)  # LotID
    lot_exp = models.DateTimeField(db_column = 'LotExpDate', blank = True, null = True)  # Lot expiration date 
    exc_comments = models.TextField(db_column = 'ExclusionComments', blank = True, null = True)  # Exclusion comments (for Line Listings).
    misc_comments = models.TextField(db_column = 'MiscComments', blank = True, null = True)  # Miscellaneous comments (NOT for line listings).
    #data_entry_id = models.ForeignKey(get_user_model(), db_column = 'DataEntryPersonID', blank = True, null = True)  # date entry person id 
    date_entry_datetime = models.DateTimeField(db_column = 'DateEntryTime', auto_now_add=True, blank = True)  # data entry transaction time 
    i_well_1 = models.SmallIntegerField(db_column = 'Init_WellResult_1', blank = True, null = True)  # Well 1 initial id -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
    i_well_2 = models.SmallIntegerField(db_column = 'Init_WellResult_2', blank = True, null = True)  # Well 2 initial id -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
    i_well_3 = models.SmallIntegerField(db_column = 'Init_WellResult_3', blank = True, null = True)  # Well 3 initial id -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
    i_well_4 = models.SmallIntegerField(db_column = 'Init_WellResult_4', blank = True, null = True)  # Well 4 initial id -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
    i_well_5 = models.SmallIntegerField(db_column = 'Init_WellResult_5', blank = True, null = True)  # Well 5 initial id -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
    i_well_6 = models.SmallIntegerField(db_column = 'Init_WellResult_6', blank = True, null = True)  # Well 6 initial id -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
    i_well_7 = models.SmallIntegerField(db_column = 'Init_WellResult_7', blank = True, null = True)  # Well 7 initial id -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
    i_well_8 = models.SmallIntegerField(db_column = 'Init_WellResult_8', blank = True, null = True)  # Well 8 initial id -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
    i_well_9 = models.SmallIntegerField(db_column = 'Init_WellResult_9', blank = True, null = True)  # Well 9 initial id -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
    i_well_10 = models.SmallIntegerField(db_column = 'Init_WellResult_10', blank = True, null = True)  # Well 10 initial id -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
    i_well_11 = models.SmallIntegerField(db_column = 'Init_WellResult_11', blank = True, null = True)  # Well 11 initial id -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
    e_well_1 = models.SmallIntegerField(db_column = 'Edit_WellResult_1', blank = True, null = True)  # Well 1 edited id -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
    e_well_2 = models.SmallIntegerField(db_column = 'Edit_WellResult_2', blank = True, null = True)  # Well 2 edited id -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
    e_well_3 = models.SmallIntegerField(db_column = 'Edit_WellResult_3', blank = True, null = True)  # Well 3 edited id -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
    e_well_4 = models.SmallIntegerField(db_column = 'Edit_WellResult_4', blank = True, null = True)  # Well 4 edited id -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
    e_well_5 = models.SmallIntegerField(db_column = 'Edit_WellResult_5', blank = True, null = True)  # Well 5 edited id -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
    e_well_6 = models.SmallIntegerField(db_column = 'Edit_WellResult_6', blank = True, null = True)  # Well 6 edited id -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
    e_well_7 = models.SmallIntegerField(db_column = 'Edit_WellResult_7', blank = True, null = True)  # Well 7 edited id -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
    e_well_8 = models.SmallIntegerField(db_column = 'Edit_WellResult_8', blank = True, null = True)  # Well 8 edited id -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
    e_well_9 = models.SmallIntegerField(db_column = 'Edit_WellResult_9', blank = True, null = True)  # Well 9 edited id -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
    e_well_10 = models.SmallIntegerField(db_column = 'Edit_WellResult_10', blank = True, null = True)  # Well 10 edited id -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
    e_well_11 = models.SmallIntegerField(db_column = 'Edit_WellResult_11', blank = True, null = True)  # Well 11 edited id -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
    card_result = models.SmallIntegerField(db_column = 'CardResult', blank = True, null = True)  # Card summary result id -(1)/1+(2)/2+(3)/3+(4)/4+(5)/+-(6)/DP(7)/?(8)/E(9) 
    abid_interp = models.CharField(db_column = 'AbID_Result', max_length = 50, blank = True, null = True)  # Antibody interpreted result 
    date_insert=models.CharField(db_column='Date_Inserted',max_length=50, blank=True, null=True)
    user=models.CharField(db_column='User', max_length=50, blank=True, null=True)

    class Meta:
        managed = False  
        db_table = 'stg1_dataentryperson_abid_2'
    def __str__(self):
        return self.sample_id

    def get_absolute_url(self):
       # return reverse('search:aliquot_add')
        return reverse("search:index")
