from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from django.db.models import Q
from claim.serializers import (
    UserSerializer,
    ClaimantSerializer, 
    ReviewerSerializer,
    ClaimFileSerializer,
)
from django.contrib.auth.models import User
from claim.models import Claimant, Reviewer, ClaimFile

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
    
    @action(detail=False, methods=["get"], url_path="list")
    def all_claims(self, request):
        queryset = Claimant.objects.filter(user__username=request.user.username)
        serializer = ClaimantSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
class ReviewerViewSet(viewsets.ModelViewSet):
    queryset = Reviewer.objects.all()
    serializer_class = ReviewerSerializer
    permission_classes = [permissions.IsAuthenticated]

class ClaimFileViewSet(viewsets.ModelViewSet):
    queryset = ClaimFile.objects.all()
    serializer_class = ClaimFile
    permission_classes = [permissions.IsAuthenticated]

