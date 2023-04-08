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
    class Meta:
        model = News
        fields = "__all__" 



