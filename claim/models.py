from django.db import models
from django.contrib.auth.models import User

from django.db import models

class MakeYear(models.Model):
    """Model for storing vehicle make years"""
    year = models.CharField(max_length=4)

    def __str__(self):
        return f"{self.year}"


class Make(models.Model):
    """Model for storing vehicle makes"""
    year = models.ForeignKey("MakeYear", on_delete=models.CASCADE, related_name="make_year")
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Model(models.Model):
    """Model for storing vehicle make models"""
    make = models.ForeignKey("Make", on_delete=models.CASCADE, related_name="make")
    name = models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.name}"


class Quotation(models.Model):
    VEHICLE_USE_CHOICES = [
        ('commercial', 'Commercial'),
        ('private', 'Private'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="client")
    registration_number = models.CharField(max_length=10)
    model = models.ForeignKey("Model", on_delete=models.PROTECT, related_name="model")
    color = models.CharField(max_length=10)
    engine_capacity = models.CharField(max_length=100)
    engine_number = models.CharField(max_length=100)
    chassis_number = models.CharField(max_length=100)
    vehicle_use = models.CharField(max_length=100, choices=VEHICLE_USE_CHOICES, blank=True, null=True) 
    cover_end = models.DateField(auto_now=False, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    has_paid = models.BooleanField(default=False)
    insured_price = models.DecimalField(decimal_places=2, max_digits=1000, null=True, blank=True)
    quotation = models.FileField(upload_to="quotation_files/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=True)

    def __str__(self):
        return f"{self.registration_number}"


class Reviewer(models.Model):
    """
    Represents an insurance claim reviewer.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Claim(models.Model):
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
        ('other', 'Other'),
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
    date_issued = models.DateField(auto_now=True, blank=True, null=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.claim_type}"


class ClaimFile(models.Model):
    """
    stores files for a claim.
    """
    claim = models.ForeignKey(Claim, on_delete=models.CASCADE, related_name="files")
    file = models.FileField(upload_to="claim_files/")

    def __str__(self):
        return f"File for {self.claim}"
