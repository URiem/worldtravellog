from django.contrib import admin
from .models import Logentry, Image, Country
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    """
    Register the Country model in the Admin area
    """
    list_display = ('ctry_title', 'slug', 'approved')
    list_filter = ('approved',)
    search_fields = ['ctry_title']
    prepopulated_fields = {'slug': ('ctry_title',)}
    actions = ['approve_country']

    def approve_country(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Logentry)
class LogentryAdmin(SummernoteModelAdmin):
    """
    Register the Logentry model in the Admin area
    """
    list_display = ('title', 'year', 'slug', 'status',
                    'privacy', 'date_created')
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'date_created')
    summernote_fields = ('description')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    """
    Register the Image model in the Admin area
    """
    list_display = ('logentry', 'caption', 'alttext')
