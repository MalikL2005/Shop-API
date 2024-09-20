from rest_framework import serializers 
from .models import Shop_item


class Shop_item_serializer(serializers.ModelSerializer):
    class Meta:
        model = Shop_item
        fields = '__all__'
