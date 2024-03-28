from django.urls import path
from .views import *

urlpatterns = [
    path('maqolalar/',BlogView.as_view(),name='maqolalar'),
]
