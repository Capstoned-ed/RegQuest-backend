from rest_framework.routers import DefaultRouter
from .views import UserViewset, StudentInfoViewSet, StaffInfoViewSet

router = DefaultRouter()

router.register(r'users', UserViewset)
router.register(r'studentinfo', StudentInfoViewSet)
router.register(r'staffinfo', StaffInfoViewSet)

urlpatterns = router.urls
