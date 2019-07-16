from django.urls import path, include
from rest_framework import routers, serializers, viewsets

from .views import InventoreyView, HandledErrorView, UnHandledErrorView


# Routers provide an easy way of automatically determining the URL conf.
#router = routers.DefaultRouter()
#router.register(r'checkout/', InventoreyView, basename='Inventory')

urlpatterns = [
    #path(r'^', include(router.urls)),
    path('checkout', InventoreyView.as_view()),
    path('handled', HandledErrorView.as_view()),
    path('unhandled', UnHandledErrorView.as_view()),
]
