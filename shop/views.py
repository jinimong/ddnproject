from django.shortcuts import render
from django.http import HttpResponse


def archives_year(request, year):
    return HttpResponse('{}년도..'.format(year))
