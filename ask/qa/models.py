# -*- coding: utf-8 -*-

from django.db import models

#User model
from django.contrib.auth.models import User

#Question model
#title - заголовок вопроса
#text - полный текст вопроса
#added_at - дата добавления вопроса
#rating - рейтинг вопроса (число)
#author - автор вопроса
#likes - список пользователей, поставивших "лайк"

# class Question(models.Model):
# 	title = models.CharField(max_length = 255)
# 	text = models.TextField()
# 	added_at = models.DateTimeField(auto_now = True)
# 	rating = models.IntegerField(default = 0)
# 	author = models.ForeignKey(User)
# 	likes = models.ManyToManyField(User)
#
# #Answer model
# #text - текст ответа
# #added_at - дата добавления ответа
# #question - вопрос, к которому относится ответ
# #author - автор ответа
#
# class Answer(models.Model):
# 	text = models.TextField()
# 	added_at = models.DateTimeField(auto_now = True)
# 	question = models.ForeignKey(Question)
# 	author = models.ForeignKey(User)

class QuestionManager(models.Manager):
    def new(self):
        return True

    def popular(self):
        return True


class Question(models.Model):
    class Meta:
        db_table = 'question'
    title = models.CharField(max_length = 255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default = 0)
    author = models.ForeignKey(User, null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='likes_set', null=True,
                                   blank=True)
    objects = QuestionManager()

    def __unicode__(self):
        return self.title

    def get_url(self):
        return '/question/%s' % self.id


class Answer(models.Model):
    class Meta:
        db_table = 'answer'
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add = True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User, null=True, blank=True)

    def __unicode__(self):
        return self.text

    def get_url(self):
        return '/question/%s' % self.question.id