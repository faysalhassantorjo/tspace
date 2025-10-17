from django.contrib import admin
from .models import Collection, Topic, Documentation, Project, Technology, ProjectImage
# Register your models here.

admin.site.register(Collection)
admin.site.register(Topic)
admin.site.register(Documentation)
admin.site.register(Project)
admin.site.register(Technology)
admin.site.register(ProjectImage)