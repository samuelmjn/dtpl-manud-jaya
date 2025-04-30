from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Carousel, VillageProfile, Destination, Reservation
from django.db.models import Q
from news.models import News
from django.contrib import messages
from .forms import ReservationForm
from django.db.models import Avg, Count

def home(request):
    carousels = News.objects.all()
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


#def destination_detail(request, destination_id):
#    destination = get_object_or_404(Destination, id=destination_id)
#    destinations = Destination.objects.exclude(id=destination_id)[:3]
#    
#    context = {
#        'destination': destination,
#        'destinations': destinations,
#    }
#    
#    return render(request, 'village/destination_detail.html', context)

def destination_detail(request, destination_id):
    # Get destination with rating and visitor_count annotations
    destination = Destination.objects.annotate(
        rating=Avg('review__rating'),
        visitor_count=Count('review')
    ).get(id=destination_id)

    # Other destinations (e.g. for "related" or "you may also like")
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


def reservation_create(request, destination_id):
    destination = get_object_or_404(Destination, id=destination_id)
    
    if request.method == 'POST':
        form = ReservationForm(request.POST, destination=destination)
        if form.is_valid():
            reservation = form.save()
            messages.success(request, 'Reservasi Anda berhasil dibuat. Terima kasih!')
            return redirect('village:reservation_success', reservation_id=reservation.id)
    else:
        form = ReservationForm(destination=destination)
    
    context = {
        'form': form,
        'destination': destination,
    }
    return render(request, 'village/reservation_form.html', context)


def reservation_success(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    
    context = {
        'reservation': reservation,
    }
    return render(request, 'village/reservation_success.html', context)