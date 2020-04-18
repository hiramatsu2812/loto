# Generated by Django 2.2 on 2020-04-18 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScrapingImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
                ('create_user', models.CharField(default='admin', max_length=32, verbose_name='登録ユーザ')),
                ('update_datetime', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('update_user', models.CharField(default='admin', max_length=32, verbose_name='更新ユーザ')),
                ('delete_flg', models.BooleanField(default=False, verbose_name='削除フラグ')),
                ('url', models.URLField(max_length=1024, verbose_name='URL')),
                ('full_image', models.ImageField(height_field='full_height', upload_to='full/', verbose_name='フルサイズ画像ファイル', width_field='full_width')),
                ('full_height', models.IntegerField(editable=False)),
                ('full_width', models.IntegerField(editable=False)),
                ('thumbnail_image', models.ImageField(height_field='thumbnail_height', upload_to='thumbnail/', verbose_name='サムネイル画像ファイル', width_field='thumbnail_width')),
                ('thumbnail_height', models.IntegerField(editable=False)),
                ('thumbnail_width', models.IntegerField(editable=False)),
                ('scraping_result', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='scraping.ScrapingResult', verbose_name='スクレイピング結果')),
            ],
            options={
                'db_table': 'scraping_image',
            },
        ),
    ]
