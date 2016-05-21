# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, Http404

from models import Question, Answer


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def post_list_all(request):
    questions = Question.objects.all().order_by('-added_at')
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, 10)
    paginator.baseurl = '/?page='
    page = paginator.page(page) # Page
    return render(request, 'index.html', {
        'questions': page.object_list,
        'paginator': paginator, 'page': page,
    })

def popular(request):
    questions = Question.objects.all().order_by('-rating')
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, 10)
    paginator.baseurl = '/popular/?page='
    page = paginator.page(page) # Page
    return render(request, 'popular.html', {
        'questions': page.object_list,
        'paginator': paginator, 'page': page,
    })

def question(request, question_id):
    try:
        q = Question.objects.get(id=question_id)
    except ObjectDoesNotExist, err:
        raise Http404()

    answers = Answer.objects.filter(question=q)[:]
    return render(request, 'question.html', {
        'answers': answers
    })