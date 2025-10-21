from rest_framework import serializers
from locations.models import Category, Location


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'icon']


class LocationSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Location
        fields = [
            'id', 'name', 'description', 'address',
            'latitude', 'longitude', 'category', 'photo',
            'is_approved', 'created_at'
        ]


class GeoJSONLocationSerializer(serializers.ModelSerializer):
    """Сериализатор для GeoJSON формата"""
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Location
        fields = ['id', 'name', 'description', 'address',
                  'latitude', 'longitude', 'category']

    def to_representation(self, instance):
        """Преобразуем в GeoJSON формат"""
        data = super().to_representation(instance)
        return {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [data['longitude'], data['latitude']]
            },
            'properties': {
                'id': data['id'],
                'name': data['name'],
                'description': data['description'],
                'address': data['address'],
                'category': data['category']
            }
        }
