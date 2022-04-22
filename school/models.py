from django.db import models
from datetime import date
# Create your models here.
class details(models.Model):
    name = models.CharField(max_length=20,default="0")
    gender = models.CharField(max_length=10,default="0")
    email= models.CharField(default="0",max_length=30)
    education = models.CharField(max_length=30,default="0")
    DOB = models.DateField(default=date(1111, 11, 11))
    contact = models.CharField(max_length=13,default="0")
    age = models.IntegerField(default="0")
    # cs = models.BooleanField(default=False)
    address = models.CharField(max_length=50,default="0")

    def __str__(self):
        return f"{self.name}+{self.contact}"



class notice(models.Model):
    name = models.CharField(default="0",max_length=30)
    desc = models.CharField(default="0",max_length=200)
    s_date = models.DateField(default=date(1111, 11, 11))
    associate_links= models.URLField(blank=True)
    imp=models.BooleanField(default=False)

    def __str__(self):
        return self.name

class all_urls(models.Model):
    link = models.URLField(blank=True)
    name=models.CharField(default="0",max_length=10)
    def __str__(self):
        return self.name
class to_do(models.Model):
    id =models.IntegerField(default="0",primary_key=True)
    work_due = models.CharField(default="0",max_length=200)
    due_date =models.DateField(default=date(1111, 11, 11))
    def __str__(self):
        return self.work_due
class upcomingevents(models.Model):
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to='upcoming_events',default='0')
    desc = models.CharField(max_length=200)
    def __str__(self):
        return self.name