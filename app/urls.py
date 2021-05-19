from app.views import ResultViewSet
from django.urls import path, include
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns


get_results = ResultViewSet.as_view({
    'get': 'get_result',
})

urlpatterns = format_suffix_patterns([
    path('results/', get_results, name='result-list')
])