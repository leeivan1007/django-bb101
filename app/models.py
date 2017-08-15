# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Cat(models.Model):
    bigcatid = models.CharField(db_column='bigCatID', max_length=1, blank=True, primary_key=True)  # Field name made lowercase.
    bigcatname = models.CharField(db_column='bigCatName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    midcatid = models.CharField(db_column='midCatID', max_length=2, blank=True, null=True)  # Field name made lowercase.
    midcatname = models.CharField(db_column='midCatName', max_length=40, blank=True, null=True)  # Field name made lowercase.
    smlcatid = models.CharField(db_column='smlCatID', max_length=3, blank=True, null=True)  # Field name made lowercase.
    smlcatname = models.CharField(db_column='smlCatName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dtlcatid = models.CharField(db_column='dtlCatID', max_length=4, blank=True, null=True)  # Field name made lowercase.
    dtlcatname = models.CharField(db_column='dtlCatName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcatid = models.CharField(db_column='subCatID', primary_key=True, max_length=6)  # Field name made lowercase.
    subcatname = models.CharField(db_column='subCatName', max_length=80, blank=True, null=True)  # Field name made lowercase.
    udfcatid = models.ForeignKey('Catudf', models.DO_NOTHING, db_column='udfCatID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cat'


class Catudf(models.Model):
    catid = models.CharField(db_column='catID', primary_key=True, max_length=10 )  # Field name made lowercase.
    description = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catudf'


class City(models.Model):
    cityid = models.IntegerField(db_column='CityID', primary_key=True)  # Field name made lowercase.
    cityname = models.CharField(db_column='CityName', max_length=20, blank=True )  # Field name made lowercase.
    cityname_cn = models.CharField(db_column='CityName_CN', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'city'


class Distance(models.Model):
    url = models.CharField(max_length=100, blank=True, primary_key=True)
    green = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    food = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    leasure = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    hospital = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    mrt = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'distance'


class Pub(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=8, blank=True, primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=150, blank=True, null=True)  # Field name made lowercase.
    cityid = models.ForeignKey(City, models.DO_NOTHING, db_column='CityID', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=200, blank=True, null=True)  # Field name made lowercase.
    catid = models.ForeignKey(Catudf, models.DO_NOTHING, db_column='catID', blank=True, null=True)  # Field name made lowercase.
    lng = models.DecimalField(max_digits=15, decimal_places=11, blank=True, null=True)
    lat = models.DecimalField(max_digits=15, decimal_places=11, blank=True, null=True)
    area = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pub'


class Rental(models.Model):
    url = models.CharField(unique=True, max_length=100, blank=True, primary_key=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    cityid = models.ForeignKey(City, models.DO_NOTHING, db_column='cityID', blank=True, null=True)  # Field name made lowercase.
    area = models.CharField(db_column='Area', max_length=6, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(max_length=200, blank=True, null=True)
    pattern = models.CharField(max_length=50, blank=True, null=True)
    floor = models.IntegerField(blank=True, null=True)
    stories = models.IntegerField(blank=True, null=True)
    label = models.CharField(max_length=1, blank=True, null=True)
    rent = models.IntegerField(blank=True, null=True)
    lat = models.DecimalField(max_digits=15, decimal_places=11, blank=True, null=True)
    lng = models.DecimalField(max_digits=15, decimal_places=11, blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    space = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    smoke = models.CharField(max_length=1, blank=True, null=True)
    pet = models.CharField(max_length=1, blank=True, null=True)
    cook = models.CharField(max_length=1, blank=True, null=True)
    parking = models.CharField(max_length=1, blank=True, null=True)
    updatedate = models.DateField(db_column='updateDate', blank=True, null=True)  # Field name made lowercase.
    label2 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rental'


class Rental10Pa(models.Model):
    url = models.CharField(max_length=100, blank=True, primary_key=True)
    cityid = models.IntegerField(db_column='cityID', blank=True, null=True)  # Field name made lowercase.
    area = models.CharField(db_column='Area', max_length=6, blank=True, null=True)  # Field name made lowercase.
    food = models.IntegerField(blank=True, null=True)
    green = models.IntegerField(blank=True, null=True)
    leasure = models.IntegerField(blank=True, null=True)
    hospital = models.IntegerField(blank=True, null=True)
    mrt = models.IntegerField(blank=True, null=True)
    score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rental10pa'


class Stdid(models.Model):
    id = models.CharField(db_column='ID', unique=True, max_length=8, blank=True, primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=150, blank=True, null=True)  # Field name made lowercase.
    cityid = models.ForeignKey(City, models.DO_NOTHING, db_column='CityID', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=200, blank=True, null=True)  # Field name made lowercase.
    catid = models.ForeignKey(Cat, models.DO_NOTHING, db_column='catID', blank=True, null=True)  # Field name made lowercase.
    lng = models.DecimalField(max_digits=15, decimal_places=11, blank=True, null=True)
    lat = models.DecimalField(max_digits=15, decimal_places=11, blank=True, null=True)
    area = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stdid'
