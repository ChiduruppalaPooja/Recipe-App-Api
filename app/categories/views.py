"""View for Category"""
from rest_framework import viewsets, status
from rest_framework.response import Response

from core.models import (
    Category,
    Item,
)

from categories import serializers
from items.serializers import ItemSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """View for managing categories"""
    serializer_class = serializers.CategorySerializer
    queryset = Category.objects.all().order_by('category_id')

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response(response.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(response.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response(response.data, status=status.HTTP_200_OK)

    def partial_update(self, request, *args, **kwargs):
        response = super().partial_update(request, *args, **kwargs)
        return Response(response.data, status=status.HTTP_200_OK)

    def update_status(self, request, *args, **kwargs):
        # logic
        instance = self.get_object()
        data = {'is_active': not instance.is_active}
        serializer = self.get_serializer(instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        items = Item.objects.filter(categories=instance)
        item_serializer = ItemSerializer(items, many=True)
        return Response({
                'category': serializer.data,
                'items': item_serializer.data
        })

