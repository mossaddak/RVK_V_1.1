from rest_framework.serializers import ModelSerializer
from .models import(
    NewsCategory,
    News
)

class NewsCategorySerializer(ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = "__all__" 


class NewsSerializer(ModelSerializer):
    news_category = NewsCategorySerializer(read_only=True)
    class Meta:
        model = News
        fields = "__all__" 



