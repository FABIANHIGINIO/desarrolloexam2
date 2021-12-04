#genera archivos HTML usando una plantilla y datos. 
from django.shortcuts import render 

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from .models import Comentario, Usuario
# Create your views here.
def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_comentarios = Comentario.objects.all().count()

     # Numero de visitas a esta view, como está contado en la variable de sesión.
    #num_visits = request.session.get('num_visits', 0)
    #request.session['num_visits'] = num_visits + 1

    context = {
        'num_comentarios':num_comentarios,
        #'num_visits':num_visits,
    } 

    # Carga la plantilla index.html con la información adicional en la variable context.
    return render(request, 'index.html', context=context)
