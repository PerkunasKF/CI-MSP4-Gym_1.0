from django.db import models

# Create your models here.


class Plan(models.Model):
    """ Dummy Tag """
    name = models.CharField(max_length=254)
    line1 = models.CharField(max_length=254, null=True, blank=True)
    line2 = models.CharField(max_length=254, null=True, blank=True)
    line3 = models.CharField(max_length=254, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    unique = models.BooleanField(default=False, null=False, blank=True)

    def __str__(self):
        return self.name