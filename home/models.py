from django.db import models

# Create your models here.
class Banner(models.Model):
    img = models.ImageField(upload_to="home/banner", null=True, blank=False)

    def __str__(self):
        return f"{self.pk}.{self.img}"
    
class LatestVideo(models.Model):
    thumbnail = models.ImageField(blank=False, null=True)
    video_link = models.CharField(max_length=350, null=True, blank=False, verbose_name='Video Link')
    play_list_link = models.CharField(max_length=350, null=True, blank=False, verbose_name='Video Playlist Link')

    def __str__(self):
        return f"{self.pk}.{self.video_link}"
    
    class Meta:
        verbose_name_plural = 'Latest Videos'

class Initiative(models.Model):
    title = models.CharField(max_length=350, null=True, blank=False)
    sub_title = models.CharField(max_length=350, null=True, blank=True)
    img = models.ImageField(blank=False, null=True, upload_to="home/initiative")

    def __str__(self):
        return f"{self.pk}.{self.title}" 

    
