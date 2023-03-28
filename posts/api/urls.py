from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewsets

router = DefaultRouter()
router.register(f'posts', PostViewsets, basename='post')

urlpatterns = [
    path('', include(router.urls)),
    
]