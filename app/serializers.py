from rest_framework import serializers
from app.models import NameMaster, Result

class NameMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NameMaster
        fields = ['id', 'name']

class ResultSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="voter_name.name", read_only=True)
    first_vote_name = serializers.CharField(source="first_vote.name", read_only=True)
    second_vote_name = serializers.CharField(source="second_vote.name", read_only=True)
    third_vote_name = serializers.CharField(source="third_vote.name", read_only=True)
    class Meta:
        model = Result
        fields = ['id', 'name', 'voter_name', 'first_vote_name', 'second_vote_name', 'third_vote_name','first_vote', 'second_vote', 'third_vote', 'first_reason', 'second_reason', 'third_reason']
        extra_kwargs = {
            'first_vote': {'write_only': True},
            'second_vote': {'write_only': True},
            'third_vote': {'write_only': True}
        }