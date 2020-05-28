from datetime import datetime
import logging
import zipfile
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from scraping.models import ScrapingImage, ScrapingResult

logger = logging.getLogger('app')

@login_required
def download_all(request):
    scraping_url = request.POST.get('scraping_url')
    download_files = ScrapingImage.objects.filter(scraping_result=ScrapingResult.objects.filter(url=scraping_url).order_by('-id')[0])

    response = HttpResponse(content_type='application/zip')
    file_zip = zipfile.ZipFile(response, 'w')
    for download_file in download_files:
        file_zip.writestr(download_file.full_image.name, download_file.full_image.read())

    # Content-Dispositionでダウンロードの強制
    response['Content-Disposition'] = 'attachment; filename="scraping_files_' + datetime.now().strftime("%Y%m%d%H%M%S") + '.zip"'

    return response