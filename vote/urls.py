from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name='index'),
    path('vote', views.vote, name='vote'),
    path("success", views.vote_success, name='vote_success'),
    path("error",views.error,name='error')
]

