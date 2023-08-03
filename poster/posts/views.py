from django.shortcuts import render
from django.views.generic import *

class IndexView(TemplateView):
    template_name = 'posts/index.html'