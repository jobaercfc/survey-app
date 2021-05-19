from rest_framework import serializers
from app.models import NameMaster, Result

class NameMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NameMaster
        fields = ['id', 'name']

class ResultSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="voter_name.name", read_only=True)
    class Meta:
        model = Result
        fields = ['id', 'name', 'first_vote', 'second_vote', 'third_vote', 'first_reason', 'second_reason', 'third_reason']