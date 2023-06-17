from django.db import models
from inventory_man.models import InventoryItem, Category

class Product(InventoryItem):
    
    class Meta:
        proxy = True
        verbose_name_plural = "Products"
        
    def __str__(self):
        return self.name