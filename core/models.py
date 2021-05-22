from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.query import FlatValuesListIterable


# Create your models here.

class CustumUser(AbstractUser):

    born_day = models.DateField(null=False, blank=False)
    nick_name = models.CharField(max_length=100, unique=True)
    profile_picture = models.ImageField(upload_to='profile_picture')
    bio = models.CharField(max_length=250)
    mail = models.EmailField(unique=True)

    REQUIRED_FIELDS = ['born_day', 'nick_name']
    USERNAME_FIELD = 'mail'


    def __str__(self) -> str:
        return self.nick_name


class StyledImageCollection(models.Model):

    text_explanation = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True) 
    name = models.CharField(max_length=30)
    images = models.ManyToManyField('StyledImage')
    user = models.ForeignKey(CustumUser, on_delete=models.CASCADE)
    private = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.text_explanation


class StyleImageCollection(models.Model):

    text_explanation = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True) 
    name = models.CharField(max_length=30)
    images = models.ManyToManyField('StyleImage')
    user = models.ForeignKey(CustumUser, on_delete=models.CASCADE)
    private = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.text_explanation


class StyleImage(models.Model):

    image  =  models.ImageField(upload_to='StyleImage')
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustumUser, on_delete=models.CASCADE)
    text_explanation = models.TextField(null=True)
    private = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.text_explanation

class OriginalImage(models.Model):

    image  =  models.ImageField(upload_to='StyleImage')
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustumUser, on_delete=models.CASCADE)
    text_explanation = models.TextField(null=True)
    private = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.text_explanation


class StyledImage(models.Model):

    image  =  models.ImageField(upload_to='StyledImage')
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustumUser, on_delete=models.CASCADE)
    private = models.BooleanField(default=False)
    styleImage = models.ForeignKey(StyleImage, on_delete=models.CASCADE)
    originalImage = models.ForeignKey(OriginalImage, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.styleImage)+"--"+str(self.originalImage)

