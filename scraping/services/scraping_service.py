import os
from django.contrib.auth.models import User
from requests.exceptions import MissingSchema

from scraping.models import ScrapingResult, ScrapingImage
import re
import requests
from bs4 import BeautifulSoup
from config import settings

class ScrapingService:
    def __init__(self, user: User):
        self.user = user

    def get_scraping_results(self, scraping_url):
        # ①-④.画像ページのURLを格納するリストを用意
        linklist = [scraping_url]

        # ●各画像ページから画像ファイルのURLを特定
        # ③-①.画像ページのURLを1つずつ取り出す
        for page_url in linklist:
            # ③-②.画像ページのhtmlを取得
            page_html = requests.get(page_url).text
            # ③-③.画像ページのオブジェクトを作成
            page_soup = BeautifulSoup(page_html, "lxml")
            # ③-④.画像ファイルのタグをすべて取得
            img_list = page_soup.find_all('img')

            # スクレイピング結果がない場合
            if len(img_list) == 0:
                return None

            dict_desc = page_soup.find(name='meta', attrs={'name': 'description'})
            scraping_result = ScrapingResult.objects.create(url=page_url,
                                                            website_name=page_soup.title.string,
                                                            page_name=dict_desc['content'] if dict_desc else None)

            # ③-⑤.imgタグを1つずつ取り出す
            scraping_image_files = []
            for img in img_list:
                # ③-⑥.画像ファイルのURLを抽出
                img_url = (img.get('src'))
                # ③-⑦.画像ファイルの名前を抽出
                filename = re.search(".*\/(.*png|.*jpg|.*gif)$", img_url)
                if filename is None:
                    continue

                # ●画像ファイルのURLからデータをダウンロード
                try:
                    # ④-①.画像ファイルのURLからデータを取得
                    image = requests.get(img_url)
                    if image.status_code == 404:
                        continue
                except MissingSchema:
                    # ④-④.失敗した場合はエラー表示
                    print("MissingSchema")
                    continue
                # Save File
                image_path = self.write_image(image.url, os.path.basename(image.url))
                scraping_image = ScrapingImage(url=img_url,
                                               full_image=image_path,
                                               description=img.get('alt'),
                                               scraping_result=scraping_result)
                scraping_image_files.append(scraping_image)

            ScrapingImage.objects.bulk_create(scraping_image_files)

        results = ScrapingImage.objects.filter(scraping_result=scraping_result)
        return results

    # Save File and Return FilePath
    def write_image(self, url, name=None):
        res = requests.get(url)
        if res.status_code != 200:
            return "No Image"
        path = "scraping/"
        if name == None:
            path += url.split("/")[-1]
        else:
            path += name
        with open(settings.MEDIA_ROOT + '/' + path, 'wb') as file:
            file.write(res.content)
        return path
