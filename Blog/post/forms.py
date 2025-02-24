from django import forms
from .models import Post, Category

class CreatePostForm (forms.Form):

    '''
        form used to create a new post
    '''

    categories = forms.ModelChoiceField (queryset= Category.objects.all(), label='choisir une categorie')

    model = Post
    fields = ['name', 'content']
    labels = {'name': 'nom du post', 'content': 'contenu du post'}

    widgets = {
        'name': forms.TextInput(attrs={'placeholder': 'ex: un post'}),
        'content': forms.Textarea (attrs={'placeholde': 'ceci est le contenu du post'})
    }


class UpdatePostForm(forms.Form):

    '''
        form used to update some existant post
    '''

    model = Post 
    fields = ['new name', 'new content']
    labels = {'new name': 'nouveau titre', 'new content': 'nouveau contenu'}

    widgets = {
        'new name': forms.TextInput(attrs={'placeholder': 'nouveau titre'}),
        'new content': forms.Textarea(attrs={'placeholder': 'nouveau contenu du message'})
    }