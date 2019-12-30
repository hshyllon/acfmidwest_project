from django.contrib import admin
from .models import Blog, BlogAuthor, BlogComment
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


class BlogAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    readonly_fields = ('create_date','update_date',)
# Register your models here.

class BlogAuthorAdmin(admin.ModelAdmin):
    readonly_fields = ('create_date','update_date',)
    
class BlogCommentAdmin(admin.ModelAdmin):
    readonly_fields = ('create_date','update_date',)

admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogAuthor)
admin.site.register(BlogComment)