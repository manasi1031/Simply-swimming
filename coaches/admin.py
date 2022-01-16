from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Coach

# Register your models here.


@admin.register(Coach)
class CoachAdmin(SummernoteModelAdmin):
    """Coaches app admin fields"""
    search_fields = ['coach_name', 'content']
    list_display = ('coach_name', 'status')
    summernote_fields = ('about')
