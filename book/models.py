from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.BigAutoField(
        primary_key=True,
    )

    name = models.CharField(
        max_length=150,
        verbose_name='Book Name'
    )

    cover_image = models.ImageField(
        upload_to='cover_images',
        verbose_name='Cover Image'
    )

    description = models.TextField(
        max_length=500,
        verbose_name='Description'
    )

    download = models.FileField(
        upload_to='downloads'
    )