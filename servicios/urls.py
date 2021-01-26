from . import views
from .views import *
from django.urls import path

urlpatterns = [
    path('servicios/crear', servicio_crear, name='servicio_crear'),
    path('servicios/list', views.CursoList.as_view(), name='servicio_list'),
    path('servicios-delete/<int:id>', views.ServicioDelete, name='servicio_delete'),

]