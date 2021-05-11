from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse



def index(request):
    context = {
            'foo': 'foo',
            }
    return render(request, 'simpleweb/index.html', context)
# Create your views here.
