from django.db import models

# Create your models here.

class Category (models.Model):
    name = models.CharField (null=False, max_length=255)

    def __str__(self):
        return self.name

class Post (models.Model):
    title = models.CharField (null= False, help_text= 'Renseigne un titre', max_length=255)
    content = models.TextField (null= False, default = '', max_length=2000 )
    created_at = models.DateTimeField (auto_now_add=True, help_text= 'entre une date de creation', null=False)
    updated_at = models.DateTimeField (auto_now_add=True, help_text= 'entre une date de mise a jour', null=False)
    category = models.ForeignKey (Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return ({1} + '' + {2} + ' cree le' + {str(self.created_at)}).format (self.title, self.content)

class Comment (models.Model):
    '''
        class that builds a comment model
    '''
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
    author = models.CharField(null=False, help_text='auteur du commentaire', max_length=255)
    content = models.TextField(null=False, default='', max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True, help_text='temps de creation')
