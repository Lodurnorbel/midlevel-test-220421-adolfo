from django.urls import path
from . import views

urlpatterns = [
    path('', views.SolarGradeAPI.as_view(), name='getAll'),
    path('inspections', views.SolarGradeByCompany.as_view(), name='inspections')
]
