from django.urls import path

from .views import add_link

app_name= 'link'

urlpatterns = [
    path('add/', add_link, name='add_link'),
]