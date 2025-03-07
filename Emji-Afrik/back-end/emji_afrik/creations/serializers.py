from rest_framework import serializers 
from .models import  Creations

class CreationSerializer(serializers.ModelSerializer):

    class Meta:
        model= Creations
        fields='__all__'

    def validate_prix(self, value):
        if value < 0:
            raise serializers.ValidationError("Le prix d'un service doit être positif.")
        return value