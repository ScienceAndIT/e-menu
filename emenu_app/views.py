# Create your views here.
#from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from emenu_app.models import Menu, Danie


def index(request):
    context = RequestContext(request)
    menu_list = Menu.objects.all()
    context_dict = {'menus': menu_list}
    for menu in menu_list:
        menu.url = menu.name.replace(' ', '_')
    return render_to_response('emenu_app/index.html', context_dict, context)
    #return HttpResponse("<a href='http://www.scienceandit.net'>Artur</a> says hello Heroku!")


def menu(request, menu_name_url):
    context = RequestContext(request)
    menu_name = menu_name_url.replace('_', ' ')
    context_dict = {'menu_name': menu_name}
    try:
        menu = Menu.objects.get(name=menu_name)
        danies = Danie.objects.filter(menu=menu)
        context_dict['danies'] = danies
        context_dict['menu'] = menu
    except Menu.DoesNotExist:
        pass
    return render_to_response('emenu_app/menu.html', context_dict, context)