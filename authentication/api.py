from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .serializers import UserSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):

    data = request.data
    username = data.get('username') or None
    email = data.get('email') or None
    password = data.get('password') or None

    if not password or (not username and not email):
        return Response({'detail': 'Provide username/email and password.'}, status=status.HTTP_400_BAD_REQUEST)

    # If email is provided, try to resolve to username
    if email and not username:
        try:
            user_obj = User.objects.get(email__iexact=email)
            username = user_obj.get_username()
        except User.DoesNotExist:
            return Response({'detail': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)

    user = authenticate(request, username=username, password=password)
    if user is None:
        return Response({'detail': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({'user': UserSerializer(user).data, 'token': token.key}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'user': UserSerializer(user).data, 'token': token.key}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    user = request.user
    # Delete token(s) for this user
    Token.objects.filter(user=user).delete()
    return Response({'detail': 'Logged out.'}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def refresh(request):
    user = request.user
    Token.objects.filter(user=user).delete()
    token = Token.objects.create(user=user)
    return Response({'token': token.key}, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def me(request):
    user = request.user
    return Response(UserSerializer(user).data, status=status.HTTP_200_OK)