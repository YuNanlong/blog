from django.contrib import admin
from .models import Category, Post

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'publish', 'status')
    list_editable = ('category', 'status')
    list_filter = ('category', 'publish', 'status')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'

admin.site.register(Post, PostAdmin)
