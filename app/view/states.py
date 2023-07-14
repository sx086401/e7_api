from rest_framework import generics, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from django_filters import FilterSet, CharFilter
from app.models.states import States
from app.serializers import StateSerializer


class StatesFilter(FilterSet):
    element = CharFilter(field_name='character__element', lookup_expr='exact')
    star = CharFilter(field_name='character__star', lookup_expr='exact')
    role = CharFilter(field_name='character__role', lookup_expr='exact')

    class Meta:
        model = States
        fields = ['element', 'star', 'role']

class StateListCreateView(generics.ListCreateAPIView):
    queryset = States.objects.all()
    serializer_class = StateSerializer
    filterset_class = StatesFilter
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['$editor', '$character__name']

class StateUpdateView(generics.UpdateAPIView):
    queryset = States.objects.all()
    serializer_class = StateSerializer
    lookup_field = 'pk'

class StateDeleteView(generics.DestroyAPIView):
    queryset = States.objects.all()
    serializer_class = StateSerializer
    lookup_field = 'pk'
