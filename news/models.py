from datetime import datetime

from django.db import models
from django.utils.text import slugify


class News(models.Model):
    title = models.CharField(max_length=200, null=False)
    category = models.CharField(max_length=100, null=False)
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100, null=False)
    content = models.TextField(null=False)
    image = models.ImageField(upload_to='news/')
    slug = models.SlugField(blank=True, unique=True)

    class Meta:
        verbose_name_plural = "news"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str(self.title) + "-" + str(datetime.now()))
        super().save(*args, **kwargs)