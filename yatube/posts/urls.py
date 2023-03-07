# posts/urls.py
from django.urls import path
from . import views
app_name = 'posts'

urlpatterns = [
    
    path('', views.index, name='index'),
    path('group/<slug:slug>/', views.groups, name='group_list'),

]
