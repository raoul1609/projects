from django import forms 
from .models import Programme, MiawTeachers

"""
class MiawForm (forms.Form):
    enseignantsMiaw = [('1',"M Nkollo"),('2',"Dr KUTCHE"), ('3',"Dr DJONTU"), ('4',"M NDOK PIA"), ('5',"M DJOFANG")]
    enseignant = forms.ChoiceField (label="nom de l'enseignant", choices=enseignantsMiaw)

    telephone = forms.IntegerField (label= "numero de l'enseignant", required=True)
    cours = forms.CharField (label="Intitule du cours", required=True)
"""
    # comment afficher le calendrier pour choix de la date ?
    #dateCours = forms.DateField()

class ProgammeForm (forms.ModelForm):
    enseignants = forms.ModelChoiceField (queryset= MiawTeachers.objects.all(), label="Choisir un enseignant")

    class Meta:
        model=Programme
        fields = ['jour', 'cours']
        labels = {'jour': 'La date du cours', 'cours' : 'Intitule du cours'}


class TeacherForm (forms.ModelForm):

    class Meta:
        model= MiawTeachers
        fields= ['nom','telephone']
        labels= {'nom': 'nom enseignant', 'telephone': 'numero de telephone enseignant'}