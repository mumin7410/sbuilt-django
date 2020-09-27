from django.db import models


class image(models.Model):                          #upload image in to Gallery page.
    img = models.ImageField(blank=True, null=True)

# Create your models here.
