from django.shortcuts import render
from .models import Collection, Topic, Documentation, Project
# Create your views here.
def collection_list(request):
    collections = Collection.objects.all()
    projects = Project.objects.all()
    return render(request, 'doc/collection_list.html', {'collections': collections, 'projects': projects})

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