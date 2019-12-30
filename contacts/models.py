from django.db import models

# Create your models here.
class Contact(models.Model):
    fullname = models.CharField(max_length=128, blank=False)
    email = models.EmailField(blank=False)
    phone = models.CharField(max_length=16, blank = False)
    message = models.TextField('Message', max_length=128, blank=False)
    create_date = models.DateTimeField('date created', auto_now_add=True, auto_now=False, null = True)
    update_date = models.DateTimeField('date updated',auto_now_add=False, auto_now=True, null = True)
    
    def __str__(self):
        return u'%s | %s' %(self.fullname, self.email)