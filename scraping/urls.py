from django.urls import path
from scraping.views.index import index_view

app_name = 'scraping'
urlpatterns = [
    path('', index_view, name='index'),
]