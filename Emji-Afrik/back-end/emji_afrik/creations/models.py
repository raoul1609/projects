from django.db import models

# Create your models here.

## modele Categorie
class Category(models.Model):
    name=models.CharField(max_length=100)

    class Meta:
        db_table = 'emji_categories'

    def __str__(self):
        return self.name

## modele Tag
class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'emji_tag'

    def __str__(self):
        return self.name
    

def upload_to_path(instance, filename):
    return f'images/{instance.titre}/{filename}'
    
## modele Creations
class Creations (models.Model):
    titre = models.CharField (max_length=100)
    description = models.TextField(null=False)
    image = models.ImageField(upload_to=upload_to_path)
    prix = models.IntegerField()
    categorie = models.ForeignKey (Category, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'emji_creations'

    def __str__(self):
        return self.titre