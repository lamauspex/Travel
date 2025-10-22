from django.test import TestCase
from django.urls import reverse

class IndexViewTest(TestCase):
    """Тесты для главной страницы"""
    
    def test_index_view_status_code(self):
        """Тест что главная страница возвращает 200"""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
    
    def test_index_view_template_used(self):
        """Тест что используется правильный шаблон"""
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'index.html')
    
