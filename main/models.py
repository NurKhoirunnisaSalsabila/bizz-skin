import uuid 
from django.db import models

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    # time = models.DateTimeField(auto_now_add=True)
    skin_type = models.TextField()
    stock = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    # max_digits=3 and decimal_places=2 allows for ratings like 4.75, 5.00, etc.
    
    def __str__(self):
        return self.name