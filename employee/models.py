from django.db import models
import random

def create_new_eno():
    return random.randint(1000,9999)

# Create your models here.
class Employee(models.Model):
    probation_period_list = [
        ('1month','1 Month'),
        ('2month','2 Month'),
        ('3month','3 Month'),
    ]
    eno = models.CharField(max_length=4,blank=False,editable=False,unique=True,default=create_new_eno())
    hiredate = models.DateField()
    pfno = models.PositiveIntegerField()
    probation_period = models.CharField(choices=probation_period_list,max_length=100)

