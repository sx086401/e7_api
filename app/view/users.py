from app.models import Users
from rest_framework import generics, permissions, authentication
from rest_framework.views import APIView
from django.contrib.auth import login
from rest_framework.response import Response
from ..serializers import UserSerializer, UserUpdateSerializer

class UserListCreateView(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = [authentication.SessionAuthentication]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        return super().perform_create(serializer)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(response.data)


class UserDetailView(generics.RetrieveAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

class UserUpdateView(generics.UpdateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserUpdateSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        serializer.save()

class UserDeleteView(generics.DestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = Users.objects.get(username=username, password=password)

        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful', 'username': user.username})
        else:
            return Response({'message': 'Invalid credentials'}, status=401)
