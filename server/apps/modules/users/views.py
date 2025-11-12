from django.contrib.auth.models import User

from drf_spectacular.utils import extend_schema

from rest_framework import status
from rest_framework.response import Response

from apps.core.viewsets import AuthViewSet
from apps.modules.users.serializers import UserSerializer

@extend_schema(tags=['Users'])
class UserViewSet(AuthViewSet):
    """
    API for managing users.
    """
    serializer_class = UserSerializer
    def create(self, request):
        if User.objects.filter(username=request.data.get('username')).exists():
            return Response({'error': 'Username already exists'},
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = UserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            User.objects.create_user(request.data)
            return Response(status=status.HTTP_201_CREATED)

    def destroy(self, request, pk):
        user_exists = User.objects.filter(id=pk).exists()
        if user_exists:
            user = User.objects.filter(id=pk).first()
            user.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
