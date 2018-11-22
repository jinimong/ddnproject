import logging

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Item

logger = logging.getLogger(__name__)

def archives_year(request, year):
    return HttpResponse('{}년도..'.format(year))

def item_list(request):
    qs = Item.objects.all()

    word = request.GET.get('word', '')
    if word:
        qs = qs.filter(name__icontains=word)
        logger.debug(f'query: {word}')

    return render(request, 'shop/item_list.html', {
        'item_list': qs,
        'word': word,
    })

def item_detail(request, id):
    item = get_object_or_404(Item, pk=id)
    return render(request, 'shop/item_detail.html', {
        'item': item,
    })
