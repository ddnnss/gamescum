from django.shortcuts import render
from django.utils.translation import gettext as _

def index(request):
    page_title = 'ГЛАВНАЯ'
    index_page_active = 'active'

    return render(request, 'home/index.html', locals())

def statistic(request):
    page_title = 'ТОП 20'
    statistic_page_active = 'active'
    return render(request, 'home/statistic.html', locals())

