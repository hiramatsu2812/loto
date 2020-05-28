from django import forms


class ScrapingForm(forms.Form):
    scraping_url = forms.CharField(label='スクレイピングURL',
                                   required=True,
                                   widget=forms.URLInput(
                                       attrs={'placeholder': 'URLを入力してください'}
                                   ))