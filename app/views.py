from app.models import Users
from rest_framework import generics
from rest_framework.response import Response
from .serializers import UserSerializer, UserUpdateSerializer

class UserListView(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

class UserCreateView(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'status': 200,
            'data': response.data
        })

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

