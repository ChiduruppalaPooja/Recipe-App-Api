from rest_framework import serializers
from core.models import Item, FoodType


class FoodTypeSerializer(serializers.ModelSerializer):
    """Serializer for Food Type"""
    class Meta:
        model = FoodType
        fields = ['food_type_id', 'food_type_name']
        read_only_fields = ['food_type_id']


class ItemSerializer(serializers.ModelSerializer):
    """Serializer for Item"""
    class Meta:
        model = Item
        fields = ['item_id', 'item_name',
                  'item_description', 'item_price', 'item_type', 'item_image_url', 'cgst', 'sgst','is_active']
        read_only_fields = ['item_id']

    # def create(self, validated_data):
    #     instance = super().create(validated_data)  # This saves the instance
    #     return instance
