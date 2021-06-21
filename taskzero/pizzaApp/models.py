from django.db.models.base import Model
from django.db.models.fields import AutoField, CharField, DateTimeField, PositiveBigIntegerField
from djongo import models
import uuid
import time
import datetime

# Create your models here.

class Pizza(models.Model):
    """ 
    pizza type : Regular OR Square
    pizza size : Multiple Sizes such as small large medium etc.
    """

    #id = PositiveBigIntegerField(primary_key=True, unique=True)

    typed = (
        ( "Regular" , "Regular" ),
        ( "Square"  , "Square"  ),
        )

    pizType = models.CharField(
        max_length=25,
        choices=typed,
        null=False)
    
    pizSize = models.CharField(
        max_length=25,
        null=False)

    pTops = models.CharField(max_length=100, null=False)
    
    #pTops = models.ForeignKey(PizzaTopping, on_delete=models.CASCADE)
    #pTops = models.ManyToManyField(PizzaTopping)

    pkey = models.CharField(max_length=155, unique=True, null=False, primary_key=True) 
    
    def getName(self):

        s = self.pizSize+" "+self.pizType+" Pizza with " + self.pTops + " Toppings"
        return s
    
    

