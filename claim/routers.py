from rest_framework.routers import DefaultRouter

from claim.viewsets import (
    UserViewSet    ,
    ClaimViewSet,
    ReviewerViewSet,
    ClaimFileViewSet,
    MakeYearViewSet,
    MakeViewSet,
    ModelViewSet,
    QuotationViewSet,
)

router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'claims', ClaimViewSet, basename='claims')
router.register(r'reviewers', ReviewerViewSet, basename='reviewer')
router.register(r'claimfiles', ClaimFileViewSet, basename='claimfiles')
router.register(r'make', MakeViewSet, basename='make')
router.register(r'make-year', MakeYearViewSet, basename='make-year')
router.register(r'make-model', ModelViewSet, basename='make-model')
router.register(r'quotation', QuotationViewSet, basename='quotation')

app_name = 'claim'
urlpatterns = router.urls
