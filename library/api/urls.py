from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, BooksViewSet


app_name = 'api'

router = DefaultRouter()

router.register('users', UserViewSet, basename='users')
router.register('books', BooksViewSet, basename='books')

urlpatterns = [
    path('', include(router.urls)),
    # path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
