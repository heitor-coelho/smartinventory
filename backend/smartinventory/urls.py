from django.contrib import admin
from django.urls import path, include
from apps.users.views import UserCreateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # login
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # refresh token


    path('api/inventory/', include('apps.inventory.urls')),
    path('api/register/', UserCreateView.as_view(), name='user-register'),
]
