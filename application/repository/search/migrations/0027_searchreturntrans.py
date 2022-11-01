# Generated by Django 2.1 on 2020-09-14 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0026_auto_20200814_1404'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchReturnTrans',
            fields=[
                ('trans_id', models.AutoField(db_column='trans_id', primary_key=True, serialize=False)),
                ('boxid_in', models.CharField(blank=True, db_column='boxid_in', max_length=50, null=True)),
                ('ship_location', models.CharField(blank=True, db_column='ship_location', max_length=50, null=True)),
                ('date_returned', models.DateTimeField(blank=True, db_column='date_returned', null=True)),
                ('user', models.CharField(blank=True, db_column='user', max_length=50, null=True)),
                ('condition', models.CharField(blank=True, db_column='condition', max_length=50, null=True)),
            ],
            options={
                'db_table': 'search_return_trans',
                'managed': False,
            },
        ),
    ]