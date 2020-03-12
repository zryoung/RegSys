from django.urls import path
from .views import AddStudView
from . import views

app_name = 'Student'


urlpatterns = [
    path('', views.index, name='index'),
    path('add/', AddStudView.as_view(), name='add_stu'),
]