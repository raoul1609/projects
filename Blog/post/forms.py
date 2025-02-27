from django import forms
from .models import Post, Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreatePostForm (forms.ModelForm):

    '''
        form used to create a new post
    '''
    categories = forms.ModelChoiceField (queryset= Category.objects.all(), label='choisir une categorie')

    class Meta:

        model = Post
        fields = ['title', 'content']
        labels = {'title': 'titre du post', 'content': 'contenu du post'}

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'ex: un post'}),
            'content': forms.Textarea (attrs={'placeholder': 'ceci est le contenu du post'})
        }


"""class UpdatePostForm(forms.ModelForm):

    '''
        form used to update some existant post
    '''
    class Meta:

        model = Post 
        fields = ['new name', 'new content']
        labels = {'new name': 'nouveau titre', 'new content': 'nouveau contenu'}

        widgets = {
            'new name': forms.TextInput(attrs={'placeholder': 'nouveau titre'}),
            'new content': forms.Textarea(attrs={'placeholder': 'nouveau contenu du message'})
        }
"""

# pour la creation d'un nouveau compte utilisateur je voudrais demander des informations supplementaire : email, first_name, last_name
# pour cela, je cree un formulaire personnalise qui va etendre UserCreationForm fournit par django

class SignupForm(UserCreationForm):
    '''
        classe personnalisee, utile pour la creation d'un nouveau compte utilisateur.
    '''
    email = forms.EmailField(required=False)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User 
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')