# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, Http404, HttpResponseRedirect

from models import Question, Answer
from forms import AskForm, AnswerForm


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
    form = AnswerForm()
    return render(request, 'question.html', {
        'answers': answers,
        'question': q,
        'form': form
    })

def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'ask.html', {
        'form': form
    })

def answer(request):
    if request.method == "POST":
        form = AnswerForm(request.POST)

        print form.data
        if form.is_valid():
            answer = form.save()
            url = answer.get_url()
            print url
            return HttpResponseRedirect(url)
        else:
            raise Http404
            # return HttpResponseRedirect(reverse('question'), [question_id])
    else:
        raise Http404
