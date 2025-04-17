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
    files = ClaimFileSerializer(many=True, read_only=True)

    class Meta:
        model = Claimant
        fields = '__all__'


class ReviewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviewer
        fields = '__all__'

