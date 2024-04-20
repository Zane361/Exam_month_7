from rest_framework import serializers
from main import models


class StaffSerializerList(serializers.ModelSerializer):
    class Meta:
        model = models.Staff
        fields = '__all__'


class AttendanceSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = models.Attendance
        fields = '__all__'


