from django.db import models
from django.contrib.auth.models import  AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from classroom.models import Classroom


class MyAccountManager(BaseUserManager):
    def create_student(self,username, password=None):
        if not username:
            raise ValueError("User must have username")

        user = self.model(
            username = username,
            password = password
            )
        user.set_password(password) 
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_student(
            password = password,
            username = username,
            )
        user.is_admin = True
        user.is_staff = True       
        user.is_superuser = True 
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    username                =models.CharField(max_length=60, unique=True)
    date_joined             =models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_joined             =models.DateTimeField(verbose_name='last login', auto_now_add=True)
    
    first_name              =models.CharField(max_length=60, default='')
    last_name               =models.CharField(max_length=60, default='')

    is_admin                =models.BooleanField(default=False)
    is_active               =models.BooleanField(default=True)
    is_staff                =models.BooleanField(default=False)
    is_superuser            =models.BooleanField(default=False)
    is_student              =models.BooleanField(default=False)
    is_teacher              =models.BooleanField(default=False)

    classroom               =models.ForeignKey(Classroom,null = True,blank = True,default = None,on_delete=models.CASCADE)
    

    USERNAME_FIELD = 'username'
    #REQUIRED_FIELDS = ['username',]

    objects = MyAccountManager()

    def __str__(self) -> str:
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
    
   


class Student(models.Model):
    user                    =models.OneToOneField(Account,on_delete=models.CASCADE,primary_key=True)
    age                     =models.CharField(max_length=60)
    """ first_name          =models.CharField(max_length=60, default='')
    last_name               =models.CharField(max_length=60, default='') """

class Teacher(models.Model):
    user                    =models.OneToOneField(Account,on_delete=models.CASCADE,primary_key=True)
    age                     =models.CharField(max_length=60)
