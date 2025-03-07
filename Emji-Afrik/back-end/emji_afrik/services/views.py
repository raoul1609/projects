from .models import Services

### IMPORT UTILES POUR IMPLEMENTER LES API
from rest_framework import  viewsets, status
from rest_framework.response import Response

from .serializers import ServiceSerializer


# endpoint pour avoir la liste des services 
# utilisation de viewset pour implementer les API

class ServicesViewSet(viewsets.ModelViewSet):
    '''
        cette classe genere toutes les routes sur le modele service
        avec Viewset, la validation des donnees se fait dans le serialisateur
    '''
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer

    def create(self, request, *args, **kwargs):
        '''
            avec viewset la validation se fait aussi au niveau des vues 
            il est question de modifier les fonctions utilisees, comme create, update, ...
        '''
            # Validation supplémentaire : vérifier l'existance d'un serice avant sa creation

        request_data = request.data

        check_existance_service_before_creating = [service for service in ServicesViewSet.queryset if service.name == request_data['name']]

        if len (check_existance_service_before_creating)==0 :
            # Appeler la méthode create du parent pour continuer le traitement
            return super().create(request, *args, **kwargs)
        else :
            return Response({'error': 'this service already exist.'}, status=status.HTTP_406_NOT_ACCEPTABLE)




    