from rest_framework.decorators import api_view # type: ignore
from rest_framework.response import Response # type: ignore
from base.models import Rooms
from .serializers import RoomSerializer


@api_view(['GET'])
def getRoutes(requests):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id',
        ]
    return Response(routes)


@api_view(['GET'])
def getRooms(requests):
    rooms = Rooms.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def getRoom(requests,pk):
    room = Rooms.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)