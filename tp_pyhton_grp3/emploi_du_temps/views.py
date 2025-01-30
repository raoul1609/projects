from django.db import IntegrityError, ProgrammingError
from django.shortcuts import redirect, render, get_object_or_404
from django.http import Http404, HttpResponse
from .models import Programme, MiawTeachers
from datetime import date, datetime
from .forms import ProgammeForm, TeacherForm
from django.contrib import messages

from rest_framework import generics
from .serializers import TeacherSerializer

                ### CLASSES POUR MON API ####

class MiawTeachersList(generics.ListCreateAPIView):
    queryset = MiawTeachers.objects.all()
    serializer_class = TeacherSerializer

class MiawTeachersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MiawTeachers.objects.all()
    serializer_class = TeacherSerializer



                #### DEFINITIONS DES DIFFERENTES VUES DJANGO####

def index (request):
    context ={'titre': "Page d'acceuil"}
    #context = ["NEUDJIEU RAOUL", "TCHUENTE PIERRETTE", "KEMAJOU SIMEU", "MENDOUGA ARMEL", "AYINA YVES"]
    return render (request, 'new_index.html', context)


def saveProgram (request):
    if (request.method == 'POST'):
        formulaire = ProgammeForm (request.POST)
        if formulaire.is_valid():
            # recuperer les donnees verifies dans le formulaire
            dateVerified = formulaire.cleaned_data ["jour"]
            nameTeaherVerified = formulaire.cleaned_data['enseignants']
            intituleCours = formulaire.cleaned_data ["cours"]

            #check si il y a deja cours a la date du formulaire
            try:
                checkExistantCourse = get_object_or_404(Programme, pk= dateVerified)
                if type(checkExistantCourse)== Programme :
                    messages.error(request, "Il y a deja un cours programme a la date du " + str(dateVerified) )
                    return redirect ('saveProgram')
            
            except Http404:
                # faire une requette dans le bd pour recuperer l'enseignant et ses infos
                lookForTeacher = MiawTeachers.objects.get(nom = nameTeaherVerified)
                formToSave = Programme.objects.create (jour = dateVerified, cours= intituleCours, enseignant=nameTeaherVerified, teacherTel= lookForTeacher.telephone)
                messages.success (request, "Ok, le programme a ete enregistre avec succes" )
                return render (request, 'new_saveNewProgram.html', {})
        else:
            formulaire = ProgammeForm()
            context = {"titre": "Definir Programme",
                "messageError": "Il y a deja un cours programme a cette date.",
                "message": "Formulaire d'enregistrement d'un programme journalier",
                "formulaire": formulaire}
            return render (request, 'new_saveNewProgram.html', context)  
              
    else:
        
        formulaire = ProgammeForm()
        context = {"titre": "Definir Programme",
                   "messageError": "",
                   "message": "Formulaire d'enregistrement d'un programme journalier",
                   "formulaire": formulaire}
        return render (request, 'new_saveNewProgram.html', context)



def translateError (databaseError):
    return databaseError['nom']


def addTeacher(request):
    #add a new in the database
    if (request.method == 'POST'):
        teacherForm = TeacherForm(request.POST)
        
        if teacherForm.is_valid():
            verifiedTeacherName = teacherForm.cleaned_data['nom']
            try :
                checkExistanceOfTeacher = get_object_or_404 (MiawTeachers, pk=verifiedTeacherName)
                if type (checkExistanceOfTeacher) == MiawTeachers:
                    message =  "Cet enseignant existe deja"
                    context = {'titre': "Ajouter un enseignant",
                               'message': message,
                               'formulaire': teacherForm}
                    return render ( request, 'addTeacher.html', context)
            
            except Http404 :
                #create and save a new teacher
                verifiedPhone = teacherForm.cleaned_data['telephone']
                newTeacher = MiawTeachers.objects.create (nom= verifiedTeacherName, telephone= verifiedPhone)
                message = "Ok, l'enseignant a ete ajoute avec succes"
                teacherForm = TeacherForm ()
                context = {'titre': "Ajouter un enseignant",
                           'message': message,
                           'formulaire': teacherForm}
                return render (request, 'addTeacher.html', context)
               
        else:
            # message est un dictionnaire contenant les erreurs de la methode is_valid()
            message = teacherForm.errors
            teacherForm = TeacherForm()
            context = {'titre': "Ajouter un enseignant",
                       'message': message,
                       'formulaire': teacherForm}
            return render (request,'addTeacher.html', context)
    else:
        teacherForm = TeacherForm()
        context = {'titre': "Ajouter un enseignant",
                   'message': "" , 
                   'formulaire': teacherForm}
        return render (request, 'addTeacher.html', context)
        


def lookForOneProgram (request, name):
    # look for the program of a specific day
    #nameOfCourse = request.GET.get ('name_course')
    print(name)
    
    if name:
        try:
            lookupProgramInDb = Programme.objects.raw ("SELECT * FROM emploi_du_temps_programme where cours = %s", [name])

            if lookupProgramInDb:
                context = {"allPrograms": lookupProgramInDb}
                return render (request, 'new_showProgam.html', context)
            else:
                return HttpResponse ("Aucun cours correspondant n'a ete trouve.")
            
        except ProgrammingError | IntegrityError :
            return HttpResponse ("Erreur survenue lors de la recherche")
        
    else:
        return HttpResponse ("Veuillez specifier le nom du cours a rechercher")
        



# fonction affiche les programmes enregistres dans la bd
def getProgram (request):
    allPrograms = Programme.objects.all()
    context = {"allPrograms": allPrograms,
               "titre": "Affichage du programme",
               "message": "Plateforme qui affiche l'emploi du temps de licence professionnelle delocalisee, filiere MIAW"}
    
    return render (request, 'new_showProgram.html', context)



