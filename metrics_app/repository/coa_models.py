# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TUpCoa(models.Model):
    year = models.CharField(db_column='Year', max_length=5, blank=True, null=True)  # Field name made lowercase.
    lotid = models.CharField(db_column='LotID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    field_field = models.CharField(db_column='#', max_length=10, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    originalid = models.CharField(db_column='OriginalID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cofa = models.TextField(db_column='CofA', blank=True, null=True)  # Field name made lowercase.
    pdf_contents = models.TextField(db_column='PDF_Contents', blank=True, null=True)  # Field name made lowercase.
    comments = models.TextField(db_column='Comments', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_up_CoA'
