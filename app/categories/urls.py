# """categories paths"""
# from django.urls import (
#     path,
#     include,
# )

# from rest_framework.routers import DefaultRouter

# from .views import CategoryViewSet


# app_name = 'categories'

# urlpatterns = [

#     path('',
#          CategoryViewSet.as_view({'get': 'list'}), name='get_all_categories'),

#     path('admin/create/',
#          CategoryViewSet.as_view({'post': 'create'}), name='category_create'),

#     path('admin/delete/<int:pk>/',
#          CategoryViewSet.as_view({'delete': 'destroy'}), name='delete_category'),

#     path('admin/update/<int:pk>/',
#          CategoryViewSet.as_view({'put': 'update'}), name='category_update'),

#     path('admin/partial_update/<int:pk>/', CategoryViewSet.as_view(
#         {'patch': 'partial_update'}), name='category_partial_update'),

#     path('admin/update_status/<int:pk>/', CategoryViewSet.as_view(
#         {'patch': 'update_status'}), name='category_status_update'),
# ]
from django.urls import (
   path,
   include,
)

from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet

app_name = 'categories'

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
   path('', include(router.urls)),
   path('categories/update_status/<int:pk>/',
         CategoryViewSet.as_view({'patch': 'update_status'}), name='status update'),
   path('categories/<int:pk>/items/', CategoryViewSet.as_view({'get': 'retrieve'}), name='category-items'),
]

