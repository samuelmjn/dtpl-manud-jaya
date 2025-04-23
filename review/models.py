from datetime import datetime, timedelta
from django.db import models
from manud_jaya_site.settings import BASE_URL
from uuid import uuid4


class Review(models.Model):
    token = models.CharField(max_length=255, unique=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    comment = models.TextField(blank=True)
    is_used = models.BooleanField(default=False)
    expired_at = models.DateTimeField(null=True, blank=True)
    destination = models.ForeignKey('village.Destination', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Ulasan"
        verbose_name_plural = "Ulasan"

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = uuid4()
            self.expired_at = datetime.now() + timedelta(days=1)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return BASE_URL + '/review/' + str(self.token)

    def __str__(self):
        return self.get_absolute_url()