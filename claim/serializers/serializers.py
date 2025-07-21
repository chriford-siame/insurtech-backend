from rest_framework import serializers
from django.contrib.auth.models import User

from claim.models import (
    Claim, 
    Reviewer, 
    ClaimFile,
    MakeYear,
    Make,
    Model,
    Quotation,
)

class MakeYearSerializer(serializers.ModelSerializer):
    """
    Serializer for MakeYear model.
    """

    class Meta:
        model = MakeYear
        fields = '__all__'


class MakeSerializer(serializers.ModelSerializer):
    """
    Serializer for Make model.
    """

    class Meta:
        model = Make
        fields = '__all__'


class ModelSerializer(serializers.ModelSerializer):
    """
    Serializer for Model model.
    """

    class Meta:
        model = Model
        fields = '__all__'


class QuotationSerializer(serializers.ModelSerializer):
    """
    Serializer for Quotation model.
    """

    class Meta:
        model = Quotation
        fields = '__all__'

# ...
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


class ClaimSerializer(serializers.ModelSerializer):
    files = serializers.ListField(
        child=serializers.FileField(),
        write_only=True,
        required=False
    )
    user = UserSerializer(read_only=True)

    class Meta:
        model = Claim
        fields = [
                'id',
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
                'comment',
        ]
    
    def create(self, validated_data):
        files = validated_data.pop('files', [])
        claim = Claim.objects.create(**validated_data)
        for f in files:
            ClaimFile.objects.create(claim=claim, file=f)
        return claim


class ReviewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviewer
        fields = '__all__'

