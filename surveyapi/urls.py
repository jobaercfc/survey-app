from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from app import urls




# The API URLs are now determined automatically by the router.
urlpatterns = [
    path(r'', include(urls), name='result'),
    path(r'admin/', admin.site.urls),
]
