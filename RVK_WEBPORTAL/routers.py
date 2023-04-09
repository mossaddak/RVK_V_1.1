from rest_framework import routers
from accounts.views import AccountViewSet
from django.urls import path
from posts.views import PostViewSet

#event
from events.views import (
    EventViewSet,
    EventRegisterViewSet,
)

from support.views import SupportViewset
from careers.views import (
    CareerViewset,
    CareerDescModelView
)
from volunteers.views import VolunteerViewset
from contacts.views import ContactViewset
from announcements.views import AnnouncementViewset

#home
from home.views import (
    BannerModelView,
    LatestVideoModelView,
    InitiativeVideoModelView,
    NewsShelterViewset
)

from password_recover.views import (
    PasswordReset,
    ResetPasswordAPI
)

from news.views import(
    NewsCategoryModelView,
    NewsModelView
)

from about.views import(
    RvkAboutBannerView,
    RvkAboutDescriptionView,
    QuickLinksView
)
from about_prem_rawat.views import(
    PremRawatAboutBannerView,
    PremRawattDescriptionView
)

from media_gallery.views import(
    BannerView,
    GalleryCategoryView,
    MediaView
)

#payment
from events.views import(
    EventRegisterViewSet
)






router = routers.DefaultRouter()

router.register(r'accounts', AccountViewSet)
router.register(r'posts',PostViewSet)

#event
router.register(r'events',EventViewSet)
#router.register(r'eventregister',EventRegisterViewSet)


router.register(r'careers',CareerViewset)
router.register(r'volunteers',VolunteerViewset)
router.register(r'contact',ContactViewset)
router.register(r'announcements',AnnouncementViewset)

#home
router.register(r'home_banner',BannerModelView)
router.register(r'latestvideo',LatestVideoModelView)
router.register(r'initiative',InitiativeVideoModelView)
router.register(r'newsshelter',NewsShelterViewset)

#router.register(r'donate',DonationView)

router.register(r'news',NewsModelView)
router.register(r'news_category',NewsCategoryModelView)
router.register(r'career_desc',CareerDescModelView)

router.register(r'rvkaboutbanner',RvkAboutBannerView)
router.register(r'rkbaboutdescription',RvkAboutDescriptionView)
router.register(r'quicklinkview',QuickLinksView) 

router.register(r'premrawataboutbanner',PremRawatAboutBannerView)
router.register(r'premrawatdescription',PremRawattDescriptionView)

router.register(r'mediabannerview',BannerView)
router.register(r'gallerycategory',GalleryCategoryView)
router.register(r'mediaview',MediaView)

#payment






urlpatterns = [
    #path('event_register/', EventRegisterViewSet.as_view(), name="event_register"),
    # path('reset-password/', PasswordReset.as_view(), name="reset-password/"),
    # path('reset-password/<str:encoded_pk>/<str:token>/',ResetPasswordAPI.as_view()),
    
]+ router.urls