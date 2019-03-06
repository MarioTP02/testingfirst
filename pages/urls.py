from django.urls import path

from .views import *

urlpatterns = [
    path('', homePageView, name='home'),
    path('2', kPageView, name='2'),
    path('3', aPageView, name='3'),
]
#komentar