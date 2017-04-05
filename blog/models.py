from django.db import models
from django.conf import settings
from django.utils import timezone
class Post(models.Model):
    author = models.ForeignKey('auth.user')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    pub_date = models.DateTimeField(blank=True,null=True)
    def publikuj(self):
        self.pub_date=timezone.now()
        self.save()
    def __str__(self):
        return self.title
class Projekt(models.Model):
    author = models.ForeignKey('auth.user')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    edited_date = models.DateTimeField(blank=True,null=True)
    done = models.BooleanField(default=False)
    image_url=models.ImageField(upload_to="images",default='/images/no-img.jpg')
    def dodaj(self):
        self.edit_date=time.zone()
        self.save()
    def __str__(self):
        return self.title
    
# Create your models here.
