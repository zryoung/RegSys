from django import forms
from django.forms import ModelForm

from Student.models import Stud


class StudForm(ModelForm):
    class Meta:
        model = Stud
        fields = '__all__'
