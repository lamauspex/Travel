
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from locations.models import Category, Location
from .serializers import (
    CategorySerializer,
    LocationSerializer,
    GeoJSONLocationSerializer
)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class LocationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Location.objects.filter(is_approved=True)
    serializer_class = LocationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description', 'address']

    @action(detail=False, methods=['get'])
    def geojson(self, request):
        """Эндпоинт для получения данных в формате GeoJSON"""
        locations = self.get_queryset()
        serializer = GeoJSONLocationSerializer(locations, many=True)
        return Response({
            'type': 'FeatureCollection',
            'features': serializer.data
        })
