from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from classroom.models import Classroom

# Create your models here.
class Activity(models.Model):
    a_name = models.CharField(null=True, max_length=100)
    a_number = models.PositiveIntegerField(null = True, validators = [MaxValueValidator(10), MinValueValidator(1)], default = 1)
    a_material = models.TextField(null=True, max_length=1000)
    expected_total = models.IntegerField(null=True, blank=False)
    clss = models.ForeignKey(Classroom, default = None,blank = True,null = True, on_delete=models.CASCADE)
    
   
    def __str__(self):
        return self.a_name +" "+ str(self.clss)