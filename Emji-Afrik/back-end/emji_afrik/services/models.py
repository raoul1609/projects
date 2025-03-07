from django.db import models

# Create your models here.

# modele Service

class Services (models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
    price = models.FloatField()

    class Meta :
        db_table = 'emji_services'

    def __str__(self):
        return self.name




