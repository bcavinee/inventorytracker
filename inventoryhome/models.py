from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import F
from datetime import datetime
from simple_history.models import HistoricalRecords

# Create your models here.

#Each class is a table in the database



class Hematology_Inventory(models.Model):

    reagent_name= models.CharField(max_length=30, unique=True)
    reagent_quantity= models.PositiveIntegerField()
    par_level= models.PositiveIntegerField()
    reagent_depletion= models.IntegerField()
    average_use= models.PositiveIntegerField()
    modfied= models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    @property
    def reagent_depletion(self):

        if self.reagent_quantity <= self.par_level:
            return True
        else:
            return False



    def __str__(self):
        return self.reagent_name


class Chemistry_Inventory(models.Model):

    reagent_name= models.CharField(max_length=30, unique=True)
    reagent_quantity= models.IntegerField()

    def __str__(self):
        return self.reagent_name

class Coagulation_Inventory(models.Model):

    reagent_name= models.CharField(max_length=30, unique=True)
    reagent_quantity= models.IntegerField()

    def __str__(self):
        return self.reagent_name

class Endo_Inventory(models.Model):

    reagent_name= models.CharField(max_length=30, unique=True)
    reagent_quantity= models.IntegerField()

    def __str__(self):
        return self.reagent_name

class Urines_Inventory(models.Model):

    reagent_name= models.CharField(max_length=30, unique=True)
    reagent_quantity= models.IntegerField()

    def __str__(self):
        return self.reagent_name


class GasesMetals_Inventory(models.Model):

    reagent_name= models.CharField(max_length=30, unique=True)
    reagent_quantity= models.IntegerField()

    def __str__(self):
        return self.reagent_name
