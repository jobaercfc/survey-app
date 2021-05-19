from app.serializers import NameMasterSerializer, ResultSerializer
from app.models import NameMaster, Result
from rest_framework import status, viewsets, response

class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

class NameMasterViewSet(viewsets.ModelViewSet):
    queryset = NameMaster.objects.all()
    serializer_class = NameMasterSerializer