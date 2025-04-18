from rest_framework.routers import DefaultRouter

from claim.viewsets import (
    UserViewSet    ,
    ClaimantViewSet,
    ReviewerViewSet,
    ClaimFileViewSet,
)

router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'claims', ClaimantViewSet, basename='claims')
router.register(r'reviewers', ReviewerViewSet, basename='reviewer')
router.register(r'claimfile', ClaimFileViewSet, basename='claimfile')

app_name = 'claim'
urlpatterns = router.urls
