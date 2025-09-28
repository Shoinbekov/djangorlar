from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import pytz
from datetime import datetime

def welcome_page(request):
    """
    Отображает главную стриницу с тремя кнопками.
    """
    return render(request, 'welcome.html')

def users_list(request):
    """
    Отображает список пользователей с их данными.
    """
    users = [
        {'full_name': 'Shoinbekov Shoinbek', 'age': 21},
        {'full_name': 'Dusikenova Samira', 'age': 21},
        {'full_name': 'Shoinbekova Azmina', 'age': 11},
    ]
    context = {'users': users}
    return render( request, 'users_list.html', context)

def city_time(request):
    """
    Показывает реальное для выбранных городов.
    """
    city_time = {
        'Almaty': datetime.now(pytz.timezone('Asia/Almaty')),
        'Calgary': datetime.now(pytz.timezone('America/Edmonton')),
        'Moscow': datetime.now(pytz.timezone('Europe/Moscow')),
        'UTC': datetime.now(pytz.utc),
    }
    context = {'city_time': city_time}
    return render(request, 'city_time.html', context)

def counter(request):
    """
    Обрабатывает счетчик, увеличивая его по нажатию кнопки.
    """
    if 'counter_value' not in request.session:
        request.session['counter_value'] = 0

    if request.method == 'POST':
        if 'increment' in request.POST:
            request.session['counter_value'] += 1

    context = {'counter_value': request.sission['counter_value']}
    return render(request, 'counter.html', context)

def reset_counter(request):
    """
    Сбрасывает значение счетчика.
    """
    request.session['counter_value'] = 0
    return redirect(reverse('counter'))

def index(request):
    return HttpResponse("Django is up!")

# Create your views here.
