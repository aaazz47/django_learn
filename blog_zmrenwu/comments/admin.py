from django.contrib import admin

# Register your models here.
from comments.models import Comment

class CommentsAdmin(admin.ModelAdmin):
    list_display = ['post', 'text', 'user_name', 'created_time','email', 'url']

admin.site.register(Comment, CommentsAdmin)