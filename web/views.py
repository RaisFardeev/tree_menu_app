from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest
from web.models import Menu


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'base.html', {'menus': Menu.objects.all()})


def draw_menu(request: HttpRequest, path: str) -> HttpResponse:
    splitted_path = path.split('/')
    return render(request, 'base.html', {'menu_name': splitted_path[0], 'menu_item': splitted_path[-1]})