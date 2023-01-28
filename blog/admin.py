from django.contrib import admin
from .models import BlogCategory, PostModel, Comment

# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created')

admin.site.register(PostModel, PostModelAdmin)
admin.site.register(Comment)
admin.site.register(BlogCategory)