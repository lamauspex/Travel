
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from . import views  
from api.views import CategoryViewSet, LocationViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'locations', LocationViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/locations/geojson/', LocationViewSet.as_view({'get': 'geojson'}), name='locations-geojson'),
    path('api/stats/', views.api_stats, name='api-stats'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)