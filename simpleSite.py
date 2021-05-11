from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse



def index(request):
    context = {
            'foo': 'foo',
            }
    template = loader.get_template('simpleweb/index.html')
    return HttpResponse(template.render(context, request))
# Create your views here.

