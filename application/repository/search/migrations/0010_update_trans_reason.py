# Generated by Django 2.1.14 on 2020-01-24 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0009_auto_20200124_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='update_trans',
            name='reason',
            field=models.CharField(blank=True, db_column='Reason', max_length=255, null=True),
        ),
    ]
