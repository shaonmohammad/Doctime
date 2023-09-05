from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('add_patient/', views.add_patient, name='add_patients'),
    path('search/', views.searching, name='search')
]
