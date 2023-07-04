from app.models import Characters
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from ..serializers import CharacterSerializer

class CharacterListCreateView(generics.ListCreateAPIView):
    queryset = Characters.objects.all()
    serializer_class = CharacterSerializer
    filterset_fields = ['element', 'star']
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['$name']

    def perform_create(self, serializer):
        return super().perform_create(serializer)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(response.data)


class CharacterDetailView(generics.RetrieveAPIView):
    queryset = Characters.objects.all()
    serializer_class = CharacterSerializer
    lookup_field = 'pk'

class CharacterUpdateView(generics.UpdateAPIView):
    queryset = Characters.objects.all()
    serializer_class = CharacterSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        serializer.save()

class CharacterDeleteView(generics.DestroyAPIView):
    queryset = Characters.objects.all()
    serializer_class = CharacterSerializer
    lookup_field = 'pk'

