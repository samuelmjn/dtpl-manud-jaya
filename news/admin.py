from django.contrib import admin
from .models import News


# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date', 'author')
    list_filter = ('category', 'date', 'author')
    search_fields = ('title', 'content', 'category', 'author')
    date_hierarchy = 'date'
    ordering = ('-date',)
    
    # Membuat field readonly setelah pembuatan
    readonly_fields = ('date', 'slug')