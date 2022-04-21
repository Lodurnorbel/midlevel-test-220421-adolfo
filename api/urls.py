from django.urls import path
from . import views

urlpatterns = [
    path('', views.SolarGradeAPI.as_view())
    # path('inspections?company=<string:company_name>', views.getAll, name='getAll')
]
