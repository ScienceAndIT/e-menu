# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("<a href='http://www.scienceandit.net'>Artur</a> says hello Heroku!")