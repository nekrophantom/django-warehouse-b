from rest_framework.serializers import ModelSerializer
from main.models import categoryWarehouse

class categoryWarehouseSerializer(ModelSerializer):
    class Meta:
        model = categoryWarehouse
        fields = '__all__'

