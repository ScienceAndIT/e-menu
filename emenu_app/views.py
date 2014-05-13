# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response
from emenu_app.models import Menu, Danie
from emenu_app.forms import ErrorForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    context = RequestContext(request)
    menu_list = Menu.objects.filter(danie__menu__isnull=False).distinct()
    context_dict = {'menus': menu_list}
    for menu in menu_list:
        menu.url = menu.name.replace(' ', '_')
    return render_to_response('emenu_app/index.html', context_dict, context)


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


def add_error(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = ErrorForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = ErrorForm()
    return render_to_response('emenu_app/add_error.html', {'form': form}, context)