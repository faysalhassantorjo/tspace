from django.shortcuts import render
from .models import Collection, Topic, Documentation, Project, Technology
# Create your views here.
def collection_list(request):
    collections = Collection.objects.all().order_by('-updated_at')
    projects = Project.objects.all()
    
    techs = Technology.objects.all()
    return render(request, 'doc/collection_list.html', {'collections': collections, 'projects': projects, 'techs': techs})

def collection_detail(request, slug):
    collection = Collection.objects.get(slug=slug)
    print('collection:', collection)
    topics = collection.topics.all()
    return render(request, 'doc/collection_detail.html', {'collection': collection, 'topics': topics})

def topic_detail(request, pk):
    topic = Topic.objects.get(pk=pk)
    collection = topic.collection
    all_topics = collection.topics.all()
    
    return render(request, 'doc/topic_detail.html', {'topic': topic, 'all_topics': all_topics, 'collection': collection})

def project_detail(request, slug):
    project = Project.objects.get(slug=slug)
    return render(request, 'doc/project_details.html', {'project': project})

from .forms import DocumentationForm, TopicForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

def documentation_create(request):

    if request.method == 'POST':
        documentation_form = DocumentationForm(request.POST)
        topic_form = TopicForm(request.POST)
        if documentation_form.is_valid() and topic_form.is_valid():
            topic = topic_form.save()
            documentation = documentation_form.save(commit=False)
            documentation.topic = topic
            documentation.save()
            return redirect('/')
    else:
        documentation_form = DocumentationForm()
        topic_form = TopicForm()
    return render(request, 'doc/documentation_create.html', {
        'documentation_form': documentation_form,
        'topic_form': topic_form,
    })

def documentation_update(request, id):
    documentation = get_object_or_404(Documentation, pk=id)

    if request.method == 'POST':
        documentation_form = DocumentationForm(request.POST, instance=documentation)
        topic_form = TopicForm(request.POST, instance=documentation.topic)
        if documentation_form.is_valid() and topic_form.is_valid():
            topic = topic_form.save()
            documentation = documentation_form.save(commit=False)
            documentation.topic = topic
            documentation.save()
            return redirect('/')
    else:
        documentation_form = DocumentationForm(instance=documentation)
        topic_form = TopicForm(instance=documentation.topic)
    return render(request, 'doc/documentation_create.html', {
        'documentation_form': documentation_form,
        'topic_form': topic_form,
    })