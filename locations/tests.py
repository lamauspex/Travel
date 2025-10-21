from django.test import TestCase
import os
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import Category, Location


class CategoryModelTest(TestCase):
    """Тесты для модели Category"""

    def setUp(self):
        """Создаем тестовые данные"""
        self.category = Category.objects.create(
            name="Тестовая категория",
            description="Описание тестовой категории",
            icon="🏛️"
        )

    def test_category_creation(self):
        """Тест создания категории"""
        self.assertEqual(self.category.name, "Тестовая категория")
        self.assertEqual(self.category.description,
                         "Описание тестовой категории")
        self.assertEqual(self.category.icon, "🏛️")
        self.assertEqual(str(self.category), "Тестовая категория")

    def test_category_str_representation(self):
        """Тест строкового представления категории"""
        self.assertEqual(str(self.category), "Тестовая категория")


class LocationModelTest(TestCase):
    """Тесты для модели Location"""

    def setUp(self):
        """Создаем тестовые данные"""
        self.category = Category.objects.create(
            name="Парки",
            description="Парки и скверы"
        )

        # Создаем временное изображение для теста
        self.test_image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'fake image content',
            content_type='image/jpeg'
        )

        self.location = Location.objects.create(
            name="Тестовый парк",
            description="Описание тестового парка",
            address="ул. Тестовая, 1",
            latitude=55.7558,
            longitude=37.6173,
            category=self.category,
            photo=self.test_image,
            is_approved=True
        )

    def tearDown(self):
        """Очищаем временные файлы после тестов"""
        if self.location.photo:
            if os.path.isfile(self.location.photo.path):
                os.remove(self.location.photo.path)

    def test_location_creation(self):
        """Тест создания локации"""
        self.assertEqual(self.location.name, "Тестовый парк")
        self.assertEqual(self.location.latitude, 55.7558)
        self.assertEqual(self.location.longitude, 37.6173)
        self.assertEqual(self.location.category, self.category)
        self.assertTrue(self.location.is_approved)

    def test_location_str_representation(self):
        """Тест строкового представления локации"""
        self.assertEqual(str(self.location), "Тестовый парк")

    def test_location_coordinates_property(self):
        """Тест свойства coordinates"""
        expected_coords = {'lat': 55.7558, 'lng': 37.6173}
        self.assertEqual(self.location.coordinates, expected_coords)

    def test_location_ordering(self):
        """Тест порядка сортировки локаций"""
        # Создаем вторую локацию
        location2 = Location.objects.create(
            name="Вторая локация",
            description="Описание",
            latitude=55.7600,
            longitude=37.6200,
            category=self.category
        )

        locations = list(Location.objects.all())
        # Должны быть отсортированы по убыванию даты создания
        self.assertEqual(locations[0], location2)  # Последняя созданная первой
        self.assertEqual(locations[1], self.location)
