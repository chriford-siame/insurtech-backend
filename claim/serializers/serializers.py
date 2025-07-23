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

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model.
    """

    class Meta:
        model = User
        fields = '__all__'
        
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
    year = MakeYearSerializer(read_only=True)
    class Meta:
        model = Make
        fields = ['id', 'year', 'name']



class ModelSerializer(serializers.ModelSerializer):
    """
    Serializer for model model.
    """
    make = MakeYearSerializer(read_only=True)

    class Meta:
        model = Model
        fields = [
            "id",
            "make",
            "name"
        ]

class QuotationSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    model = ModelSerializer(read_only=True)

    class Meta:
        model = Quotation
        fields = [
            "id",
            "user",
            "registration_number",
            "model",
            "color",
            "engine_capacity",
            "engine_number",
            "chassis_number",
            "vehicle_use",
            "cover_end",
            "has_paid",
            "insured_price",
            "status",
            "quotation",
            "created_at",
        ]
    

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

