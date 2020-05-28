from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill

from scraping.models import ScrapingResult
from scraping.models.common_column import CommonColumnsModel


class ScrapingImage(CommonColumnsModel):
    """スクレイピング画像"""

    class Meta:
        db_table = 'scraping_image'

    url = models.URLField(max_length=1024, verbose_name='URL')
    full_image = models.ImageField(upload_to='scraping/', verbose_name='フルサイズ画像ファイル',
                                   height_field='full_height', width_field='full_width', max_length=1024)
    full_height = models.IntegerField(editable=False)
    full_width = models.IntegerField(editable=False)
    thumbnail = ImageSpecField(source='full_image', processors=[ResizeToFill(200, 100)],
                               format='JPEG', options={'quality': 80})
    description = models.CharField(null=True, max_length=500)
    scraping_result = models.ForeignKey(ScrapingResult, verbose_name='スクレイピング結果', on_delete=models.PROTECT)
