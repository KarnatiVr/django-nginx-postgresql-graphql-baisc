from django.db import models

# Create your models here.
class Skills(models.Model):
    list=models.CharField(max_length=50)

    def __str__(self):
        return self.list
   

class Profile(models.Model):
    name=models.CharField(max_length=50,blank=False)
    role=models.CharField(max_length=50,blank=False)
    skills=models.ForeignKey(Skills,on_delete=models.CASCADE,related_name="techstack")

    def __str__(self):
        return self.name
   
