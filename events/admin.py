from django.contrib import admin
from .models import Event
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


# class EventAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'start_day', 'start_time', 'is_published')
#     list_display_links = ('id', 'title')
#     list_editable = ('is_published',)
#     search_fields = ('title', 'description', 'location')
#     list_per_page = 25
# admin.site.register(Event, EventAdmin)

class EventAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    readonly_fields = ('create_date','update_date',)
admin.site.register(Event, EventAdmin)

