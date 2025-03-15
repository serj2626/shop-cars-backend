from django.contrib import admin
from .models import Seo

@admin.register(Seo)
class SeoAdmin(admin.ModelAdmin):
    '''
    Админка SEO
    '''

    list_display = ('url',)
