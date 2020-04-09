import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

logger = logging.getLogger('app')

@login_required
def index_view(request):
    if request.path == '/scraping/':
        return render(request, 'index.html')
    return redirect('scraping:index')
