from django.db import models
from django.db.models import DateField,CharField,ForeignKey,IntegerField
#from django.Eastern import models
# from django.Eastern.models import DateField,CharField,ForeignKey,IntegerField
# Create your models here.
# BALANCE_TYPE = ((u'收入',u'收入'),(u'支出',u'支出'))
# class Category(models.Model):
# 	#user     = 
# 	category = CharField(max_length=20)
# 	def __str__(self):
# 		return self.category

# class Record(models.Model):
# 	#user        = 
# 	date        = DateField()
# 	description = CharField(max_length=300)
# 	category    = ForeignKey(Category,on_delete=models.SET_NULL,null=True)
# 	cash        = IntegerField()
# 	balance_type= CharField(max_length=2,choices=BALANCE_TYPE)
# 	def __str__(self):
# 		return self.description

# class Eastern(models.Model):
# 	url=CharField(max_length=300)
# 	getTime=DateField()
# 	title=CharField(max_length=300)
# 	address=CharField(max_length=300)
# 	lat_lng=CharField(max_length=300)
# 	floor=IntegerField()
# 	rent_dollars=IntegerField()
# 	deposit_dollars=IntegerField()
# 	minimum_live_month=IntegerField()
# 	pings=FloatField()
# 	use=CharField(max_length=300)
# 	type=CharField(max_length=300)
# 	pattern=CharField(max_length=300)
# 	parking=CharField(max_length=300)
# 	management_fee_dollars=IntegerField()
# 	MRT=CharField(max_length=300)
# 	bus_station=CharField(max_length=300)
# 	school=CharField(max_length=300)
# 	business_district=CharField(max_length=300)
# 	furniture=CharField(max_length=300)
# 	equipment=CharField(max_length=300)
# 	features_recommended=CharField(max_length=2000)

# 	def __str__(self):
# 		return self.address