from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
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

class StatePagination(PageNumberPagination):
    page_size = 20

class StateListCreateView(generics.ListCreateAPIView):
    queryset = States.objects.all().order_by('-updated_at')
    serializer_class = StateSerializer
    pagination_class = StatePagination
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

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        instance.current_state.delete()
        instance.expect_state.delete()

        return super().destroy(request, *args, **kwargs)
