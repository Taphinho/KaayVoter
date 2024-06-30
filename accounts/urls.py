from django.urls import path
from . import views

urlpatterns=[
        path('login',views.login,name='login'),
        path('success',views.success, name='success'),
]
