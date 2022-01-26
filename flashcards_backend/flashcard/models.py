from django.db import models

# Create your models here.
class Flashcard(models.Model):
    term = models.CharField(max_length=100, null=False)
    definition = models.CharField(max_length=250, null=False)
    collection = models.CharField(max_length=250, null=False)
    
    def __str__(self):
        return str(self.collection) + str(self.term)
    
