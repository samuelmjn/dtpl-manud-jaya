from django.contrib import admin
from .models import Carousel, VillageProfile, Destination, DestinationImage


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
    list_display = ('name', 'location', 'is_featured', 'created_at')
    list_filter = ('is_featured',)
    search_fields = ('name', 'location')
    inlines = [DestinationImageInline] 