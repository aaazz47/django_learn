from django.contrib import admin

# Register your models here.
from blog.models import Category, Tag, Post

# 通过定义类来控制后台显示的内容
class PostAdim(admin.ModelAdmin):
    list_display = ['title', 'pub_date', 'update_time', 'fen_lei', 'author']

# 使用 Django 提供的方法，快速注册后台管理的模型
admin.site.register(Post, PostAdim)
admin.site.register(Category)
admin.site.register(Tag)