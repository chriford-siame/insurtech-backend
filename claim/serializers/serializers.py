from rest_framework import serializers
from django.contrib.auth.models import User

# from claim.models import (
    
# )

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model.
    """

    class Meta:
        model = User
        fields = '__all__'
