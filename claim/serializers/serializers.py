from rest_framework import serializers
from django.contrib.auth.models import User

from claim.models import Claimant, Reviewer, ClaimFile

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model.
    """

    class Meta:
        model = User
        fields = '__all__'


class ClaimFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClaimFile
        fields = ['id', 'file']


class ClaimantSerializer(serializers.ModelSerializer):
    files = serializers.ListField(
        child=serializers.FileField(),
        write_only=True,
        required=False
    )
    user = UserSerializer(read_only=True)

    class Meta:
        model = Claimant
        fields = [
                'files',
                'user',
                'first_name',
                'middle_name',
                'last_name',
                'incident',
                'nrc',
                'phone_number',
                'claim_type',
                'date_issued',
                'status',
        ]
    
    def create(self, validated_data):
        files = validated_data.pop('files', [])
        claim = Claimant.objects.create(**validated_data)
        for f in files:
            ClaimFile.objects.create(claimant=claim, file=f)
        return claim


class ReviewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviewer
        fields = '__all__'

