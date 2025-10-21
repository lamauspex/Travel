import factory
from factory.django import DjangoModelFactory
from locations.models import Category, Location


class CategoryFactory(DjangoModelFactory):
    """Фабрика для создания тестовых категорий"""

    class Meta:
        model = Category

    name = factory.Sequence(lambda n: f"Категория {n}")
    description = factory.Faker('sentence')
    icon = "🌳"


class LocationFactory(DjangoModelFactory):
    """Фабрика для создания тестовых локаций"""

    class Meta:
        model = Location

    name = factory.Sequence(lambda n: f"Локация {n}")
    description = factory.Faker('paragraph')
    address = factory.Faker('address')
    latitude = factory.Faker('latitude')
    longitude = factory.Faker('longitude')
    category = factory.SubFactory(CategoryFactory)
    is_approved = True
