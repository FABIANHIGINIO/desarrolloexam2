from django.contrib import admin

# Register your models here.


from .models import Comentario, Usuario
admin.site.register(Comentario)
admin.site.register(Usuario)