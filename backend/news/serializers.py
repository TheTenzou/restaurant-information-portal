from rest_framework import serializers
from .models import NewsPicture, NewsType, News


class NewsPicturesSerializer(serializers.ModelSerializer):
    picture = serializers.FileField(max_length=None, use_url=True, allow_null=True, required=False)

    class Meta:
        model = NewsPicture
        fields = ('picture',)

        
class NewsTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsType
        fields = ['id', 'name']


class NewsShortSerializer(serializers.ModelSerializer):
    card_picture = serializers.FileField(max_length=None, use_url=True, allow_null=True, required=False)
    news_type = NewsTypeSerializer(many=False, read_only=True)

    class Meta:
        model = News
        fields = ['id', 'headline', 'publication_date', 'news_type', 'card_picture', 'slug']


class NewsSerializer(serializers.ModelSerializer):
    card_picture = serializers.FileField(max_length=None, use_url=True, allow_null=True, required=False)
    news_type = NewsTypeSerializer(many=False, read_only=True)
    news_pictures = NewsPicturesSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = ['id', 'headline', 'news_text', 'publication_date', 'news_type', 'card_picture', 'news_pictures']