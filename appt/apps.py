"""Application configuration for appointment app"""
from django.apps import AppConfig


class ApptConfig(AppConfig):
    """Appointment configuration"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appt'
