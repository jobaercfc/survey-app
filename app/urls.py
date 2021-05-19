from app.views import ResultViewSet, NameMasterViewSet
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'results', ResultViewSet)
router.register(r'namemaster', NameMasterViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]