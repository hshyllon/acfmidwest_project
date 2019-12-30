from django.contrib import admin
from .models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ('create_date','update_date',)


admin.site.register(Contact)