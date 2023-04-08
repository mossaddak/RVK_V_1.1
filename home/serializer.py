from rest_framework.serializers import ModelSerializer
from .models import(
    Banner,
    LatestVideo,
    Initiative
)

class BannerSerializer(ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__" 

class LatestVideoSerializer(ModelSerializer):
    class Meta:
        model = LatestVideo
        fields = "__all__" 

class InitiativeSerializer(ModelSerializer):
    class Meta:
        model = Initiative
        fields = "__all__" 


