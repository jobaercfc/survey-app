from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path(r'admin/', admin.site.urls),
    path('', include('app.urls'))
]
