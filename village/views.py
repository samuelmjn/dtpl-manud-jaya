from django.shortcuts import render, get_object_or_404
from .models import Carousel, VillageProfile, Destination


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