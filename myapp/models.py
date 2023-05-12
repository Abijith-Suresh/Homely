from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

    
from django.contrib.auth.models import User
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)


    def __str__(self):
        return self.user.username



class Listing(models.Model):
    listing_id = models.CharField(max_length=10, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property_name = models.CharField(max_length=100,blank=True, null=True)
    estimated_price = models.DecimalField(max_digits=20, decimal_places=2)
    address = models.CharField(max_length=100,blank=True, null=True)
    location= models.CharField(max_length=100,blank=True, null=True)
    description = models.CharField(max_length=100,blank=True, null=True)
    feature = models.IntegerField(blank=True, null=True)
    area = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    garage_space = models.IntegerField(blank=True, null=True)
    parking_space = models.IntegerField(blank=True, null=True)
    spa = models.CharField(max_length=10,blank=True, null=True)
    association = models.CharField(max_length=10,blank=True, null=True)
    heating = models.CharField(max_length=10,blank=True, null=True)
    cooling = models.CharField(max_length=10,blank=True, null=True)
    bedrooms = models.IntegerField(blank=True, null=True)
    bathrooms = models.IntegerField(blank=True, null=True)
    floors = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return f'{self.listing_id}: {self.property_name} ({self.user.username})'
    


class userwishlist(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   listingid = models.CharField(max_length=10)
   def __str__(self):
        return f'{self.listingid}: ({self.user.username})'


