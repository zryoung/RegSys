from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

# Create your views here.
from django.views.generic.base import View

from .forms import StudForm


def index(request):
    if request.method == 'POST':
        form = StudForm(request.POST)
        if form.is_valid():
            form.save()
            HttpResponse('hello')
    else:
        form = StudForm()

    return render(request, 'student/add.html', {'form': form})


class AddStudView(View):
    def post(self, request):
        add_stud_form = StudForm(request.POST)
        if add_stud_form.is_valid():
            add_stud_form.save(commit=True)
            HttpResponse('success')
            # return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            add_stud_form = StudForm()
            HttpResponse('fail')
            # return HttpResponse('{"status":"fail","msg":"报名出错"}', content_type='application/json')
        return render(request, 'student/add.html', {'form': add_stud_form})
