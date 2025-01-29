from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_user(request):
    if (request.method == 'POST'):
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username= username, password = password)

        if user is not None:
            login(request, user)
            return redirect ("new_index")
        else:
            messages.info(request, "Identifiant ou mot de passe incorrect")

    else:
        messages.info(request, "le formulaire post ne vient pas ")
        formulaire = AuthenticationForm()
        return render(request, "login.html", {"formulaire": formulaire}) 


def logout_user(request):
    logout(request)
    return redirect("new_index")
     

def register_user(request):
    pass 