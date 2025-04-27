from django.contrib import admin
from .models import Carousel, VillageProfile, Destination, DestinationImage, Reservation


class DestinationImageInline(admin.TabularInline):
    model = DestinationImage
    extra = 3


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active')
    list_editable = ('order', 'is_active')


@admin.register(VillageProfile)
class VillageProfileAdmin(admin.ModelAdmin):
    list_display = ('title', 'last_updated')


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'destination_price', 'operational_hour', 'category', 'is_featured', 'created_at')
    list_filter = ('is_featured',)
    search_fields = ('name', 'location')
    inlines = [DestinationImageInline]


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'destination', 'visit_date', 'number_of_visitors', 'need_guide', 'total_price', 'created_at')
    list_filter = ('destination', 'visit_date', 'need_guide')
    search_fields = ('name', 'email', 'phone')
    readonly_fields = ('created_at', 'total_price')
    date_hierarchy = 'visit_date'
    ordering = ('-created_at',) 