from django.db import models
from account.models import Account
from act.models import Activity
from classroom.models import Classroom
from django.core.validators import FileExtensionValidator

class VideoFiles(models.Model):

    INTEGER_CHOICES= [tuple([x,x]) for x in range(1,11)]

    title = models.CharField(max_length=100)
    activity_number = models.IntegerField(null = True,choices=INTEGER_CHOICES,default = 1)
    video = models.FileField(upload_to='videos/', validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
    transcript = models.TextField(null=True, blank=True, max_length=5000)
    audio = models.FileField(null=False, blank=False)
    expected = models.IntegerField(null=True, blank=False)
    actual = models.IntegerField(null=True, blank=False)
    accuracy = models.IntegerField(null=True, blank=False)
    student = models.ForeignKey(Account, default=None, on_delete=models.CASCADE)
    act = models.ForeignKey(Activity, default = None,blank = True,null = True, on_delete=models.CASCADE)
    clss = models.ForeignKey(Classroom, default = None,blank = True,null = True, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'
        
    def __str__(self):
        return self.title + ": " + str(self.video)

        