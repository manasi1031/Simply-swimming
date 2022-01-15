from django.urls import path
from .views import HomeTemplateView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name="home"),
    path('about/', HomeTemplateView.as_view(), name="about"),
]