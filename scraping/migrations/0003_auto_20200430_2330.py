# Generated by Django 2.2 on 2020-04-30 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0002_scrapingimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scrapingimage',
            name='thumbnail_height',
        ),
        migrations.RemoveField(
            model_name='scrapingimage',
            name='thumbnail_image',
        ),
        migrations.RemoveField(
            model_name='scrapingimage',
            name='thumbnail_width',
        ),
        migrations.AddField(
            model_name='scrapingimage',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='scrapingimage',
            name='full_image',
            field=models.ImageField(height_field='full_height', max_length=1024, upload_to='full/', verbose_name='フルサイズ画像ファイル', width_field='full_width'),
        ),
    ]
