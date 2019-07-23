from rest_framework import serializers
from .models import Inventory


# Serializers define the API representation.
class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ("name", "count")
