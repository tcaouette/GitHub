# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class SearchFreezeThawTrans(models.Model):
    aqid = models.CharField(db_column='AqID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    freeze_thaw = models.IntegerField(db_column='Freeze_Thaw', blank=True, null=True)  # Field name made lowercase.
    datetime_freeze = models.DateTimeField(db_column='DateTime_Freeze', blank=True, null=True)  # Field name made lowercase.
    datetime_thaw = models.DateTimeField(db_column='DateTime_Thaw', blank=True, null=True)  # Field name made lowercase.
    user = models.CharField(db_column='User', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'search_freeze_thaw_trans'
