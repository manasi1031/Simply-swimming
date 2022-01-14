from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Appt


@admin.register(Appt)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('request')
