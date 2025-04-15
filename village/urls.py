from django.urls import path
from . import views

app_name = 'village'

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.village_profile, name='village_profile'),
    path('destination/<int:destination_id>/', views.destination_detail, name='destination_detail'),
    path('destinations/', views.destination_list, name='destination_list'),
    path('api/search/', views.search_destinations_api, name='search_destinations_api'),
    path('destination/<int:destination_id>/reservation/', views.reservation_create, name='reservation_create'),
    path('reservation/<int:reservation_id>/success/', views.reservation_success, name='reservation_success'),
]