

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from .serializers import UserSerializer

@api_view(['POST'])  # Change the decorator to accept POST requests
def login_view(request):
    username = request.data.post('username')
    password = request.data.post('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return Response({'message': 'Login successful.'})
    else:
        return Response({'message': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def signup_view(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'User created successfully.'})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUTs'])
def forget_password_view(request):
    return Response({'message': 'Password reset instructions sent.'})

@api_view(['POST'])
def logout_view(request):
    logout(request)
    return Response({'message': 'Logout successful.'})
