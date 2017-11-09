from django.contrib import admin

# Register your models here.
from .models import Article, Person


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'update_time',)
    search_fields = ('title', 'counter',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()
    

class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Person, PersonAdmin)
