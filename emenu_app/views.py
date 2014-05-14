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
        menu.count_danie = Danie.objects.filter(menu=menu).count()
        menu.url = menu.name.replace(' ', '_')
    return render_to_response('emenu_app/index.html', context_dict, context)


def menu(request, menu_name_url):
    context = RequestContext(request)
    menu_name = menu_name_url.replace('_', ' ')
    context_dict = {'menu_name': menu_name}
    try:
        menu = Menu.objects.get(name=menu_name)
        danies = Danie.objects.filter(menu=menu).order_by('title')
        paginator = Paginator(danies, 1)
        page = request.GET.get('page')
        try:
            danies_paginated = paginator.page(page)
        except PageNotAnInteger:
            danies_paginated = paginator.page(1)
        except EmptyPage:
            danies_paginated = paginator.page(paginator.num_pages)
        context_dict['danies_paginated'] = danies_paginated
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