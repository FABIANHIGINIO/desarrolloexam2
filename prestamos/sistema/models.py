from django.db import models

# Create your models here.
class Comentario(models.Model):
	equipo = models.CharField(max_length=200, help_text="Ingrese el nombre del equipo")
	ip = models.CharField(max_length=15, help_text="Ingrese la direccion ip del equipo")
	Comentario = models.CharField(max_length=1000, help_text="Ingrese su comentario")
	def __str__(self):
		return self.equipo

class Usuario(models.Model):
    """
    Modelo que representa un usuario
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        """
        String para representar el Objeto Modelo
        """
        return '%s, %s' % (self.last_name, self.first_name)