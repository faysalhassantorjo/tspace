from django.urls import path

from . import views

urlpatterns = [
    path('', views.collection_list, name='collection_list'),
    path('collection/<slug:slug>/', views.collection_detail, name='collection_detail'),
    path('topic/<int:pk>/', views.topic_detail, name='topic_detail'),
    path('project/<slug:slug>/', views.project_detail, name='project_detail'),
]