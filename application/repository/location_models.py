# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class SearchCreateLocationTrans(models.Model):
    create_trans_id = models.IntegerField()
    user = models.CharField(db_column='User', max_length=50, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=50, blank=True, null=True)  # Field name made lowercase.
    locatino_abbr = models.CharField(db_column='Locatino_abbr', max_length=50, blank=True, null=True)  # Field name made lowercase.
    date_created = models.DateTimeField(db_column='Date_created', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'search_create_location_trans'
