from django.db import models
from django.contrib.auth.models import *

# Create your models here.
class Perfil(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, )
    photo = models.ImageField(upload_to="media/", blank=True, null=True)    
    # description = models.CharField(max_length=1000, blank=True)
    parrafo = models.TextField(max_length=500, blank=True)

    
class Blogers(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to="media/", blank=True)
    parrafo = models.TextField(max_length=500)
    
class Text(models.Model):
    text = models.TextField(max_length=500, default=" Soy desarrollador web Full Stack mis lenguajes favoritos son Python y Dart tengo unos grandes proyectos creados en con Python y Django los puedes ver en la seccion de fotos y  la mitad de los codigos en mi Github")
    
class Description(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    

class Blog(models.Model):
    # user_blog = models.ForeignKey(User, on_delete=models.CASCADE)
    # title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="media/", blank=True, null=True)
    # parrafo = models.TextField(max_length=500)
    
