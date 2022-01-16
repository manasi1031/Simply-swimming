from . import views
from django.urls import path


urlpatterns = [
    path('about/', views.About.as_view(), name='about'),
    path('<slug:slug>/', views.CourseDetail.as_view(), name='course_detail'),
]