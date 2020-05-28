from django.urls import path
from scraping.views.download import download_all
from scraping.views.index import index_view, ScrapingResultListView

app_name = 'scraping'
urlpatterns = [
    path('', index_view, name='index'),
    path('result/', ScrapingResultListView.as_view(), name='scraping_result'),
    path('download/', download_all, name='download_all')
]