"""
Admin for Appointment or bookings
"""

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Appt


@admin.register(Appt)
class PostAdmin(SummernoteModelAdmin):
    """
    Register Appointment
    """
    summernote_fields = ('request')
