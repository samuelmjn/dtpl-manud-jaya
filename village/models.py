from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator
from datetime import date

class Carousel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='carousel/')
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title


class VillageProfile(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='profile/', blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title


class Destination(models.Model):
    name = models.CharField(max_length=200)
    short_description = models.TextField(max_length=500)
    detailed_description = models.TextField()

    destination_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    operational_hour = models.CharField(max_length=100, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)

    main_image = models.ImageField(upload_to='destinations/')
    location = models.CharField(max_length=200)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('village:destination_detail', args=[str(self.id)])


class DestinationImage(models.Model):
    destination = models.ForeignKey(Destination, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='destinations/gallery/')
    caption = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return f"Image for {self.destination.name}"


class Reservation(models.Model):
    GUIDE_CHOICES = (
        (True, 'Ya'),
        (False, 'Tidak'),
    )
    
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='reservations')
    name = models.CharField("Nama Lengkap", max_length=100)
    email = models.EmailField("Email")
    phone = models.CharField("Nomor Telepon", max_length=20)
    visit_date = models.DateField("Tanggal Kunjungan", validators=[MinValueValidator(limit_value=date.today)])
    number_of_visitors = models.PositiveIntegerField("Jumlah Pengunjung", validators=[MinValueValidator(1)])
    need_guide = models.BooleanField("Perlu Pemandu", default=False)
    special_requests = models.TextField("Permintaan Khusus", blank=True)
    total_price = models.DecimalField("Total Biaya", max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Reservasi"
        verbose_name_plural = "Reservasi"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Reservasi oleh {self.name} untuk {self.destination.name}"
    
    def save(self, *args, **kwargs):
        if not self.total_price:
            # Hitung total harga jika belum diisi
            self.total_price = self.calculate_price()
        super().save(*args, **kwargs)
    
    def calculate_price(self):
        # Harga dasar per pengunjung
        base_price = 25000
        # Tambahan untuk pemandu
        guide_price = 100000 if self.need_guide else 0
        
        return (base_price * self.number_of_visitors) + guide_price 