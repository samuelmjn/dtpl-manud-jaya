# Generated by Django 5.1.7 on 2025-04-15 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_news_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Berita', 'verbose_name_plural': 'Berita'},
        ),
    ]
