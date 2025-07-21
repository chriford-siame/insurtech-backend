from django.contrib import admin
from claim.models import (
    Claimant, 
    Reviewer, 
    ClaimFile,
    MakeYear,
    Make,
    Model,
    Quotation,
)

admin.site.register(Claimant)
admin.site.register(Reviewer)
admin.site.register(ClaimFile)
admin.site.register(MakeYear)
admin.site.register(Make)
admin.site.register(Model)
admin.site.register(Quotation)

# Register your models here.
