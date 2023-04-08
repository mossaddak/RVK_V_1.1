from django.shortcuts import render
from rest_framework.permissions import (
    BasePermission, SAFE_METHODS
)
from rest_framework import (
    parsers,
)

from rest_framework.viewsets import(
    ModelViewSet
)
from .models import(
    Banner,
    LatestVideo,
    Initiative

)
from .serializer import(
    BannerSerializer,
    LatestVideoSerializer,
    InitiativeSerializer,
)

class ReadOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

# Create your views here.
class BannerModelView(ModelViewSet):

    serializer_class = BannerSerializer
    queryset = Banner.objects.all()
    permission_classes = [ReadOnlyPermission]

    print("BannerSerializer=====================================")

    parser_classes = [parsers.FormParser, parsers.MultiPartParser]

class LatestVideoModelView(ModelViewSet):

    serializer_class = LatestVideoSerializer
    queryset = LatestVideo.objects.all()
    permission_classes = [ReadOnlyPermission]

class InitiativeVideoModelView(ModelViewSet):

    serializer_class = InitiativeSerializer
    queryset = Initiative.objects.all()
    permission_classes = [ReadOnlyPermission]