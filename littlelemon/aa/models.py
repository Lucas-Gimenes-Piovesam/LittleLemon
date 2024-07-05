from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

class Booking(models.Model):
    customer_name = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    party_size = models.IntegerField()

    def __str__(self):
        return self.customer_name