

from django.contrib import admin
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', "category", "url")
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'views', 'likes')


admin.site.register(Category)
admin.site.register(Page)
