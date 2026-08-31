from django import forms
from .models import Documentation, Topic


class DocumentationForm(forms.ModelForm):
    class Meta:
        model = Documentation
        fields = ['content']



class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'order', 'group']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control',
            })