from rest_framework import serializers
from .models import MiawTeachers

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model= MiawTeachers
        fields='__all__'