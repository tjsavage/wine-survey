from django.contrib import admin
from django.utils.html import format_html

from .models import WineItem

# Register your models here.
class WineItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'bottle_image_thumbnail_html', 'label_type')
    list_editable = ('label_type',)
    readonly_fields = ['bottle_image_thumbnail_html']

admin.site.register(WineItem, WineItemAdmin)
