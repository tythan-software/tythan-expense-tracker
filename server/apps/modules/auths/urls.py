from django.urls import path
from apps.modules.auths.views import TokenObtainPairWrapper, TokenRefreshWrapper, AuthenticationViews

urlpatterns = [
    path('token/', TokenObtainPairWrapper.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshWrapper.as_view(), name='token_refresh'),
    path('logout/', AuthenticationViews.as_view({'post': 'logout_view'}), name='logout'),
]
