"""View for Category"""
from rest_framework import viewsets

from core.models import Category
from categories import serializers


class CategoryViewSet(viewsets.ModelViewSet):
    """View for managing categories"""
    serializer_class = serializers.CategorySerializer
    queryset = Category.objects.all()
