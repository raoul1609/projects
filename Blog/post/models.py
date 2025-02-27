from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category (models.Model):
    name = models.CharField (null=False, max_length=255, unique=True)

    class Meta:
        db_table = 'blog_categories'

    def __str__(self):
        return self.name
    
    
class Tag(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'blog_tags'
   
    def __str__(self):
        return self.name


class Post (models.Model):
    title = models.CharField (null= False, max_length=255)
    content = models.TextField (null= False, default = '', max_length=2000 )
    created_at = models.DateTimeField (auto_now_add=True, help_text= 'entre une date de creation', null=False)
    updated_at = models.DateTimeField (auto_now_add=True, help_text= 'entre une date de mise a jour', null=False)
    category = models.ForeignKey (Category, on_delete=models.SET_NULL, null=True, blank=True)
    # une realtion manytomany entre tag et posts
    tag = models.ManyToManyField(Tag, related_name='posts', blank=True)  #L'option related_name='posts' permet d'accéder à tous les posts associés à un tag via tag.posts


    class Meta:
        db_table = 'blog_posts'

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

    class Meta:
        db_table = 'blog_comments'

    def __str__(self):
        return ("comment by {0} at {1}".format(self.author, self.created_at))



class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=100)
    profile_picture = models.ImageField()

    class Meta:
        db_table = 'blog_profiles'  #p ersonnaliser le nom de la table dans le bd


