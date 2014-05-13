# Create your views here.
#from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from emenu_app.models import Menu, Danie


def index(request):
    context = RequestContext(request)
    menu_list = Menu.objects.all()
    context_dict = {'menus': menu_list}
    #context_dict = {'boldmessage': "I am bold font from the context"}
    return render_to_response('emenu_app/index.html', context_dict, context)
    #return HttpResponse("<a href='http://www.scienceandit.net'>Artur</a> says hello Heroku!")