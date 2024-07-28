from django.db import models
from ckeditor.fields import RichTextField

class Bungalov(models.Model):
    name = models.CharField(max_length=200, verbose_name='Bungalov Adı')
    description = models.TextField(verbose_name='Açıklama')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Fiyat')
    
    def __str__(self):
        return self.name

class BungalovImage(models.Model):
    bungalov = models.ForeignKey(Bungalov, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='bungalov_images/')
    
    def __str__(self):
        return self.bungalov.name


class Villa(models.Model):
    name = models.CharField(max_length=200, verbose_name='Villa Adı')
    description = RichTextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Fiyat')
    
    def __str__(self):
        return self.name

class VillaImage(models.Model):
    villa = models.ForeignKey(Villa, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='villa_images/')
    
    def __str__(self):
        return self.villa.name

class Kurallar(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title
class Kurallar(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title
