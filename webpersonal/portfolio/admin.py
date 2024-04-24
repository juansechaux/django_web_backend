from django.contrib import admin
from .models import Project


# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created_At', 'updated_At')



admin.site.register(Project, ProjectAdmin)
