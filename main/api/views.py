from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from . import serializers
from main import models

@api_view(['GET'])
def staff_list(request):
    try:
        data = models.Staff.objects.all()
        serializer_data = serializers.StaffSerializerList(data, many=True)
        return Response(serializer_data.data, status=status.HTTP_200_OK)
    except:
        return Response({'success':False}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def attendance_create(request):
    try:
        staff = models.Staff.objects.get(id=request.data['body'])
        is_enter = not models.Attendance.objects.filter(staff=staff).last().is_enter
        models.Attendance.objects.create(
            staff = staff,
            is_enter = is_enter,
        )
        return Response({'success':True}, status=status.HTTP_201_CREATED)
    except:
        return Response({'success':False}, status=status.HTTP_400_BAD_REQUEST)
    
