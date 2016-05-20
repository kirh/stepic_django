# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render

from models import Question


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def post_list_all(request):
    questions = Question.objects.all().order_by('-added_at')
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, 10)
    paginator.baseurl = '/?page='
    page = paginator.page(page) # Page
    return render(request, 'index.html', {
        'posts': page.object_list,
        'paginator': paginator, 'page': page,
    })