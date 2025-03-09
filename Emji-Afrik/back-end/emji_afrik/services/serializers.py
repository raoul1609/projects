from rest_framework import serializers 
from .models import Services

class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model= Services
        fields='__all__'

    def validate_price(self, value):
        '''
            cette validation personnalise permet de valider un champ precis, ici le champ price
        '''
        if value < 0:
            raise serializers.ValidationError("Le prix d'un service doit être positif.")
        return value


