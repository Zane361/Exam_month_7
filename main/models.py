from django.db import models
from django.contrib.auth.models import User


class Staff(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    salary = models.IntegerField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Attendance(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    date_time = models.DateTimeField(auto_now_add=True)
    is_enter = models.BooleanField()

    def __str__(self):
        return self.staff.first_name


