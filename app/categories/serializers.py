from rest_framework import serializers
from core.models import Category


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for category"""
    class Meta:
        model = Category
        fields = ['category_id', 'category_name',
                  'category_name_id', 'category_rank','category_image_url', 'is_active']
        read_only_fields = ['category_id']


