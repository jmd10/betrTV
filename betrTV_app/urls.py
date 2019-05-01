''' defines the url patterns for betrTV_app '''

from django.urls import path
from . import views

app_name = 'betrTV_app'
urlpatterns = [
    # Home Page
    path('', views.index, name='index')
]
