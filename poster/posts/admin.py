from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ['slug', 'title', 'text', 'photo', 'is_published', 'pub_time', 'upd_time']
    list_display_links = ['slug', 'title']
    search_fields = ('title', 'text')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'pub_time', 'upd_time')
    prepopulated_fields = {"slug": ("title",)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
