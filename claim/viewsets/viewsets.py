from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from django.db.models import Q
from claim.serializers import (
    UserSerializer,
)
from django.contrib.auth.models import User

class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing product categories.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_object(self):
        lookup_value = self.kwargs.get(self.lookup_field)
        
        # Try ID lookup first
        if lookup_value.isdigit():
            try:
                return User.objects.get(id=lookup_value)
            except User.DoesNotExist:
                raise NotFound("User with this ID does not exist.")
        
        # Fallback to username lookup
        try:
            return User.objects.get(username=lookup_value)
        except User.DoesNotExist:
            raise NotFound("User with this username does not exist.")

    lookup_field = 'lookup'  # Custom URL parameter
    