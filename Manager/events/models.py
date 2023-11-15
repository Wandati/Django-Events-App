from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from datetime import date
class Venue(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    zipcode= models.CharField(max_length=50)
    email = models.EmailField(null=True,blank=True)
    web = models.URLField(null=True,blank=True)
    phone = models.CharField(max_length=20,null=True,blank=True)
    owner = models.IntegerField(blank=False,default=1)
    venue_img=models.ImageField(null=True,blank=True,upload_to="images/")
    
    def __str__(self):
        return self.name
    
class EventUser(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email_adress= models.EmailField(max_length=100)
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    
class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    description = models.TextField(null=True,blank=True)
    venue = models.ForeignKey(Venue,blank=True,null=True,on_delete=models.CASCADE)
    manager = models.ForeignKey(User,blank=True,null=True,on_delete=models.SET_NULL)
    attendees = models.ManyToManyField(EventUser,blank=True)
    is_approved=models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    @property
    def days_till(self):
        days = (self.date.date() - date.today()).days

        if days < 1:
            return "passed"
        else:
            return str(days)
   
   
       
        