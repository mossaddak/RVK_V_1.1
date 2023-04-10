from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
ORDER_STATUS_CHOICES = [
        ('Humanitarian', 'Humanitarian'),
        ('Peace Education Program', 'Peace Education Program'),
        ('Peace Education & Knowledge', 'Peace Education & Knowledge'),
    ]

# class Initiative(models.Model):
#     title = forms.ChoiceField(choices = GEEKS_CHOICES)


#Humanitarian=================================================
class HumanitarianTopSection(models.Model):
    category = models.CharField(null=True,blank=False,max_length=50, choices=ORDER_STATUS_CHOICES)
    title = models.CharField(max_length=350, null=True, blank=False)
    first_desc = RichTextUploadingField(blank=True, null=True, verbose_name="First Description")
    second_desc = RichTextUploadingField(blank=True, null=True, verbose_name="Second Description")

    img = models.ImageField(blank=False, null=True)


    def __str__(self):
        return f"{self.pk}.{self.title}"
    
    class Meta:
        verbose_name_plural = 'Humanitarian Top Section'
    
class HumanitarianBottomSections(models.Model):
    category = models.CharField(null=True, blank=False, max_length=50, choices=ORDER_STATUS_CHOICES)
    title = models.CharField(max_length=350, null=True, blank=False, verbose_name="Title")
    first_desc = RichTextUploadingField(blank=True, null=True, verbose_name = "First Description")
    img = models.ImageField(blank=False, null=True)

    def __str__(self):
        return f"{self.pk}.{self.title}"
    
    class Meta:
        verbose_name_plural = 'Humanitarian Top Section'


#Peace Education Program=================================================
class PeaceEducationProgramTopSection(models.Model):
    title = models.CharField(max_length=350, null=True)
    image = models.ImageField(null=True, blank=True)
    desc = RichTextUploadingField(blank=True, null=True, verbose_name = "Description")

    class Meta:
        verbose_name_plural = 'Peace Education Program Top Section'

class PeaceEducationProgramSecondSection(models.Model):
    desc = RichTextUploadingField(blank=True, null=True, verbose_name = "Description")
    image = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Peace Education Program Middle Section'

