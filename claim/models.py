from django.db import models
from django.contrib.auth.models import User
# models.py

from django.db import models

class Reviewer(models.Model):
    """
    Represents an insurance claim reviewer.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Claimant(models.Model):
    """
    Represents a person submitting an insurance claim.
    """
    CLAIM_TYPES = [
        ('motor', 'Motor Insurance'),
        ('medical', 'Medical Insurance'),
        ('property', 'Property Insurance'),
        ('life', 'Life Insurance'),
        ('travel', 'Travel Insurance'),
        ('agriculture', 'Agricultural Insurance'),
        ('workmen', 'Workmen’s Compensation'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    incident = models.TextField()
    nrc = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    claim_type = models.CharField(max_length=30, choices=CLAIM_TYPES)
    date_issued = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.claim_type}"


class ClaimFile(models.Model):
    """
    Files attached to a claimant's submission.
    """
    claimant = models.ForeignKey(Claimant, on_delete=models.CASCADE, related_name="files")
    file = models.FileField(upload_to="claim_files/")

    def __str__(self):
        return f"File for {self.claimant}"
