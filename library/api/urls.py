from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from django_grpc_framework import services

from .views import UserViewSet, BooksViewSet
# from grpc import library_pb2_grpc
# from grpc.service import BooksService


app_name = 'api'

router = DefaultRouter()

router.register('users', UserViewSet, basename='users')
router.register('books', BooksViewSet, basename='books')

urlpatterns = [
    path('', include(router.urls)),
    # path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    # path('gRPC/', services.as_view(library_pb2_grpc.BooksService)),
]
