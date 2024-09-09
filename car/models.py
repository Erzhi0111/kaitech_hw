from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    color = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    years = models.IntegerField()
    model = models.CharField(max_length=100)

    def __self__(self):
        return self.name
    