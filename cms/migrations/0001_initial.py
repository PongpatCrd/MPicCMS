# Generated by Django 2.1 on 2020-06-18 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TblBranchImpAx',
            fields=[
                ('brid', models.CharField(db_column='BRID', max_length=2)),
                ('brcode', models.CharField(blank=True, db_column='BRCODE', max_length=4, null=True)),
                ('brabb', models.CharField(blank=True, db_column='BRABB', max_length=255, null=True)),
                ('brname', models.CharField(blank=True, db_column='BRNAME', max_length=255, null=True)),
                ('axbu', models.CharField(blank=True, db_column='AXBU', max_length=255, null=True)),
                ('axdiv', models.CharField(blank=True, db_column='AXDIV', max_length=255, null=True)),
                ('axloc', models.FloatField(blank=True, db_column='AXLOC', null=True)),
                ('axcomp', models.FloatField(blank=True, db_column='AXCOMP', null=True)),
                ('filmhire', models.CharField(blank=True, db_column='FILMHIRE', max_length=255, null=True)),
                ('regional', models.CharField(blank=True, db_column='REGIONAL', max_length=255, null=True)),
                ('vendorcd', models.CharField(blank=True, db_column='VENDORCD', max_length=255, null=True)),
                ('filmhirempic', models.CharField(blank=True, db_column='FILMHIREmpic', max_length=5, null=True)),
                ('tbl_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'tbl_Branch_imp_ax',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblMpicCustomerImpAx',
            fields=[
                ('tbl_id', models.AutoField(primary_key=True, serialize=False)),
                ('custcode', models.CharField(max_length=20)),
                ('custname', models.CharField(blank=True, max_length=255, null=True)),
                ('custaddress', models.CharField(blank=True, max_length=255, null=True)),
                ('custgroup', models.CharField(blank=True, max_length=5, null=True)),
                ('postprofile', models.CharField(blank=True, max_length=5, null=True)),
                ('site', models.CharField(blank=True, max_length=5, null=True)),
                ('warehouse', models.CharField(blank=True, max_length=5, null=True)),
                ('buax', models.CharField(blank=True, max_length=10, null=True)),
                ('divax', models.CharField(blank=True, max_length=10, null=True)),
                ('locax', models.CharField(blank=True, max_length=10, null=True)),
                ('intercocd', models.CharField(blank=True, max_length=10, null=True)),
                ('custmapping', models.CharField(blank=True, max_length=10, null=True)),
                ('amend_date', models.DateTimeField(blank=True, null=True)),
                ('amend_by', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'tbl_Mpic_customer_imp_ax',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblMpicMovieImpAx',
            fields=[
                ('tbl_id', models.AutoField(primary_key=True, serialize=False)),
                ('mvcode', models.CharField(max_length=20)),
                ('mvtitle', models.CharField(max_length=10)),
                ('mvname', models.CharField(blank=True, max_length=100, null=True)),
                ('unit_price', models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True)),
                ('perc_disc', models.FloatField(blank=True, null=True)),
                ('mvmapping', models.CharField(blank=True, max_length=50, null=True)),
                ('releasedate', models.CharField(blank=True, max_length=8, null=True)),
                ('finishdate', models.CharField(blank=True, max_length=8, null=True)),
                ('amend_date', models.DateTimeField(blank=True, null=True)),
                ('amend_by', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'tbl_Mpic_movie_imp_ax',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblMv',
            fields=[
                ('mv_id', models.IntegerField(db_column='MV_ID', primary_key=True, serialize=False)),
                ('mv_ename', models.CharField(blank=True, db_column='MV_Ename', max_length=100, null=True)),
                ('mv_tname', models.CharField(blank=True, db_column='MV_Tname', max_length=100, null=True)),
                ('mv_kname', models.CharField(blank=True, db_column='MV_Kname', max_length=100, null=True)),
                ('mv_sname', models.CharField(blank=True, db_column='MV_Sname', max_length=20, null=True)),
                ('mv_actor', models.CharField(blank=True, db_column='MV_Actor', max_length=100, null=True)),
                ('mv_actress', models.CharField(blank=True, db_column='MV_Actress', max_length=100, null=True)),
                ('distributor_id', models.IntegerField(blank=True, db_column='Distributor_ID', null=True)),
                ('mv_time', models.IntegerField(blank=True, db_column='MV_Time', null=True)),
                ('mv_adtime', models.IntegerField(blank=True, db_column='MV_AdTime', null=True)),
                ('mv_releasedate', models.CharField(blank=True, db_column='MV_ReleaseDate', max_length=8, null=True)),
                ('mv_expiredate', models.CharField(blank=True, db_column='MV_ExpireDate', max_length=8, null=True)),
                ('mv_desc', models.CharField(blank=True, db_column='MV_Desc', max_length=255, null=True)),
                ('mv_abstract', models.CharField(blank=True, db_column='MV_Abstract', max_length=255, null=True)),
                ('mv_status', models.SmallIntegerField(blank=True, db_column='MV_Status', null=True)),
                ('lastupdate', models.DateTimeField(blank=True, db_column='LastUpdate', null=True)),
                ('mv_groupid', models.IntegerField(blank=True, db_column='MV_GroupID', null=True)),
                ('mvnation_id', models.CharField(blank=True, db_column='MVNation_ID', max_length=2, null=True)),
                ('mvgenre_id', models.SmallIntegerField(blank=True, db_column='MVGenre_ID', null=True)),
            ],
            options={
                'db_table': 'tbl_mv',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblUsersprofile',
            fields=[
                ('userid', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=150, null=True)),
                ('useremail', models.CharField(blank=True, max_length=150, null=True)),
                ('userphone', models.CharField(blank=True, max_length=150, null=True)),
                ('userpriv', models.CharField(blank=True, max_length=1, null=True)),
                ('userlvl', models.CharField(blank=True, max_length=1, null=True)),
                ('userstatus', models.CharField(blank=True, max_length=1, null=True)),
                ('password', models.CharField(blank=True, max_length=50, null=True)),
                ('amenddate', models.CharField(blank=True, max_length=10, null=True)),
                ('amendby', models.CharField(blank=True, max_length=50, null=True)),
                ('userdiv', models.CharField(blank=True, max_length=5, null=True)),
                ('userext', models.CharField(blank=True, max_length=5, null=True)),
            ],
            options={
                'db_table': 'tbl_usersprofile',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReportMenu',
            fields=[
                ('tbl_id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=5)),
                ('desc', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'report_menus',
            },
        ),
    ]
