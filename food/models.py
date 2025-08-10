from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Food(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='food_items')
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=100)
    item_desc = models.CharField(max_length=600)
    item_price = models.DecimalField(max_digits=6, decimal_places=2)
    item_image = models.URLField(default='https://cdn.dribbble.com/userupload/22570626/file/original-379b4978ee41eeb352e0ddacbaa6df96.jpg?resize=752x564&vertical=center')

    def __str__(self):
        return self.item_name
    
    def get_absolute_url(self):
        return reverse('item_list', kwargs={'pk': self.pk})
