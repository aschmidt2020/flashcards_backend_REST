from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Collection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False,  default=None)
    name = models.CharField(max_length=100, null=False)
    
    def __str__(self):
        return str(self.name)
class Flashcard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default=None)
    term = models.CharField(max_length=100, null=False)
    definition = models.CharField(max_length=250, null=False)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        return str(self.collection) + str(self.term)
    
