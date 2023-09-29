from django.shortcuts import render
from django.views.generic import FormView

from .models import GovernmentEmployee
from .form import PostForm


def MainPage(request):
    return render(request, 'main.html')


def ListPage(request):
    gov_employee_list = GovernmentEmployee.objects.all()
    return render(request, 'list.html', context={'gov_employee_list': gov_employee_list})


class QuestionFormView(FormView):
    template_name = 'form.html'
    form_class = PostForm

    def form_valid(self, form):
        form.save()
        return render(self.request, 'success.html')

