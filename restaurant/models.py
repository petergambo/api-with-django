from django.db import models


# Create your models here.
class Booking(models.Model):
   first_name = models.CharField(max_length=200)    
   last_name = models.CharField(max_length=200)
   guest_number = models.IntegerField()
   comment = models.CharField(max_length=1000)

   def __str__(self):
      return self.first_name + ' ' + self.last_name


# Add code to create Menu model
class Menu(models.Model):
   dish_name= models.CharField(max_length=100)
   dish_discription=models.CharField(max_length=1000)
   dish_price=models.IntegerField()
   def __str__(self):
      return self.dish_name