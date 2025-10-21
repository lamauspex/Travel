
from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    """Категория локации (парк, музей, кафе и т.д.)"""
    name = models.CharField(max_length=100, verbose_name=_('Название'))
    description = models.TextField(verbose_name=_('Описание'), blank=True)
    icon = models.CharField(
        max_length=50, verbose_name=_('Иконка'), blank=True)

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')

    def __str__(self):
        return self.name


class Location(models.Model):
    """Модель локации на карте"""
    name = models.CharField(max_length=255, verbose_name=_('Название'))
    description = models.TextField(verbose_name=_('Описание'))
    address = models.CharField(
        max_length=255, verbose_name=_('Адрес'), blank=True)

    # Геоданные
    latitude = models.FloatField(verbose_name=_('Широта'))
    longitude = models.FloatField(verbose_name=_('Долгота'))

    # Связи
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_('Категория')
    )

    # Медиа
    photo = models.ImageField(
        upload_to='locations/photos/',
        verbose_name=_('Фотография'),
        blank=True,
        null=True
    )

    # Мета-данные
    is_approved = models.BooleanField(
        default=False, verbose_name=_('Одобрено'))
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Дата создания'))
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=_('Дата обновления'))

    class Meta:
        verbose_name = _('Локация')
        verbose_name_plural = _('Локации')
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    @property
    def coordinates(self):
        """Возвращает координаты в формате для карты"""
        return {
            'lat': self.latitude,
            'lng': self.longitude
        }
