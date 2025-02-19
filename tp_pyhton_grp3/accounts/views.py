from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        print(user)

        if user is not None:
            login(request, user)
            messages.info(request, "ok utilisateur connecter avec succes")
            return render(request, "emploi_du_temps/new_index.html", {})
        
        else:
            messages.info(request, "Identifiant ou mot de passe incorrect")

    else:
        messages.info(request, "le formulaire post ne vient pas ")
        formulaire = AuthenticationForm()

    return render(request, "login.html", {"formulaire": formulaire})


def logout_user(request):
    logout(request)
    return HttpResponse ("<p> Ok, utilisateur deconnecte avec succes.</p>")


def register_user(request):
    if request.method == 'POST':
        formulaire = UserCreationForm(request.POST)

        if formulaire.is_valid():
            formulaire.save()
            messages.info(request, "Ok utilisateur cree avec succes")
            return HttpResponse ("Ok, utilisateur enregistre avec succes.")
        
        else:
        # reinitialise le formulaire
            formulaire = UserCreationForm()
            messages.info(request, "formulaire non valide")
            return render(request, "register.html", {"formulaire": formulaire})
    else:
        formulaire = UserCreationForm()

    return render(request, "register.html", {"formulaire": formulaire})

