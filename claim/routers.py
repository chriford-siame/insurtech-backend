from rest_framework.routers import DefaultRouter

from claim.viewsets import (
    UserViewSet    
)

router = DefaultRouter()
router.register(r'users', UserViewSet)

app_name = 'claim'
urlpatterns = router.urls
