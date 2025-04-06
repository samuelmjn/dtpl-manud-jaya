from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Carousel, VillageProfile, Destination
from django.db.models import Q


def home(request):
    carousels = Carousel.objects.filter(is_active=True)
    destinations = Destination.objects.all()
    featured_destinations = Destination.objects.filter(is_featured=True)[:6]
    
    context = {
        'carousels': carousels,
        'destinations': destinations,
        'featured_destinations': featured_destinations,
    }
    return render(request, 'village/home.html', context)


def village_profile(request):
    # Get all profile sections or create a default one if none exists
    profiles = VillageProfile.objects.all()
    
    context = {
        'profiles': profiles,
    }
    return render(request, 'village/profile.html', context)


def destination_detail(request, destination_id):
    destination = get_object_or_404(Destination, id=destination_id)
    destinations = Destination.objects.exclude(id=destination_id)[:3]
    
    context = {
        'destination': destination,
        'destinations': destinations,
    }
    return render(request, 'village/destination_detail.html', context)


def destination_list(request):
    destinations = Destination.objects.all()
    
    context = {
        'destinations': destinations,
        'title': 'Semua Destinasi'
    }
    return render(request, 'village/destination_list.html', context)


def search_destinations(request):
    query = request.GET.get('query', '')  # retrieve search term from ?query=
    results = []

    if query:
        results = Destination.objects.filter(
            Q(name__icontains=query) |
            Q(detailed_description__icontains=query) |
            Q(location__icontains=query)
        )
        
    context = {
        'query': query,
        'results': results
    }
    return render(request, 'search_results.html', context)


def search_destinations_api(request):
    query = request.GET.get('query', '')
    destinations = Destination.objects.filter(name__icontains=query) if query else Destination.objects.all()
    data = [
        {
            'name': destination.name,
            'short_description': destination.short_description,
            'main_image_url': destination.main_image.url,
            'url': destination.get_absolute_url(),
        }
        for destination in destinations
    ]
    return JsonResponse({'destinations': data})