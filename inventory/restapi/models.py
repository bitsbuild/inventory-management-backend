from django.db import models
import uuid

class Item(models.Model):
    item_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item_name = models.CharField(max_length=70)
    item_description = models.CharField(max_length=350)
    CATEGORY_CHOICES = [
        ('clothing', 'Clothing'),
        ('electronics', 'Electronics'),
        ('home_appliances', 'Home Appliances'),
        ('furniture', 'Furniture'),
        ('books', 'Books'),
        ('toys', 'Toys'),
        ('beauty', 'Beauty & Personal Care'),
        ('sports', 'Sports & Outdoors'),
        ('groceries', 'Groceries'),
        ('footwear', 'Footwear'),
        ('stationery', 'Stationery'),
        ('automotive', 'Automotive'),
        ('jewelry', 'Jewelry'),
        ('pet_supplies', 'Pet Supplies'),
        ('music', 'Musical Instruments'),
        ('gaming', 'Gaming'),
        ('mobile_accessories', 'Mobile Accessories'),
        ('luggage', 'Luggage & Travel'),
        ('health', 'Health & Wellness'),
        ('baby_products', 'Baby Products'),
    ]
    item_category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    item_quantity = models.IntegerField()
    item_prices = models.IntegerField()
    def __str__(self):
        return self.item_name
