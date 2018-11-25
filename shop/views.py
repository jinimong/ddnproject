import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm

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


@login_required
def item_new(request, item=None):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save()
            return redirect(item)
    else:
        form = ItemForm(instance=item)

    return render(request, 'shop/item_edit.html', {
        'form': form,
    })


@login_required
def item_edit(request, id):
    item = get_object_or_404(Item, pk=id)
    return item_new(request, item)


@login_required
def item_remove(request, id):
    item = get_object_or_404(Item, pk=id)
    item.delete()
    return redirect('shop:item_list')
