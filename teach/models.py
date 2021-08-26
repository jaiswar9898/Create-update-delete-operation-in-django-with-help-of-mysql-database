from django.db import models

# Create your models here.
from django.db import models
import MySQLdb as Database
from django.forms import ModelForm, Textarea
from django.db import models 
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

# create a tuple for the status of each post
class Employee(models.Model):
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=100)
    eemail = models.CharField(max_length=100)
    econtact = models.CharField(max_length=30)