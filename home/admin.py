from django.contrib import admin
from .models import(
    Banner,
    LatestVideo,
    Initiative
)

# Register your models here.
admin.site.register(Banner)
admin.site.register(LatestVideo)
admin.site.register(Initiative)