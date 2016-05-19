from django.http import HttpResponse 
from django.core.paginator import Paginator

from django.shortcuts import render 
def test(request, *args, **kwargs):
    return HttpResponse('OK')

def post_list_all(request):
    page = request.GET.get('page', 1)
