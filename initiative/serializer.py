from rest_framework import serializers

from .models import(
    HumanitarianTopSection,
    HumanitarianBottomSections,
    PeaceEducationProgramTopSection,
    PeaceEducationProgramSecondSection
)

class HumanitarianTopSectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = HumanitarianTopSection
        fields = "__all__"

class HumanitarianBottomSectionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = HumanitarianBottomSections
        fields = "__all__"


class PeaceEducationProgramTopSectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = PeaceEducationProgramTopSection
        fields = "__all__"

class PeaceEducationProgramSecondSectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = PeaceEducationProgramSecondSection
        fields = "__all__"



