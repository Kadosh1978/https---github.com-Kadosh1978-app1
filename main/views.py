from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context: dict [str, str] = {
        'title': 'Home - главная',
        'content' : 'Магазин мебели HOME'
    }
    return render(request, 'main/index.html', context)
 
def about(request):
    context: dict [str, str] = {
        'title': 'Home - О нас',
        'content' : 'О нас',
        'text_on_page': 'This shop is brilliant'
    }
    return render(request, 'main/about.html', context)
