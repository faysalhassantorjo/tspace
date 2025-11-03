from django.contrib import admin
from .models import Collection, Topic, Documentation, Project, Technology, ProjectImage
# Register your models here.

admin.site.register(Collection)
admin.site.register(Topic)
# admin.site.register(Documentation)
admin.site.register(Project)
admin.site.register(Technology)
admin.site.register(ProjectImage)

from django import forms
class DocumentationForm(forms.ModelForm):
    class Meta:
        model = Documentation
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Order the Topic dropdown by created_at descending (newest first)
        self.fields['topic'].queryset = Topic.objects.order_by('-created_at')
        
@admin.register(Documentation)
class DocumentationAdmin(admin.ModelAdmin):
    form = DocumentationForm
    list_display = ('topic', 'created_at', 'updated_at')

