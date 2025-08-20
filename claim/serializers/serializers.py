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
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class MakeYearSerializer(serializers.ModelSerializer):
    """
    Serializer for MakeYear model.
    """

    class Meta:
        model = MakeYear
        fields = ['id', 'year']


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
    make = MakeSerializer(read_only=True)

    class Meta:
        model = Model
        fields = '__all__'

class QuotationSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    model_info = serializers.SerializerMethodField()

    class Meta:
        model = Quotation
        fields = [
            "id",
            "user",
            "registration_number",
            "model",
            "model_info",
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
        
    def get_model_info(self, obj):
        model_id = obj.model.id
        model_obj = Model.objects.get(id=model_id)
        response = ModelSerializer(model_obj)
        return response.data

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

