from django.shortcuts import render
from django.views.generic import TemplateView


def home(request):
    return render(request, "index.html")

class HomeView(TemplateView):
    template_name = 'index.html'
class Sa1ytView(TemplateView):
    template_name = '1sayt.html'
class Sa2ytView(TemplateView):
    template_name = '2sayt.html'
class Sa3ytView(TemplateView):
    template_name = '3sayt.html'
