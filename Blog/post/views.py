from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from .models import Post, Comment
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .forms import CreatePostForm, SignupForm
from datetime import datetime

### IMPORT UTILES POUR ENVOYER LES MAILS
from django.conf import settings
from django.core.mail import send_mail

### IMPORT UTILES POUR IMPLEMENTER LES API
from rest_framework import generics
from .serializers import PostSerializer




### CLASSES POUR MON API ####

# endpoint pour avoir la liste des posts 
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer







### IMPLEMENTATION DES VUES AVEC LES FONCTIONS : on peut aussi le faire avec les classes.

def getAllPosts (request):
    '''
        first view to get all the posts inside the database
        included, the pagination of the page.
    '''

    allPosts = Post.objects.all()

    paginator = Paginator(allPosts, 5) # afficher 5 post par page 
    page = request.GET.get('page') # recupere le numero de la page depuis l'url
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # si le parametre page n'est pas un entier affiche la premiere page
        posts = paginator.page(1)
    except EmptyPage:
        # si la page est hors limite (trop grande), affiche la derniere page
        posts = paginator.page(paginator.num_pages)

    return render (request, 'post_list.html', {'posts': posts})



def postDetails(request, post_id):
    '''
        view that gives more details about one specific post
    '''
    try:
        post = get_object_or_404 (Post, id= post_id)
        comments = Comment.objects.filter(post = post).order_by('-created_at') # -created_at indique que le tri se fera par ordre decroissant, du plus recent au plus ancien
        return render (request, 'post_details.html', {'thePost': post, 'comments': comments})
    
    except Http404:
        messages.info(request, 'il n y a pas de poste avec pour id {1}'.format(post_id))
        return HttpResponse ('Il n y a pas de post avec cet identifiant')
    
#le decorateur login_required permet de proteger une vue, en exigeant une connexion avant l'appel de cette fonction
# pour proteger les vues basees sur les classes, ca se passe autrement, on utilise autre technique.

@login_required
def addPost(request):
    '''
        view to add a post
    '''
    context = {}
    if request.method == 'POST':
        formulaire = CreatePostForm(request.POST)

        if formulaire.is_valid():

            validedTitle = formulaire.cleaned_data['title']
            validedContent = formulaire.cleaned_data['content']
            datePost = datetime.now()
            Post.objects.create(title= validedTitle, content=validedContent, created_at=datePost)
            return render (request, 'add_post.html', {'message': 'Ok, le post a ete cree avec success', 'form': formulaire})
        
        else:
            formulaire = CreatePostForm()
            #messages.info(request, 'formulaire non valide')
            return render (request, 'add_post.html', {'message':'formulaire non valide, veuillez recommencer.', 'form': formulaire})
    else:
        formulaire = CreatePostForm()
        
    return render(request, 'add_post.html', {'message': '', 'form': formulaire})


@login_required
def update_post(request, post_id):
    '''
        this view is used for update some post
    '''
    try:
        thepost = get_object_or_404 (Post, id=post_id)
        if request.method == 'POST':
            update_form = CreatePostForm(request.POST, instance= thepost) 

            if update_form.is_valid():
                update_form.save()
                return render ()
        else:
            update_form = CreatePostForm(instance=thepost)
            return render (request, 'update_post.html', {'formulaire': update_form})
        
    except Http404:
            return render(request, 'update_post.html', {'message': 'ce post n existe pas encore'})
    

@login_required    
def delete_post(request, post_id):
    '''
        this view is for delete post
    '''
    if request.method == 'POST':
        try:
            postToDelete = get_object_or_404(Post, id=post_id)
            postToDelete.delete()
            return redirect('posts')
        
        except Http404:
            #return render(request, 'delete_post.html', {'message': 'le post que vous voulez supprimer n existe pas.'})
            return redirect('posts')
    else:
        return render(request, 'delete_post.html', {})
    

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid() :
            user = form.save()
            login(request, user) #connecte user apres inscription

            # Envoyer un email de confirmation
            send_mail(
                'Neudjieu te souhaite la bienvenue',
                'Merci pour la creation de ton compte!',
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,
            )
            return redirect('post_list')
        
    else:
        form = SignupForm()
        #return render (request, 'signup/signup.html', {'form': form}) # donne une erreur lors de l'execution
    
    return render (request, 'signup/signup.html', {'form': form})

    
       
       
        
   
       


