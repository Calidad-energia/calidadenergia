from django.urls import path
from .views import*

urlpatterns = [ 
    path('registro/',registro_vista,name='registro'),
    path('login/',login_vista,name='login'),
    path('logout/',logout_vista,name='logout'),
    path('principal/',principal_vista,name='principal'),
]