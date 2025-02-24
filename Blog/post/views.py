from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from .models import Post, Category
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .forms import CreatePostForm
from datetime import datetime

# Create your views here.


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
        return render (request, 'post_details.html', {'thePost': post} )
    except Http404:
        messages.info(request, 'il n y a pas de poste avec pour id {1}'.format(post_id))
        return HttpResponse ('Il n y a pas de post avec cet identifiant')
    


def addPost(request):
    '''
        view to add a post
    '''
    context = {}
    if request.method == 'POST':
        formulaire = CreatePostForm(request.POST)

        if formulaire.is_valid():
            validedName = formulaire.cleaned_data['name']
            validedContent = formulaire.cleaned_data['content']
            datePost = datetime.now()
            Post.objects.create(name= validedName, content=validedContent, created_at=datePost)
            context = {'message': 'Ok, le post a ete cree avec success', 'form': formulaire}
            return render (request, 'add_post.html', context )
        else:
            formulaire = CreatePostForm()
            #messages.info(request, 'formulaire non valide')
            context = {'message': 'formulaire non valide, veuillez recommencer.'}
    else:
        return render(request, 'add_post.html', {})


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
            return render(request, 'delete_post.html', {'message': 'le post que vous voulez supprimer n existe pas.'})
    else:
        return render(request, 'delete_post.html', {'post': postToDelete})

    
       
       
        
   
       


