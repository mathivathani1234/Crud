from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CrudappModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    crudapps=models.CharField(max_length=20,blank=True)
    def __str__(self):
        return f"User (self.user)"
