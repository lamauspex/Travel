
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from locations.models import Category, Location


class CategoryAPITest(APITestCase):
    """Тесты для API категорий"""

    def setUp(self):
        """Создаем тестовые данные"""
        self.category1 = Category.objects.create(
            name="Парки",
            description="Парки и скверы",
            icon="🌳"
        )
        self.category2 = Category.objects.create(
            name="Музеи",
            description="Музеи и выставки",
            icon="🏛️"
        )

    def test_category_detail_api(self):
        """Тест получения деталей категории через API"""
        url = reverse('category-detail', args=[self.category1.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Парки")
        self.assertEqual(response.data['icon'], "🌳")


class LocationAPITest(APITestCase):
    """Тесты для API локаций"""

    def setUp(self):
        """Создаем тестовые данные"""
        self.category = Category.objects.create(name="Парки")

        # Создаем одобренные и неодобренные локации
        self.approved_location = Location.objects.create(
            name="Одобренный парк",
            description="Описание",
            latitude=55.7558,
            longitude=37.6173,
            category=self.category,
            is_approved=True
        )

        self.unapproved_location = Location.objects.create(
            name="Неодобренный парк",
            description="Описание",
            latitude=55.7500,
            longitude=37.6200,
            category=self.category,
            is_approved=False
        )

    def test_geojson_api_endpoint(self):
        """Тест GeoJSON эндпоинта"""
        url = reverse('locations-geojson')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['type'], 'FeatureCollection')
        self.assertEqual(len(response.data['features']), 1)

        feature = response.data['features'][0]
        self.assertEqual(feature['type'], 'Feature')
        self.assertEqual(feature['properties']['name'], "Одобренный парк")
        self.assertEqual(feature['geometry']['type'], 'Point')
        self.assertEqual(feature['geometry']
                         ['coordinates'], [37.6173, 55.7558])


class LocationFilterTest(APITestCase):
    """Тесты фильтрации локаций"""

    def setUp(self):
        """Создаем тестовые данные для фильтрации"""
        self.parks_category = Category.objects.create(name="Парки")
        self.museums_category = Category.objects.create(name="Музеи")

        Location.objects.create(
            name="Центральный парк",
            description="Большой парк в центре",
            latitude=55.7558,
            longitude=37.6173,
            category=self.parks_category,
            is_approved=True
        )

        Location.objects.create(
            name="Исторический музей",
            description="Музей истории",
            latitude=55.7539,
            longitude=37.6208,
            category=self.museums_category,
            is_approved=True
        )
