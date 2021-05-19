from app.serializers import NameMasterSerializer, ResultSerializer
from app.models import NameMaster, Result
from rest_framework import status, viewsets, response

class ResultViewSet(viewsets.ModelViewSet):
    def get_result(request, format=None):
        queryset = Result.objects.all()
        serializer_class = ResultSerializer(queryset, many=True)
        return response.Response({'results': serializer_class.data}, status=status.HTTP_200_OK)