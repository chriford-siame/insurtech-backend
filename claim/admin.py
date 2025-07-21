from django.contrib import admin
from claim.models import (
    Claim, 
    Reviewer, 
    ClaimFile,
    MakeYear,
    Make,
    Model,
    Quotation,
)

admin.site.register(Claim)
admin.site.register(Reviewer)
admin.site.register(ClaimFile)
admin.site.register(MakeYear)
admin.site.register(Make)
admin.site.register(Model)
admin.site.register(Quotation)

# Register your models here.
