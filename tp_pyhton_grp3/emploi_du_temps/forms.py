from django import forms 
from .models import Programme, MiawTeachers

import phonenumbers

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
        widgets = {
            'jour': forms.TextInput(attrs={'placeholder': 'ex : 2025-01-29'}),
            'cours': forms.EmailInput(attrs={'placeholder': 'ex : Programmation Python'}),
        }
        

    # validation personnalise du champ cours 
    def clean_cours (self):
        standarVerifiedCours = self.cleaned_data['cours']
        pass 


#creation du formulaire pour enregisrement d'un enseignant 
class TeacherForm (forms.ModelForm):

    class Meta:
        model= MiawTeachers
        fields= ['nom','telephone']
        labels= {'nom': 'nom enseignant', 'telephone': 'numero de telephone enseignant'}
        widgets = {
            'nom': forms.TextInput(attrs={'placeholder': 'ex : Votre nom'}),
            'telephone': forms.EmailInput(attrs={'placeholder': 'ex : 673314822'}),
        }


    # validation personnalise du numero de telephone using phonenumbers
    def clean_telephone(self):
        firstVerifiedPhone = self.cleaned_data['telephone']
        cmRegion = "CM"
        numberWithCode = "+237"+ str(firstVerifiedPhone)

        try :
            buildPhoneNumberObject = phonenumbers.parse(numberWithCode, cmRegion)

            if phonenumbers.is_valid_number_for_region (buildPhoneNumberObject, cmRegion):
                 return numberWithCode
            
        except phonenumbers.NumberParseException : 
            raise ("le numero de telephone doit contenir que des chiffres")
        
