from django.db import models

# Create your models here.
class SignUpForm(models.Model):
    Name=models.CharField(max_length=30)
    Batch=models.IntegerField()
    Branch=models.CharField(max_length=20)
    Address=models.CharField(max_length=100)
    Mobile=models.IntegerField()
    Email=models.EmailField(max_length=50)
    
    def __str__(self): 
        return self.Name





class EventAlumniMeet(models.Model):
    FullName=models.CharField(max_length=200)
    FatherName=models.CharField(max_length=200)
    Batch=models.CharField(max_length=200)
    MobileNo=models.CharField(max_length=200)
    Email=models.EmailField()
    Address=models.CharField(max_length=500)
    URN=models.CharField(max_length=500)
    Branch=models.CharField(max_length=200)
    Course= models.CharField(max_length=200)
    Workingstatus=models.CharField(max_length=200)
    
    def __str__(self): 
        return self.FullName




