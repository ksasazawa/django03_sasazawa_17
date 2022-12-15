from django import forms
from .models import Post

class PostForm(forms.Form):
    qualification_list = [
        ("２級土木施工管理", "２級土木施工管理")
        , ("１級土木施工管理", "１級土木施工管理")
        , ("２級建築施工管理", "２級建築施工管理")
        , ("１級建築施工管理", "１級建築施工管理")
        , ("２級電気工事施工管理", "２級電気工事施工管理")
        , ("１級電気工事施工管理", "１級電気工事施工管理")
        , ("２級管工事施工管理", "２級管工事施工管理")
        , ("１級管工事施工管理", "１級管工事施工管理")
        , ("２級造園施工管理", "２級造園施工管理")
        , ("１級造園施工管理", "１級造園施工管理")
        , ("２級電気通信工事施工管理", "２級電気通信工事施工管理")
        , ("１級電気通信工事施工管理", "１級電気通信工事施工管理")
        , ("資格不問", "資格不問")
        ]
    agent_list = [
        ("株式会社夢真", "株式会社夢真")
        , ("株式会社テクノプロ・コンストラクション", "株式会社テクノプロ・コンストラクション")
        , ("共同エンジニアリング株式会社", "共同エンジニアリング株式会社")
        , ("株式会社アーキ・ジャパン", "株式会社アーキ・ジャパン")
        , ("株式会社TS工研", "株式会社TS工研")
        , ("ブライザ株式会社", "ブライザ株式会社")
        , ("株式会社ウィルオブ・コンストラクション", "株式会社ウィルオブ・コンストラクション")   
    ]
    title = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder':'タイトル'}))
    slug = forms.SlugField()
    job = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder':'業務内容'}))
    qualification = forms.MultipleChoiceField(choices = qualification_list, widget=forms.CheckboxSelectMultiple)
    location = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder':'勤務地'}))
    body = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'placeholder':'入力してください'}))
    price = forms.IntegerField()
    agent = forms.MultipleChoiceField(choices = agent_list, widget=forms.CheckboxSelectMultiple)
    create_user = forms.IntegerField()
