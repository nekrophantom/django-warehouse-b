from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.models import categoryWarehouse
from .serializers import categoryWarehouseSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/category-warehouse',
        # 'GET /api/rooms/:id',

    ]

    return Response(routes)

@api_view(['GET'])
def getCategoryWarehouse(request):
    categoryWarehouse = categoryWarehouse.objects.all()
    serializer = categoryWarehouseSerializer(categoryWarehouse)
    return Response(serializer.data)

# @api_view(['GET'])
# def getRoom(request, pk):
#     room = Room.objects.get(id=pk)
#     serializer = RoomSerializer(room, many=False)
#     return Response(serializer.data)