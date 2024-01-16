

from django.urls import (
   path,
   include,
)

from rest_framework.routers import DefaultRouter

from .views import ItemsViewSet

app_name = 'items'

router = DefaultRouter()
router.register(r'items', ItemsViewSet, basename='items')

urlpatterns = [
   path('', include(router.urls)),
   path('item/update_status/<int:pk>/',
         ItemsViewSet.as_view({'patch': 'update_status'}), name='status update'),
   path('items/<int:pk>/category/', ItemsViewSet.as_view({'get': 'retrieve'}), name='items-categories'),
   
]

