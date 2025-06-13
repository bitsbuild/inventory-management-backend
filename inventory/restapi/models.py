from django.db import models
import uuid

class Item(models.Model):
    item_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item_name = models.CharField(max_length=70)
    item_description = models.CharField(max_length=350)
    CATEGORY_CHOICES = [
        ('clothing', 'clothing'),
        ('electronics', 'electronics'),
        ('home_appliances', 'home_appliances'),
        ('furniture', 'furniture'),
        ('books', 'books'),
        ('toys', 'toys'),
        ('beauty', 'beauty_personal_care'),
        ('sports', 'sports_outdoors'),
        ('groceries', 'groceries'),
        ('footwear', 'footwear'),
        ('stationery', 'stationery'),
        ('automotive', 'automotive'),
        ('jewelry', 'jewelry'),
        ('pet_supplies', 'pet Supplies'),
        ('music', 'musical_instruments'),
        ('gaming', 'gaming'),
        ('mobile_accessories', 'mobile_accessories'),
        ('luggage', 'luggage_travel'),
        ('health', 'health_wellness'),
        ('baby_products', 'baby_products'),
    ]
    item_category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    item_quantity = models.IntegerField()
    item_prices = models.IntegerField()
    def __str__(self):
        return self.item_name
