from django.shortcuts import render
from django.http import JsonResponse
from locations.models import Category, Location

def index(request):
    return render(request, 'index.html')

def api_stats(request):
    """API endpoint для статистики проекта"""
    stats = {
        'locations_count': Location.objects.filter(is_approved=True).count(),
        'categories_count': Category.objects.count(),
        'api_version': '1.0'
    }
    return JsonResponse(stats)