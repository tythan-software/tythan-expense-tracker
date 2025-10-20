from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'You need to provide username and password credentials'},
                        status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(request, username=username, password=password)

    if user:
        login(request, user)
        refresh = RefreshToken.for_user(user)
        return Response({'refresh': str(refresh), 'access': str(refresh.access_token)},
                        status=status.HTTP_201_CREATED)
    else:
        return Response({'error': 'Invalid credentials'},
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def create_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    print(username, password)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'},
                        status=status.HTTP_400_BAD_REQUEST)
    else:
        user = User.objects.create_user(username, password)
        if user:
            return Response({'detail': 'User registered successfully!'})
        else:
            return Response({'error': 'There was an issue with registering the user'})


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def logout_view(request):
    try:
        refresh_token = request.data.get("refresh_token")
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({"message": "Logout successful."},
                        status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
        return Response({"message": "An error occurred during logout."},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
@authentication_classes([])
@permission_classes([])
def delete_user(request, username):
    user_exists = User.objects.filter(username=username).exists()
    if user_exists:
        user = User.objects.filter(username=username).first()
        user.delete()

        return Response({'detail': 'User deleted successfully'},
                        status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({'detail': 'User not found'},
                        status=status.HTTP_404_NOT_FOUND)
