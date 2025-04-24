from django.contrib import admin
from review.models import Review


# Register your models here.
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('destination', 'rating', 'comment', 'is_used', 'expired_at')
    list_filter = ('destination', 'rating', 'is_used', 'expired_at')

    readonly_fields = ('token', 'rating', 'comment', 'is_used', 'expired_at')