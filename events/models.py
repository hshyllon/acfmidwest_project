from django.db import models
import datetime
#from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    photo = models.ImageField(upload_to='eventphotos', blank = False, null = True)
    photo2 = models.ImageField(upload_to='eventphotos', blank = False, null = True, default = "default image")
    title = models.CharField(max_length=256, blank=False)
    location = models.CharField(max_length=256, blank=False)
    city = models.CharField(max_length=64, blank=False, default = "City")
    start_day = models.DateField('Begin Day',default=datetime.date.today)
    start_time = models.TimeField('Begin Time',default=datetime.time)
    end_time = models.TimeField('End Time',default=datetime.time)
    #duration = models.DecimalField('Duration',default= '1.0', max_digits=5, decimal_places=1)
    adult_cost = models.DecimalField('Cost for Adult',default= '0', max_digits=7, decimal_places=2)
    youth_cost = models.DecimalField('Cost for Youth', default= '0', max_digits=7, decimal_places=2)
    children_cost = models.DecimalField('Cost for Child',default= '0', max_digits=7, decimal_places=2)
    description = models.TextField('Event Description',max_length=1024, blank=False)
    requirement = models.TextField('Event Requirement',max_length=1024, default = 'Enter Requirements here', blank=False)
    create_date = models.DateTimeField('date created', auto_now_add=True, auto_now=False, null = True)
    update_date = models.DateTimeField('date updated',auto_now_add=False, auto_now=True, null = True)
    is_published = models.BooleanField('Is Event Published?',default = False)
    
    def __str__(self):
        return u'%s %s' %(self.title, self.start_day)