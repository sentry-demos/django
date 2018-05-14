# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.base import TemplateView
# from raven.contrib.django.raven_compat.models import client
from . import client

# Create your views here.


class BaseTemplateView(TemplateView):
    template_name = "myapp/home.html"

    def get_context_data(self, **kwargs):
        context = super(BaseTemplateView, self).get_context_data(**kwargs)
        user_email = self.request.GET.get('email', False)
        if user_email and user_email != 'guest':
            client.user_context({
                'email': user_email
            })
        context['email'] = user_email or "guest"
        return context

class HomePageView(BaseTemplateView):
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        return context

class IndexError(BaseTemplateView):
    def get_context_data(self, **kwargs):
        context = super(IndexError, self).get_context_data(**kwargs)
        a = [ 'one', 'two' ]
        x = a[1]
        return context

class DivZero(BaseTemplateView):
    def get_context_data(self, **kwargs):
        context = super(DivZero, self).get_context_data(**kwargs)
        1/0
        return context

class UndefinedVariable(BaseTemplateView):
    def get_context_data(self, **kwargs):
        context = super(UndefinedVariable, self).get_context_data(**kwargs)
        c.size
        return context

class TypeError(BaseTemplateView):
    def get_context_data(self, **kwargs):
        context = super(TypeError, self).get_context_data(**kwargs)
        [1, 2, 3].first("two")
        return context

class WrongNumArgs(BaseTemplateView):
    def get_context_data(self, **kwargs):
        context = super(WrongNumArgs, self).get_context_data(**kwargs)
        [1, 2, 3].first("two")
        return context
