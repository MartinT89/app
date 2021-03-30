from django.conf.urls import url 
from test1 import views
from django.urls import path

urlpatterns = [
    url('tasks/', views.snippet_list),
    url('display/', views.index, name='index'),
]
