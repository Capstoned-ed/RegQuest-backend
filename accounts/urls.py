from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserViewset, StudentInfoViewSet, StaffInfoViewSet, RegisterView, login

router = DefaultRouter()

router.register(r'users', UserViewset)
router.register(r'studentinfo', StudentInfoViewSet)
router.register(r'staffinfo', StaffInfoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('login/', login, name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
