from django.contrib import admin
from .models import(
    HumanitarianTopSection,
    HumanitarianBottomSections,
    PeaceEducationProgramTopSection
)

# Register your models here.
admin.site.register(HumanitarianTopSection)
admin.site.register(HumanitarianBottomSections)
admin.site.register(PeaceEducationProgramTopSection)