from django.contrib import admin
from .models import Volunteer, Photo, Album
# Register your models here.

class VolunteerAdmin(admin.ModelAdmin):
    readonly_fields = ('create_date','update_date',)

class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ('create_date','update_date',)

class PhotoAdmin(admin.ModelAdmin):
    readonly_fields = ('create_date','update_date',)

admin.site.register(Volunteer)
admin.site.register(Photo)
admin.site.register(Album)