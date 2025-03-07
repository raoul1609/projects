from .models import Creations

### IMPORT UTILES POUR IMPLEMENTER LES API
from rest_framework import  viewsets, status
from rest_framework.response import Response

from .serializers import CreationSerializer
# Create your views here.

class CreationViewset(viewsets.ModelViewSet):
    """
        viewset du modele Creation
    """
    queryset = Creations.objects.all()
    serializer_class = CreationSerializer

    def create(self, request, *args, **kwargs):

        # Validation supplémentaire : vérifier l'existance d'un serice avant sa creation
        request_data = request.data

        check_existance_service_before_creating = [service for service in CreationViewset.queryset if service.name == request_data['name']]

        if len (check_existance_service_before_creating)==0 :
            # Appeler la méthode create du parent pour continuer le traitement
            return super().create(request, *args, **kwargs)
        else :
            return Response({'error': 'this creation already exist.'}, status=status.HTTP_406_NOT_ACCEPTABLE)