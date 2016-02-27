from __future__ import unicode_literals

from django.db import models


# Create your models here.

Accountant = 'Accountant'
Admin = 'Admin'
Employee='Employee'
TITLE_CHOICES = (
        (Accountant, 'Accountant'),
        (Admin, 'Admin'),
        (Employee,'Employee')
    )
# user of system 
class User(models.Model):
    user_name=models.CharField(max_length=1500)
    user_age=models.IntegerField(default=0)
    user_email=models.CharField(max_length=1500)
    user_password=models.CharField(max_length=1500)
    user_role=models.CharField(max_length=1500,choices=TITLE_CHOICES,default=Employee)
    def __unicode__(self):
        return  self.user_name

# images of slider
class ImgSlider(models.Model):
    img=models.CharField(max_length=1500)
    img_title=models.CharField(max_length=1500)
    def __unicode__(self):
        return self.img_title

# project class
class Project(models.Model):
	name=models.CharField(max_length=1500)
	start_date=models.DateField(auto_now=True)
	end_date=models.DateField(auto_now=True)
	def __unicode__(self):
		return self.name


# items that have bought 
class Item(models.Model):
    item_title=models.CharField(max_length=1500)
    item_price=models.CharField(max_length=1500)
    item_amount=models.CharField(max_length=1500)
    item_total=models.CharField(max_length=1500)
    item_date= models.DateField(auto_now=False)
    item_description=models.CharField(max_length=1500)
    project=models.ForeignKey(Project)
    def __unicode__(self):
        return self.item_title

# m2awelen of system
class M2awel(models.Model):
    name=models.CharField(max_length=1500)
    job=models.CharField(max_length=1500)
    money=models.IntegerField()
    paid=models.IntegerField()
    project=models.ForeignKey(Project)
    # no_card=models.IntegerField()
    def __unicode__(self):
        return self.name

# transactions of payment to m2awel
class Transaction(models.Model):
    action_paid=models.IntegerField()
    action_date=models.DateField(auto_now=False)
    m2awel=models.ForeignKey(M2awel)
    def __unicode__(self):
        return self.m2awel.name

# shekat data
class Shek(models.Model):
    num=models.IntegerField()
    date=models.DateField(auto_now=False)
    amount=models.IntegerField()
    project=models.ForeignKey(Project)
    def __unicode__(self):
        return self.num.__str__()
