from django.db import models

# Create your models here.
class Persona(models.Model):
	nombre = models.CharField(max_length=30)
	nota = models.DecimalField(decimal_places=1, max_digits=2)

	def __str__(self):
		return self.nombre