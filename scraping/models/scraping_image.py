from django.db import models
from scraping.models import ScrapingResult
from scraping.models.common_column import CommonColumnsModel


class ScrapingImage(CommonColumnsModel):
    """スクレイピング画像"""

    class Meta:
        db_table = 'scraping_image'

    url = models.URLField(max_length=1024, verbose_name='URL')
    full_image = models.ImageField(upload_to='full/', verbose_name='フルサイズ画像ファイル',
                                   height_field='full_height', width_field='full_width')
    full_height = models.IntegerField(editable=False)
    full_width = models.IntegerField(editable=False)
    thumbnail_image = models.ImageField(upload_to='thumbnail/', verbose_name='サムネイル画像ファイル',
                                        height_field='thumbnail_height', width_field='thumbnail_width')
    thumbnail_height = models.IntegerField(editable=False)
    thumbnail_width = models.IntegerField(editable=False)
    scraping_result = models.ForeignKey(ScrapingResult, verbose_name='スクレイピング結果', on_delete=models.PROTECT)
