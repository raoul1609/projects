from django.db import models
from datetime import date

# Create your models here.

class Programme (models.Model):
    jour = models.DateField (primary_key= True, default=date.today, null=False, help_text="Format de la date : AAAA-MM-JJ", verbose_name= "jour de la semaine")
    cours = models.CharField (default="", null= False, help_text= "Intitule du cours dans", max_length=255, verbose_name="intitule cu cours")
    enseignant = models.CharField (help_text= "Nom de l'enseignant", null=False, verbose_name= "Nom de l'enseignant", max_length= 255)
    teacherTel = models.IntegerField (help_text="Entre le numero de l'enseignant", null=False)

    def __str__(self):
        jourStr = str(self.jour)
        teacherTelStr = str(self.teacherTel)
        return jourStr + " " + self.cours + " " + self.enseignant + " " + teacherTelStr
    
    
class MiawTeachers (models.Model):
    nom = models.CharField (primary_key=True, null=False, default="M Raoul", verbose_name= "nom de l'enseignant", max_length=255)
    telephone = models.IntegerField (null=False)

    def __str__(self):
        return self.nom