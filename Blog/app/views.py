from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    text = ''
    description= ''
    photo = ''
    nombre = ''
    blog = ''
    # if request.user.is_authenticated:
    user = User.objects.filter(id=1)
    for user in user:
            nombre = user.first_name
         
    user_perfil = User.objects.filter(pk=1)

        
    perfil = Perfil.objects.all()
    for user in perfil:
        photo = user.photo.url
                
    for user in user_perfil:
            description = user.description_set.all()
            for description in description:
                description = description.description
                
    
    blog = Blog.objects.all()
    
    import random
    text_numero = Text.objects.all().count()
    numero_random = random.randint(1, text_numero) 
       
    text_ran = Text.objects.filter(id=numero_random)
    for text in text_ran:
        text = text.text
    
    blogers = Blogers.objects.all()
 
    
    context = {
        "nombre": nombre,
        "photo": photo,
        "description":description,
        'blog': blog,
        'text':text,
        'blogers':blogers,
    }
    return render(request, 'app/home.html', context)