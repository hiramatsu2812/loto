import logging

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from scraping.forms.scraping_form import ScrapingForm
from django.views.generic import ListView

from scraping.models import ScrapingImage, ScrapingResult
from scraping.services.scraping_service import ScrapingService

logger = logging.getLogger('app')

@login_required
def index_view(request):
    if request.path == '/scraping/':
        form = ScrapingForm()
        return render(request, 'index.html', {'form': form})
    return redirect('scraping:index')


class ScrapingResultListView(LoginRequiredMixin, ListView):
    SERVICE = ScrapingService
    template_name = "index.html"
    paginate_by = 30

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.form = None
        self.scraping_url = None

    def get(self, request, *args, **kwargs):
        self.form = ScrapingForm(request.GET)
        if not self.form.is_valid():
            return HttpResponseBadRequest(content="Error Bad Request")
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        service = self.SERVICE(self.request.user)
        self.scraping_url = self.form.cleaned_data['scraping_url']
        if self.request.GET.get('page'):
            return ScrapingImage.objects.filter(
                scraping_result=ScrapingResult.objects.filter(url=self.scraping_url).order_by('-id')[0])
        object_list = service.get_scraping_results(self.scraping_url)
        return object_list

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        context['scraping_url'] = self.scraping_url
        return context
