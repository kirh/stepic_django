# -*- coding: utf-8 -*-

import time
from django import forms

from models import Question, Answer
from django.contrib.auth.models import User


class AskForm(forms.Form):
    title = forms.CharField(widget=forms.Textarea)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        return self.cleaned_data
        # if is_spam(self.clean_data):
        #     raise forms.ValidationError(
        #         u'Сообщение похоже на спам',
        #         code='spam'
        #     )

    def save(self):
        user = User(username='x_'+str(int(time.time())),
                    password='y_'+str(int(time.time())))
        user.save()
        self.cleaned_data['author'] = user
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):

    # def __init__(self, question, **kwargs):
    #     self._question = question
    #     self.question_id = question.id
    #     super(AnswerForm, self).__init__(**kwargs)

    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput())


    # def clean_message(self):
    #     message = self.cleaned_data['message']
    #     if not is_ethic(message):
    #         raise forms.ValidationError(
    #             u'Сообщение не корректно', code=12)
    #     return message + "\nThank you for your attention."

    def save(self):
        user = User(username='x_'+str(int(time.time())),
                    password='y_'+str(int(time.time())))
        user.save()
        self.cleaned_data['author'] = user
        question = Question.objects.get(id=self.cleaned_data['question'])
        self.cleaned_data['question'] = question
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer

    # def clean(self):
    #     pass
    #     # if is_spam(self.clean_data):
    #     #     raise forms.ValidationError(
    #     #         u'Сообщение похоже на спам',
    #     #         code='spam'
    #     #     )