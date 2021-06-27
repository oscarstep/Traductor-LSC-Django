from django.db import models

# Create your models here.
class Equipo(models.Model):
    idPersona = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    urlImg = models.CharField(max_length=100)
    cargo = models.CharField(max_length=30)
    correo = models.EmailField()
    def __str__(self):
        return "{0}, {1} ({2})".format(self.nombre, self.cargo, self.idPersona)


class Institucion(models.Model):
    idInstitucion = models.IntegerField(primary_key=True)
    nombreInstitucion = models.CharField(max_length=240)
    correoInstitucion = models.EmailField()
    direccion = models.CharField(max_length=240)
    def __str__(self):
        return "{0} ({1})".format(self.nombreInstitucion, self.idInstitucion)

class Contacto(models.Model):
    idContacto = models.IntegerField(primary_key=True)
    Descripcion_Nosotros = models.CharField(max_length=500)
    Descripcion_Ayuda = models.CharField(max_length=500)
    Pais = models.CharField(max_length=240)
    Ciudad = models.CharField(max_length=240)