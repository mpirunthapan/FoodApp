from django.db import models

class Food(models.Model):
    item_name = models.CharField(max_length=100)
    item_desc = models.CharField(max_length=600)
    item_price = models.DecimalField(max_digits=6, decimal_places=2)
    item_image = models.URLField()

    def __str__(self):
        return self.item_name
    
