from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

menu = [{'title': 'Главная страница', 'url_name': 'home'},
        {'title': 'Категории', 'url_name': 'category'},
        {'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Контакты', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'},
        ]

info = Techno.objects.all()
cat = Category.objects.all()
context = {
        'info': info,
        'menu': menu,
        'cat': cat,
    }


def index(request):
    return render(request, 'techno/index.html', context=context)


def about(request):
    return render(request, 'techno/about.html', {'menu': menu, 'title': 'О сайте'})


def contact(request):
    return render(request, 'techno/contact.html', {'menu': menu, 'title': 'Контакты'})


def goods(request, goods_id):
    return render(request, 'techno/goods.html', {'menu': menu, 'info': info, 'title': 'Купить ', 'goods_id': goods_id})


def category(request, cat_id):
    return render(request, 'techno/category.html', {'menu': menu, 'cat': cat, 'title': 'Категории', 'cat_id': cat_id})


def login(request):
    return render(request, 'techno/login.html', {'menu': menu, 'title': 'Вход'})


def pageNotFound(request, exeption):
    return render(request, 'techno/pnf.html')
