from drf_spectacular.utils import extend_schema

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response


@extend_schema(tags=['Authentication'])
class TokenObtainPairWrapper(TokenObtainPairView):
    permission_classes = [AllowAny]


@extend_schema(tags=['Authentication'])
class TokenRefreshWrapper(TokenRefreshView):
    permission_classes = [AllowAny]


@extend_schema(tags=['Authentication'])
class AuthenticationViews(ViewSet):
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'])
    def logout_view(self, request):
        refresh_token = request.data.get("refresh_token")
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response(status=status.HTTP_205_RESET_CONTENT)