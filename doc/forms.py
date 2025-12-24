from .models import Documentation, Topic
from django.forms import ModelForm

class DocumentationForm(ModelForm):
    class Meta:
        model = Documentation
        fields = ['content']

class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['title','collection']
    
    # style
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
