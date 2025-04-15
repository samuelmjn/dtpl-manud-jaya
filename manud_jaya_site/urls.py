from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from village.views import search_destinations

# Ubah pengaturan administrasi
admin.site.site_header = "Desa Manud Jaya - Admin"
admin.site.site_title = "Portal Admin Desa Manud Jaya"
admin.site.index_title = "Selamat Datang di Portal Admin Desa Manud Jaya"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', search_destinations, name='search_destinations'),
    path('', include('village.urls')),
    path('news/', include('news.urls')),
]

# Add URL patterns for serving media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)