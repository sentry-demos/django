# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.base import TemplateView
# from raven.contrib.django.raven_compat.models import client
from . import client

# Create your views here.

email = "user"

class BaseTemplateView(TemplateView):
    template_name = "myapp/home.html"

    def get_context_data(self, **kwargs):
        context = super(BaseTemplateView, self).get_context_data(**kwargs)
        context['email'] = self.request.GET.get('email') or 'user'
        client.context.merge({'tags': {
            'email': context['email']
        }})
        return context


class HomePageView(BaseTemplateView):
    template_name = "myapp/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        return context


def get_some_squares(n=3):
    reply = 'The first {} squares are: '.format(n)
    for x in range(1, n+1):
        reply += '{}, '.format(x * x)
    reply = reply.rstrip(', ') + '.'  # don't @ me
    return reply


class GoodView(BaseTemplateView):
    template_name = "myapp/goodbad.html"

    def get_context_data(self, **kwargs):
        context = super(GoodView, self).get_context_data(**kwargs)
        context['good_or_bad'] = 'Working'
        context['body_text'] = get_some_squares(5)
        return context


class BadView(BaseTemplateView):
    template_name = "myapp/goodbad.html"

    def get_context_data(self, **kwargs):
        context = super(BadView, self).get_context_data(**kwargs)
        context['good_or_bad'] = 'Broken'
        context['body_text'] = 'This will never be shown.'
        if True:
            raise Exception('Bad View Loaded')
        return context

class DivZero(BaseTemplateView):
    template_name = "myapp/goodbad.html"

    def get_context_data(self, **kwargs):
        context = super(DivZero, self).get_context_data(**kwargs)
        context['good_or_bad'] = 'Broken'
        context['body_text'] = 'This will never be shown.'
        1/0
        return context


class UndefinedVariable(BaseTemplateView):
    template_name = "myapp/goodbad.html"

    def get_context_data(self, **kwargs):
        context = super(UndefinedVariable, self).get_context_data(**kwargs)
        context['good_or_bad'] = 'Broken'
        context['body_text'] = 'This will never be shown.'
        c.size
        return context

class TypeError(BaseTemplateView):
    template_name = "myapp/goodbad.html"

    def get_context_data(self, **kwargs):
        context = super(TypeError, self).get_context_data(**kwargs)
        context['good_or_bad'] = 'Broken'
        context['body_text'] = 'This will never be shown.'
        [1, 2, 3].first("two")
        return context

class IndexError(BaseTemplateView):
    template_name = "myapp/goodbad.html"

    def get_context_data(self, **kwargs):
        context = super(IndexError, self).get_context_data(**kwargs)
        context['good_or_bad'] = 'Broken'
        context['body_text'] = 'This will never be shown.'
        a = []
        a.fetch(1)
        return context

class WrongNumArgs(BaseTemplateView):
    template_name = "myapp/goodbad.html"

    def get_context_data(self, **kwargs):
        context = super(WrongNumArgs, self).get_context_data(**kwargs)
        context['good_or_bad'] = 'Broken'
        context['body_text'] = 'This will never be shown.'
        [1, 2, 3].first("two")
        return context
