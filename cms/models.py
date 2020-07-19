from django.db import models

# Create your models here.
class ReportMenu(models.Model):
    tbl_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=5)
    display_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True, null=False, blank=False)

    class Meta:
        db_table = 'report_menus'


# mjcdata
class TblBranchImpAx(models.Model):
    brid = models.CharField(db_column='BRID', max_length=2)  # Field name made lowercase.
    brcode = models.CharField(db_column='BRCODE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    brabb = models.CharField(db_column='BRABB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    brname = models.CharField(db_column='BRNAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    axbu = models.CharField(db_column='AXBU', max_length=255, blank=True, null=True)  # Field name made lowercase.
    axdiv = models.CharField(db_column='AXDIV', max_length=255, blank=True, null=True)  # Field name made lowercase.
    axloc = models.FloatField(db_column='AXLOC', blank=True, null=True)  # Field name made lowercase.
    axcomp = models.FloatField(db_column='AXCOMP', blank=True, null=True)  # Field name made lowercase.
    filmhire = models.CharField(db_column='FILMHIRE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    regional = models.CharField(db_column='REGIONAL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vendorcd = models.CharField(db_column='VENDORCD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    filmhirempic = models.CharField(db_column='FILMHIREmpic', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tbl_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'tbl_Branch_imp_ax'


class TblMpicCustomerImpAx(models.Model):
    tbl_id = models.AutoField(primary_key=True)
    custcode = models.CharField(max_length=20)
    custname = models.CharField(max_length=255, blank=True, null=True)
    custaddress = models.CharField(max_length=255, blank=True, null=True)
    custgroup = models.CharField(max_length=5, blank=True, null=True)
    postprofile = models.CharField(max_length=5, blank=True, null=True)
    site = models.CharField(max_length=5, blank=True, null=True)
    warehouse = models.CharField(max_length=5, blank=True, null=True)
    buax = models.CharField(max_length=10, blank=True, null=True)
    divax = models.CharField(max_length=10, blank=True, null=True)
    locax = models.CharField(max_length=10, blank=True, null=True)
    intercocd = models.CharField(max_length=10, blank=True, null=True)
    custmapping = models.CharField(max_length=10, blank=True, null=True)
    amend_date = models.DateTimeField(blank=True, null=True)
    amend_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_Mpic_customer_imp_ax'


class TblMpicMovieImpAx(models.Model):
    tbl_id = models.AutoField(primary_key=True)
    mvcode = models.CharField(max_length=20)
    mvtitle = models.CharField(max_length=10)
    mvname = models.CharField(max_length=100, blank=True, null=True)
    unit_price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    perc_disc = models.FloatField(blank=True, null=True)
    mvmapping = models.CharField(max_length=50, blank=True, null=True)
    releasedate = models.CharField(max_length=8, blank=True, null=True)
    finishdate = models.CharField(max_length=8, blank=True, null=True)
    amend_date = models.DateTimeField(blank=True, null=True)
    amend_by = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_Mpic_movie_imp_ax'


# ticket_sale
class TblMv(models.Model):
    mv_id = models.IntegerField(db_column='MV_ID', primary_key=True)  # Field name made lowercase.
    mv_ename = models.CharField(db_column='MV_Ename', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mv_tname = models.CharField(db_column='MV_Tname', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mv_kname = models.CharField(db_column='MV_Kname', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mv_sname = models.CharField(db_column='MV_Sname', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mv_actor = models.CharField(db_column='MV_Actor', max_length=100, blank=True, null=True)  # Field name made lowercase.
    mv_actress = models.CharField(db_column='MV_Actress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    distributor_id = models.IntegerField(db_column='Distributor_ID', blank=True, null=True)  # Field name made lowercase.
    mv_time = models.IntegerField(db_column='MV_Time', blank=True, null=True)  # Field name made lowercase.
    mv_adtime = models.IntegerField(db_column='MV_AdTime', blank=True, null=True)  # Field name made lowercase.
    mv_releasedate = models.CharField(db_column='MV_ReleaseDate', max_length=8, blank=True, null=True)  # Field name made lowercase.
    mv_expiredate = models.CharField(db_column='MV_ExpireDate', max_length=8, blank=True, null=True)  # Field name made lowercase.
    mv_desc = models.CharField(db_column='MV_Desc', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mv_abstract = models.CharField(db_column='MV_Abstract', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mv_status = models.SmallIntegerField(db_column='MV_Status', blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.DateTimeField(db_column='LastUpdate', blank=True, null=True)  # Field name made lowercase.
    mv_groupid = models.IntegerField(db_column='MV_GroupID', blank=True, null=True)  # Field name made lowercase.
    mvnation_id = models.CharField(db_column='MVNation_ID', max_length=2, blank=True, null=True)  # Field name made lowercase.
    mvgenre_id = models.SmallIntegerField(db_column='MVGenre_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_mv'

# control_db
class TblUsersprofile(models.Model):
    userid = models.CharField(primary_key=True, max_length=30)
    username = models.CharField(max_length=150, blank=True, null=True)
    useremail = models.CharField(max_length=150, blank=True, null=True)
    userphone = models.CharField(max_length=150, blank=True, null=True)
    userpriv = models.CharField(max_length=1, blank=True, null=True)
    userlvl = models.CharField(max_length=1, blank=True, null=True)
    userstatus = models.CharField(max_length=1, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    amenddate = models.CharField(max_length=10, blank=True, null=True)
    amendby = models.CharField(max_length=50, blank=True, null=True)
    userdiv = models.CharField(max_length=5, blank=True, null=True)
    userext = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_usersprofile'


class TblReportmenus(models.Model):
    mnuid = models.AutoField(primary_key=True)
    mnulvl = models.CharField(max_length=1)
    mnucod = models.CharField(max_length=4)
    mnuname = models.CharField(max_length=512)
    mnudesc = models.TextField(blank=True, null=True)  # This field type is a guess.
    rptlvl = models.CharField(max_length=1, blank=True, null=True)
    rptpriv = models.CharField(max_length=1, blank=True, null=True)
    rptname = models.CharField(max_length=255, blank=True, null=True)
    rptlink = models.CharField(max_length=1024, blank=True, null=True)
    mnustatus = models.CharField(max_length=1, blank=True, null=True)
    istesting = models.CharField(db_column='isTesting', max_length=1, blank=True, null=True)  # Field name made lowercase.
    isproduction = models.CharField(db_column='isProduction', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rptstatus = models.CharField(db_column='rptStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rptowner = models.CharField(db_column='rptOwner', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rptlink1 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_reportmenus'
