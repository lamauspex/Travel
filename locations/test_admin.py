from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from locations.models import Category, Location

User = get_user_model()


class AdminSiteTest(TestCase):
    """Тесты для админ-панели"""

    def setUp(self):
        """Создаем тестовые данные и суперпользователя"""
        self.admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@test.com',
            password='password123'
        )
        self.client.force_login(self.admin_user)

        self.category = Category.objects.create(name="Тестовая категория")
        self.location = Location.objects.create(
            name="Тестовая локация",
            description="Описание",
            latitude=55.7558,
            longitude=37.6173,
            category=self.category
        )

    def test_category_admin_list_display(self):
        """Тест что категории отображаются в админке"""
        url = reverse('admin:locations_category_changelist')
        response = self.client.get(url)

        self.assertContains(response, self.category.name)

    def test_location_admin_list_display(self):
        """Тест что локации отображаются в админке"""
        url = reverse('admin:locations_location_changelist')
        response = self.client.get(url)

        self.assertContains(response, self.location.name)
        self.assertContains(response, self.category.name)

    def test_location_admin_change_page(self):
        """Тест страницы редактирования локации в админке"""
        url = reverse('admin:locations_location_change',
                      args=[self.location.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.location.name)
