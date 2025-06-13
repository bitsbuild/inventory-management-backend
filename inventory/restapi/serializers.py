from rest_framework import serializers
from restapi.models import Item
class ItemSerializer(serializers.Serializer):
    item_id = serializers.UUIDField(read_only=True)
    item_name = serializers.CharField()
    item_description = serializers.CharField()
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
    item_category = serializers.CharField(max_length=30, choices=CATEGORY_CHOICES)
    item_quantity = serializers.IntegerField()
    item_price = serializers.IntegerField()
    def create(self,validated_data):
        return Item.objects.create(**validated_data)
    def update(self,instance,validated_data):
        instance.item_name = validated_data.get('item_name',instance.item_name)
        instance.item_description = validated_data.get('item_description',instance.item_description)
        instance.item_category = validated_data.get('item_category',instance.item_category)
        instance.item_quantity = validated_data.get('item_quantity',instance.item_quantity)
        instance.item_price = validated_data.get('item_price',instance.item_price)
        instance.save()
        return instance