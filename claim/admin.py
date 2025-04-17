from django.contrib import admin
from claim.models import Claimant, Reviewer, ClaimFile

admin.site.register(Claimant)
admin.site.register(Reviewer)
admin.site.register(ClaimFile)

# Register your models here.
