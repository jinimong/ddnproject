from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

def archives_year(request, year):
    return HttpResponse('{}년도..'.format(year))

def item_list(request):
    qs = Item.objects.all()

    word = request.GET.get('word', '')
    if word:
        qs = qs.filter(name__icontains=word)

    return render(request, 'shop/item_list.html', {
        'item_list': qs,
        'word': word,
    })
