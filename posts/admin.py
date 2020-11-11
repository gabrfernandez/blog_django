from django.contrib import admin
from .models import Post

# Register your models here.
#customize admin page to display search and filter by certain fields
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'id']
    list_display_links = ['title', 'date', 'id']
    search_fields = ['title', 'id']
    list_filter = ['date']
admin.site.register(Post, PostAdmin)

