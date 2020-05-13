from django.contrib import admin
from django.utils.html import format_html

from .models import WineItem, SurveyResponse, SurveyQuestion, SurveyQuestionResponse, SurveyABTestInstance

# Register your models here.
class WineItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'bottle_image_thumbnail_html', 'label_type', 'price', 'description', 'wine_type', 'varietal')
    list_editable = ('label_type','wine_type', 'varietal')
    readonly_fields = ['bottle_image_thumbnail_html']

admin.site.register(WineItem, WineItemAdmin)
admin.site.register(SurveyResponse)
admin.site.register(SurveyQuestion)
admin.site.register(SurveyQuestionResponse)
admin.site.register(SurveyABTestInstance)