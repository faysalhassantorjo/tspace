from django.contrib import admin
from .models import Collection, Topic, Documentation
# Register your models here.

admin.site.register(Collection)
admin.site.register(Topic)
admin.site.register(Documentation)