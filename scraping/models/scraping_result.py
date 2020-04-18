from django.db import models
from scraping.models.common_column import CommonColumnsModel


class ScrapingResult(CommonColumnsModel):
    """スクレイピング結果"""

    class Meta:
        db_table = 'scraping_result'

    url = models.URLField(max_length=1024, null=True, verbose_name='URL')
    website_name = models.CharField(max_length=1024, null=True, verbose_name='WEBサイト名称')
    page_name = models.CharField(max_length=1024, null=True, verbose_name='ページ名称')
