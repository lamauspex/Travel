import os
import django

# Настраиваем Django для pytest
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_map_project.settings')
django.setup()


def pytest_configure():
    """Конфигурация pytest для Django"""
    from django.conf import settings
    if not settings.configured:
        settings.configure(
            DEBUG=True,
            DATABASES={
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': ':memory:',
                }
            },
            INSTALLED_APPS=[
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.admin',
                'rest_framework',
                'locations',
                'api',
            ],
            SECRET_KEY='test-secret-key',
            ROOT_URLCONF='travel_map_project.urls',
            MEDIA_ROOT='/tmp/media_test',
            STATIC_URL='/static/',
        )
