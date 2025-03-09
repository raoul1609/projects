from rest_framework import serializers 
from .models import  Creations

class CreationSerializer(serializers.ModelSerializer):

    class Meta:
        model= Creations
        fields='__all__'

    def validate_prix(self, prix):
        if prix < 0:
            raise serializers.ValidationError("Le prix d'un service doit être positif.")
        return prix
    
    # valide l'extension de l'image.
    def validate_image(self, image):
        goods_extensions = ['jpeg', 'png', 'jpg']
        extracted_extension = image.name.split('.')[-1].lower()

        if extracted_extension not in goods_extensions :
            raise serializers.ValidationError('not supported extension for image')
        
        max_length = 5 * 1024 * 1024
        if image.size > max_length :
            raise serializers.ValidationError ("la taille del'image ne doit pas depasser 5 Mo")

        return image

        
        
