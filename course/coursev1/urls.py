from rest_framework import routers
from django.urls import path, include
from . import views

routers = routers.DefaultRouter()

routers.register('category', views.CategoryViewSet, 'category')
routers.register('course', views.CourseViewSet, 'courses')

urlpatterns = [
    path("", include(routers.urls))
]
