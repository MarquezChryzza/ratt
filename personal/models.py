from django.db import models

class studentInfo(models.Model):
    title = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=550)

    def __str__(self):
        return self.title
class Data(models.Model):
    studentID = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.first_name
# Create your models here.
