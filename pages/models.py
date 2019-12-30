from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Volunteer(models.Model):
    fullname = models.CharField(max_length=128, blank=False)
    email = models.EmailField(blank=False)
    address = models.CharField(max_length=256, blank=False)
    phone = models.CharField(max_length=16, blank = False)
    occupation = models.CharField(max_length=256, blank=True)
    message = models.TextField('Message', max_length=128, blank=False)
    create_date = models.DateTimeField('date created', auto_now_add=True, auto_now=False, null = True)
    update_date = models.DateTimeField('date updated',auto_now_add=False, auto_now=True, null = True)
    
    def __str__(self):
        return u'%s | %s' %(self.fullname, self.email)
    
class Album(models.Model):
    appuser = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    album_title = models.CharField(max_length=128, blank=False, null = False)
    description = models.TextField(max_length=256, blank=True, null = True)
    is_published = models.BooleanField(default = True)
    create_date = models.DateTimeField('date created', auto_now_add=True, auto_now=False, null = True)
    update_date = models.DateTimeField(auto_now_add=False, auto_now=True, null = True)
    
    def __str__(self):
        return self.album_title

class Photo(models.Model):
    appuser = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    photo_album = models.ForeignKey(Album, blank = False, on_delete=models.DO_NOTHING)
    #description = models.TextField(max_length=255, blank=True, null = True)
    photo = models.ImageField(upload_to = 'photo_gallery/%Y/%m/%d/', blank= False)
    album_cover = models.BooleanField(default = False)
    is_published = models.BooleanField(default = True)
    create_date = models.DateTimeField('date created', auto_now_add=True, auto_now=False, null = True)
    update_date = models.DateTimeField(auto_now_add=False, auto_now=True, null = True)
    
#     def __str__(self):
#         return self.description
    
