"""categories paths"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from categories import views

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet)

app_name = 'categories'

urlpatterns = [
    path('', include(router.urls))
]
