from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from .models import CustomUser
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status, permissions, generics
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .serializers import UserRegistrationSerializer, UserLoginSerializer, SimpleUserSerializer

User = get_user_model()

class UserListAPIView(generics.ListAPIView):
    queryset = CustomUser.objects.all()  # <-- fetch all users
    serializer_class = SimpleUserSerializer
    permission_classes = [permissions.AllowAny]  # or IsAuthenticate

class RegisterGenericView(generics.GenericAPIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        """Follow user with id=user_id"""
        target = get_object_or_404(User, id=user_id)
        if target == request.user:
            return Response({'detail': "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.add(target)
        return Response({'detail': f'You are now following {target.username}'}, status=status.HTTP_200_OK)

class UnfollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        """Unfollow user with id=user_id"""
        target = get_object_or_404(User, id=user_id)
        if target == request.user:
            return Response({'detail': "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.remove(target)
        return Response({'detail': f'You have unfollowed {target.username}'}, status=status.HTTP_200_OK)

class FollowersListView(generics.ListAPIView):
    """
    List followers of a user: GET /api/accounts/{user_id}/followers/
    """
    serializer_class = SimpleUserSerializer
    permission_classes = [permissions.AllowAny]  # or IsAuthenticated if you prefer

    def get_queryset(self):
        user = get_object_or_404(User, id=self.kwargs['user_id'])
        return user.followers.all()

class FollowingListView(generics.ListAPIView):
    """
    List users that the given user is following: GET /api/accounts/{user_id}/following/
    """
    serializer_class = SimpleUserSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        user = get_object_or_404(User, id=self.kwargs['user_id'])
        return user.following.all()
