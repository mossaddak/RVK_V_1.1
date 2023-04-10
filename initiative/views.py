from django.shortcuts import render

from rest_framework import (
    parsers,
)

from rest_framework.viewsets import(
    ModelViewSet
)
from RVK_WEBPORTAL.permissions import(
    IsContentEditor
)

from .serializer import(
    HumanitarianTopSectionSerializer,
    HumanitarianBottomSectionsSerializer,
    PeaceEducationProgramTopSectionSerializer
)
from .models import(
    HumanitarianTopSection,
    HumanitarianBottomSections,
    PeaceEducationProgramTopSection
)

# Create your views here.

class HumanitarianTopSectionView(ModelViewSet):
    
    serializer_class = HumanitarianTopSectionSerializer
    queryset = HumanitarianTopSection.objects.all()
    permission_classes = [IsContentEditor]

    parser_classes = [parsers.FormParser, parsers.MultiPartParser]


class HumanitarianBottomSectionsView(ModelViewSet):
    serializer_class = HumanitarianBottomSectionsSerializer
    queryset = HumanitarianBottomSections.objects.all()
    permission_classes = [IsContentEditor]
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]

class PeaceEducationProgramTopSectionView(ModelViewSet):
    serializer_class = PeaceEducationProgramTopSectionSerializer
    queryset = PeaceEducationProgramTopSection.objects.all()
    permission_classes = [IsContentEditor]
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]
