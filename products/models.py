from django.db import models

class Product(models.Model):
    FARSI_MENU = {
        ("D", "Darad"),
        ("N", "Nadarad"),

    }
    name = models.CharField(max_length=1000, default="lorem ipsum")
    brand = models.CharField(max_length=80)
    image = models.ImageField(upload_to='products/', blank=False, null=False)
    category = models.CharField(max_length=80)
    color = models.CharField(max_length=80)
    guarantee = models.CharField(max_length=100)
    description = models.CharField(max_length=1500)
    price = models.PositiveIntegerField(default=0)
    chip = models.CharField(max_length=100)
    screen_size = models.CharField(max_length=50)
    internal_storage = models.CharField(max_length=50)
    ram_storage = models.CharField(max_length=50)
    camera_quality = models.CharField(max_length=50)
    battery_capacity = models.CharField(max_length=80)
    farsi_menu = models.CharField(max_length=10, choices=FARSI_MENU)

    def __str__(self):
        return self.brand

