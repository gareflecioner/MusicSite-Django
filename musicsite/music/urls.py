from django.conf.urls.static import static
from django.urls import path,include

from musicsite import settings
from .views import *



urlpatterns = [
    path('',home),
    path('musicians/',musicians),
    path('albums/',albums),
    path('about/',about),
    path('feedback/',feedback),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
