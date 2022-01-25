"""Application configuration for contactme app"""
from django.apps import AppConfig


class ContactmeConfig(AppConfig):
    """Contactme app config"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contactme'
