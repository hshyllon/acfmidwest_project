from django.db import models
import datetime
from django.contrib.auth.models import User


class BlogAuthor(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING) 
    photo =  models.ImageField(upload_to='blogAuthors', blank = False, null = True)
    intro = models.CharField(max_length=512, blank=False)
    create_date = models.DateTimeField('date created', auto_now_add=True, auto_now=False, null = True)
    update_date = models.DateTimeField('date updated',auto_now_add=False, auto_now=True, null = True)
    
    def __str__(self):
        return u'%s' %(self.author)
    
class Blog(models.Model):
    title = models.CharField(max_length=128, blank=False)
    author = models.ForeignKey(BlogAuthor, on_delete=models.DO_NOTHING)
    credit = models.CharField('Credit', max_length=128, blank=False)
    message = models.TextField('Blog Message', max_length=100000, blank=False)
    photo =  models.ImageField(upload_to='blogPhotos', blank = False, null = True)
    category = models.CharField('Blog Category', max_length=128, blank=False)
    tags = models.CharField('Blog Tags', max_length=128, blank=False)
    is_published = models.BooleanField('Is Blog Published?',default = False)
    create_date = models.DateTimeField('date created', auto_now_add=True, auto_now=False, null = True)
    update_date = models.DateTimeField('date updated',auto_now_add=False, auto_now=True, null = True)
    
    def __str__(self):
        return u'%s' %(self.title)

class BlogComment(models.Model):
    commentor = models.IntegerField(blank=False, default = -1)
    #commentor = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank = True) 
    #user_id = models.IntegerField(blank=True, default = 0)
    fullname = models.CharField(max_length=128, blank=True)
    email = models.EmailField(blank=True)
    #blog = models.ForeignKey(Blog, on_delete=models.DO_NOTHING)
    blog_title = models.CharField(max_length=256, blank=True)
    blog = models.IntegerField(blank=False, default = -1)
    comment = models.TextField('Blog Message', max_length=128, blank=False)
    is_approved = models.BooleanField('Is Comment Approved?',default = False)
    create_date = models.DateTimeField('date created', auto_now_add=True, auto_now=False, null = True)
    update_date = models.DateTimeField('date updated',auto_now_add=False, auto_now=True, null = True)
    
    def __str__(self):
        return u'%s | %s' %(self.blog_title, self.fullname)
    
    