from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from django.db.models import Q
from claim.serializers import (
    UserSerializer,
    ClaimantSerializer, 
    ReviewerSerializer
)
from django.contrib.auth.models import User
from claim.models import Claimant, Reviewer

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
    

class ClaimantViewSet(viewsets.ModelViewSet):
    queryset = Claimant.objects.all()
    serializer_class = ClaimantSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        # Fetch by query param: /claims/?username=some_user
        username = self.request.query_params.get('username')
        if username:
            return Claimant.objects.filter(user__username=username)
        return Claimant.objects.none()
    
    @action(detail=False, methods=["get"], url_path="mylist")
    def my_claims(self, request):
        # Optional endpoint: /claims/my-claims/ to fetch current user's claims
        return Response(self.get_serializer(self.get_queryset(), many=True).data)


class ReviewerViewSet(viewsets.ModelViewSet):
    queryset = Reviewer.objects.all()
    serializer_class = ReviewerSerializer
    permission_classes = [permissions.IsAuthenticated]

