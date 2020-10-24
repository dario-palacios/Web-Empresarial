from django.contrib import admin

# Register your models here.
from .models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('tittle', 'author', 'published')
    ordering = ('author', 'published')
    search_fields = ('tittle', 'content', 'author__username', 'category__name')
    date_hierarchy = 'published'
    list_filter = ('author__username', 'category__name')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
