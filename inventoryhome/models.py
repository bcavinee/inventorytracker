from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import F

# Create your models here.

#Each class is a table in the database



class Hematology_Inventory(models.Model):

    reagent_name= models.CharField(max_length=30, unique=True)
    reagent_quantity= models.IntegerField()

    def __str__(self):
        return self.reagent_name

class Chemistry_Inventory(models.Model):

    reagent_name= models.CharField(max_length=30, unique=True)
    reagent_quantity= models.IntegerField()

    def __str__(self):
        return self.reagent_name
