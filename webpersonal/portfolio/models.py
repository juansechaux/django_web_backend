from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name="Titulo")
    description = models.TextField(max_length=2500, verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    created_At = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated_At = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualizacion")

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ['-created_At']
    
    def __str__(self):
        return self.title

