from django.db import models

class Properties(models.Model):
    name = models.CharField(max_length=50, default="")
    address = models.CharField(max_length=250, default="")
    city = models.CharField(max_length=20, default="")
    state = models.CharField(max_length=20, default="")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    price_per_sqft = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    brokerage = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    bedrooms = models.IntegerField(default=0)
    bathrooms = models.IntegerField(default=0)
    parking = models.CharField(max_length=25, default="")
    balcony = models.IntegerField(default=0)
    added_status = models.CharField(max_length=25, default='just now')
    img1 = models.ImageField(upload_to='media/', default='')
    img2 = models.ImageField(upload_to='media/', default='')
    img3 = models.ImageField(upload_to='media/', default='')
    img4 = models.ImageField(upload_to='media/', default='')
    img5 = models.ImageField(upload_to='media/', default='')
