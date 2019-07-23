from django.urls import path, include
from rest_framework import routers, serializers, viewsets

from .views import InventoreyView, HandledErrorView, UnHandledErrorView


urlpatterns = [
    path('checkout', InventoreyView.as_view()),
    path('handled', HandledErrorView.as_view()),
    path('unhandled', UnHandledErrorView.as_view()),
]
