from django.db import models


class CommonColumnsModel(models.Model):
    """ 共通カラム """

    class Meta:
        abstract = True

    create_datetime = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)
    create_user = models.CharField(verbose_name='登録ユーザ', max_length=32, default='admin')
    update_datetime = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    update_user = models.CharField(verbose_name='更新ユーザ', max_length=32, default='admin')
    delete_flg = models.BooleanField(verbose_name='削除フラグ', null=False, default=False)
